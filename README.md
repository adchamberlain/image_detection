# Image Detection

Use pre-trained deep learning models from OpenCV to detect faces, gender, and common objects in images using Python. Based on the [cvlib](https://www.cvlib.net/) module.

## 🔒 Security Update (December 2024)

This project has been updated to address critical security vulnerabilities:
- ✅ Updated TensorFlow from 1.14.0 to 2.18.0+ (fixes CVE-2019-16778)
- ✅ Updated PyYAML from 5.1.2 to 6.0+ (fixes CVE-2019-20477, CVE-2020-1747, CVE-2020-14343)
- ✅ Updated requests from 2.22.0 to 2.32.2+ (fixes CVE-2023-32681, CVE-2024-35195)
- ✅ Updated urllib3 and certifi to latest secure versions
- ✅ Modernized code with error handling and dynamic paths

## Features

- 🎭 **Face Detection**: Detect faces in images with bounding boxes
- 👤 **Gender Detection**: Predict gender for detected faces with confidence scores
- 🎯 **Object Detection**: Identify common objects (people, cars, animals, etc.)
- 📊 **Visualization**: Display results with matplotlib
- 💾 **Save Results**: Optionally save annotated images

## Installation

### 1. Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

### 2. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Note**: First installation may take several minutes as it downloads TensorFlow and pre-trained models.

## Usage

### Basic Usage

Run with the default image:
```bash
python image.py
```

### Specify a Custom Image

```bash
python image.py path/to/your/image.jpg
```

### Command-Line Options

```bash
# Disable visualization windows (useful for batch processing)
python image.py image.jpg --no-viz

# Save annotated images to disk
python image.py image.jpg --save

# Specify custom output directory
python image.py image.jpg --save --output-dir ./my_results

# Combine options
python image.py image.jpg --save --no-viz --output-dir ./batch_results
```

### Help

```bash
python image.py --help
```

## Example Output

```
Loading image: getting-ready-for-the-speaker-series.jpg
Image loaded successfully: 1920x1080 pixels

============================================================
STEP 1: Face and Gender Detection
============================================================
Detecting faces...
Found 3 face(s)
Face 1: male: 87.45%
Face 2: female: 92.31%
Face 3: male: 78.90%

============================================================
STEP 2: Object Detection
============================================================
Detecting common objects...
Found 5 object(s): ['person', 'person', 'person', 'chair', 'laptop']

Detailed object detection results:
  1. person: 99.23% confidence
  2. person: 98.76% confidence
  3. person: 97.45% confidence
  4. chair: 89.12% confidence
  5. laptop: 85.67% confidence

============================================================
Detection complete!
============================================================
```

## Requirements

- Python 3.8+
- TensorFlow 2.18.0+
- OpenCV
- cvlib
- See `requirements.txt` for full list

## Security Scanning

To check for security vulnerabilities in dependencies:

```bash
# Install security scanner
pip install safety pip-audit

# Run security check
safety check

# Or use pip-audit
pip-audit
```

## Troubleshooting

### TensorFlow Installation Issues

If you encounter TensorFlow installation errors:

```bash
# For macOS with Apple Silicon (M1/M2/M3)
pip install tensorflow-macos

# For older systems, you may need an older TensorFlow version
pip install tensorflow==2.13.0
```

### Model Download Issues

On first run, cvlib downloads pre-trained models. If this fails:
- Check your internet connection
- Try running with `sudo` (Linux/macOS) if permission errors occur
- Manually download models from [cvlib GitHub](https://github.com/arunponnusamy/cvlib)

### Memory Issues

For large images or limited RAM:
- Resize images before processing
- Process images one at a time
- Close visualization windows between runs

## Project Structure

```
image_detection/
├── image.py                                    # Main detection script
├── requirements.txt                            # Python dependencies
├── README.md                                   # This file
├── getting-ready-for-the-speaker-series.jpg   # Sample image
└── results/                                    # Output directory (created when using --save)
```

## Credits

**Original Author**: Andrew Chamberlain, Ph.D.  
**Website**: [achamberlain.com](https://achamberlain.com)  
**Original Date**: September 2019  
**Updated**: December 2024

Based on the [cvlib](https://www.cvlib.net/) library by Arun Ponnusamy.

## License

See original repository for license information.

## Contributing

Contributions are welcome! Please ensure:
- All dependencies are kept up-to-date
- Security vulnerabilities are addressed promptly
- Code includes proper error handling
- Tests pass before submitting PRs

## Changelog

### December 2024
- 🔒 Fixed critical security vulnerabilities
- ✨ Added command-line argument support
- 🛡️ Added comprehensive error handling
- 📝 Improved documentation
- 🎨 Better code organization and formatting
- 🔧 Fixed hardcoded paths to use relative paths
- 📊 Enhanced output with detailed results

### September 2019
- 🎉 Initial release
