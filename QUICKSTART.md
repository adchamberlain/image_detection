# Quick Start Guide

Get up and running with the updated `image_detection` project in 5 minutes!

## 🚀 Installation (2 minutes)

```bash
# 1. Navigate to the project directory
cd /Users/andrewchamberlain/github/image_detection

# 2. Create a virtual environment
python3 -m venv venv

# 3. Activate it
source venv/bin/activate

# 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

**Note**: First installation downloads TensorFlow and models (~500MB). This may take a few minutes.

## ✨ Basic Usage (1 minute)

```bash
# Run with the sample image
python image.py

# Run with your own image
python image.py path/to/your/photo.jpg
```

## 🎯 Common Use Cases

### Save Results to Disk
```bash
python image.py my_photo.jpg --save
# Results saved to ./results/
```

### Batch Processing (No Windows)
```bash
python image.py photo1.jpg --no-viz --save
python image.py photo2.jpg --no-viz --save
python image.py photo3.jpg --no-viz --save
```

### Custom Output Directory
```bash
python image.py photo.jpg --save --output-dir ./my_results
```

## 📖 What It Does

1. **Face Detection**: Finds all faces in the image
2. **Gender Detection**: Predicts gender for each face with confidence scores
3. **Object Detection**: Identifies common objects (people, cars, animals, etc.)
4. **Visualization**: Shows results with bounding boxes and labels

## 🔍 Example Output

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

## 🛠️ Troubleshooting

### "Command not found: python3"
Try `python` instead of `python3`:
```bash
python -m venv venv
```

### "No module named 'cv2'"
Make sure you activated the virtual environment:
```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### "Image file not found"
Use the full path or ensure you're in the correct directory:
```bash
python image.py /full/path/to/image.jpg
```

### TensorFlow Installation Issues (macOS M1/M2/M3)
```bash
pip install tensorflow-macos
```

## 📚 Learn More

- **Full Documentation**: See `README.md`
- **Security Details**: See `SECURITY_AUDIT.md`
- **Migration Info**: See `MIGRATION_GUIDE.md`

## 🔐 Security Status

✅ All critical vulnerabilities fixed  
✅ Modern, maintained dependencies  
✅ Production-ready code  

Last security scan: December 24, 2024  
Status: **0 vulnerabilities found**

## 💡 Tips

1. **First run is slower**: Models are downloaded on first use
2. **Large images**: May take longer to process
3. **Better results**: Use well-lit, high-quality images
4. **Multiple faces**: Works best with frontal faces

## 🎓 Next Steps

1. Try it with your own images
2. Experiment with different command-line options
3. Check out the full documentation in README.md
4. Consider integrating into your own projects

---

**Need help?** Check the full README.md or open an issue on GitHub.

**Ready to go?** Run: `python image.py`
