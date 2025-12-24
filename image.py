"""
Image Detection Script
Use a pre-trained deep learning model to detect faces, gender, and common objects in web-based images.
Based on cvlib module (cvlib.net).

Updated: December 2024
- Modernized for TensorFlow 2.x compatibility
- Added error handling and input validation
- Fixed hardcoded paths to use relative paths
- Added command-line argument support
- Improved code organization and documentation

Original Author: Andrew Chamberlain, Ph.D.
achamberlain.com
September 2019
"""

import os
import sys
import argparse
from pathlib import Path
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import imutils
import numpy as np


def validate_image_path(image_path):
    """
    Validate that the image file exists and is readable.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Path object if valid
        
    Raises:
        FileNotFoundError: If image doesn't exist
        ValueError: If file is not a valid image format
    """
    path = Path(image_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    if not path.is_file():
        raise ValueError(f"Path is not a file: {image_path}")
    
    valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
    if path.suffix.lower() not in valid_extensions:
        raise ValueError(f"Invalid image format: {path.suffix}. Supported: {valid_extensions}")
    
    return path


def load_image(image_path):
    """
    Load an image from file with error handling.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Loaded image as numpy array
        
    Raises:
        RuntimeError: If image cannot be loaded
    """
    try:
        image = cv2.imread(str(image_path))
        
        if image is None:
            raise RuntimeError(f"Failed to load image: {image_path}")
        
        return image
    except Exception as e:
        raise RuntimeError(f"Error loading image {image_path}: {str(e)}")


def detect_faces_and_gender(image, show_visualization=True):
    """
    Detect faces and gender in an image.
    
    Args:
        image: Input image as numpy array
        show_visualization: Whether to display the results
        
    Returns:
        Annotated image with face and gender detection results
    """
    # Create a copy to avoid modifying the original
    result_image = image.copy()
    
    try:
        # Apply face detection
        print("Detecting faces...")
        faces, confidences = cv.detect_face(result_image)
        
        if len(faces) == 0:
            print("No faces detected in the image.")
            return result_image
        
        print(f"Found {len(faces)} face(s)")
        
        # Draw bounding boxes on faces
        for face in faces:
            startX, startY = face[0], face[1]
            endX, endY = face[2], face[3]
            
            # Draw rectangle over faces
            cv2.rectangle(result_image, (startX, startY), (endX, endY), (0, 255, 0), 2)
        
        # Detect gender for each face
        for idx, face in enumerate(faces):
            startX, startY = face[0], face[1]
            endX, endY = face[2], face[3]
            
            # Crop detected face
            face_crop = np.copy(result_image[startY:endY, startX:endX])
            
            if face_crop.size == 0:
                print(f"Warning: Empty face crop for face {idx + 1}, skipping gender detection")
                continue
            
            try:
                # Apply gender detection on cropped face
                labels, confidence = cv.detect_gender(face_crop)
                
                # Choose most confident label
                max_idx = np.argmax(confidence)
                gender_label = labels[max_idx]
                gender_confidence = confidence[max_idx]
                
                # Format label
                label_text = f"{gender_label}: {gender_confidence * 100:.2f}%"
                print(f"Face {idx + 1}: {label_text}")
                
                # Set label placement
                Y = startY - 10 if startY - 10 > 10 else startY + 10
                
                # Add label to image
                cv2.putText(result_image, label_text, (startX, Y), 
                           cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 0, 0), 2)
                
            except Exception as e:
                print(f"Warning: Gender detection failed for face {idx + 1}: {str(e)}")
                continue
        
        # Show results
        if show_visualization:
            plt.figure(figsize=(12, 8))
            plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
            plt.title("Face and Gender Detection Results")
            plt.axis('off')
            plt.tight_layout()
            plt.show()
        
        return result_image
        
    except Exception as e:
        print(f"Error during face/gender detection: {str(e)}")
        raise


def detect_objects(image, show_visualization=True):
    """
    Detect common objects in an image.
    
    Args:
        image: Input image as numpy array
        show_visualization: Whether to display the results
        
    Returns:
        Annotated image with object detection results
    """
    try:
        print("\nDetecting common objects...")
        
        # Detect common objects in image
        bbox, labels, confidences = cv.detect_common_objects(image)
        
        if len(labels) == 0:
            print("No objects detected in the image.")
            return image
        
        print(f"Found {len(labels)} object(s): {labels}")
        
        # Draw bounding boxes on objects
        result_image = draw_bbox(image, bbox, labels, confidences)
        
        # Show results
        if show_visualization:
            plt.figure(figsize=(12, 8))
            plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
            plt.title("Object Detection Results")
            plt.axis('off')
            plt.tight_layout()
            plt.show()
        
        # Print detailed results
        print("\nDetailed object detection results:")
        for i, (label, conf) in enumerate(zip(labels, confidences)):
            print(f"  {i + 1}. {label}: {conf * 100:.2f}% confidence")
        
        return result_image
        
    except Exception as e:
        print(f"Error during object detection: {str(e)}")
        raise


def save_results(image, output_path, prefix="result"):
    """
    Save the annotated image to file.
    
    Args:
        image: Image to save
        output_path: Directory to save the image
        prefix: Filename prefix
    """
    try:
        output_dir = Path(output_path)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / f"{prefix}_{Path(output_path).stem}.jpg"
        cv2.imwrite(str(output_file), image)
        print(f"\nSaved result to: {output_file}")
        
    except Exception as e:
        print(f"Warning: Failed to save results: {str(e)}")


def main():
    """
    Main function to run image detection pipeline.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Detect faces, gender, and objects in images using deep learning"
    )
    parser.add_argument(
        "image_path",
        nargs='?',
        default="getting-ready-for-the-speaker-series.jpg",
        help="Path to the input image (default: getting-ready-for-the-speaker-series.jpg)"
    )
    parser.add_argument(
        "--no-viz",
        action="store_true",
        help="Disable visualization windows"
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save annotated images to disk"
    )
    parser.add_argument(
        "--output-dir",
        default="./results",
        help="Directory to save results (default: ./results)"
    )
    
    args = parser.parse_args()
    
    try:
        # Validate and load image
        print(f"Loading image: {args.image_path}")
        image_path = validate_image_path(args.image_path)
        image = load_image(image_path)
        
        print(f"Image loaded successfully: {image.shape[1]}x{image.shape[0]} pixels")
        
        # Step 1: Detect faces and gender
        print("\n" + "="*60)
        print("STEP 1: Face and Gender Detection")
        print("="*60)
        
        face_result = detect_faces_and_gender(
            image.copy(),
            show_visualization=not args.no_viz
        )
        
        if args.save:
            save_results(face_result, args.output_dir, prefix="faces_gender")
        
        # Step 2: Detect common objects
        print("\n" + "="*60)
        print("STEP 2: Object Detection")
        print("="*60)
        
        object_result = detect_objects(
            image.copy(),
            show_visualization=not args.no_viz
        )
        
        if args.save:
            save_results(object_result, args.output_dir, prefix="objects")
        
        print("\n" + "="*60)
        print("Detection complete!")
        print("="*60)
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        print("\nUsage: python image.py <path_to_image>", file=sys.stderr)
        sys.exit(1)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()