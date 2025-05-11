
# 🚗 Car Number Plate Detection and Character Recognition (Bangla + English)

This project focuses on detecting vehicle number plates from images and recognizing characters (both Bangla and English) using deep learning techniques. The system is built with YOLOv8 for number plate detection and EasyOCR for multilingual optical character recognition (OCR). It is specifically tailored for the context of Bangladeshi vehicles, using CCTV-captured images.

## 🧠 Project Objectives

- Detect number plates from real-world vehicle images using a robust object detection model.
- Recognize alphanumeric characters, including **Bangla and English** fonts, from the detected plates.
- Support traffic automation, surveillance systems, and smart city applications in Bangladesh.
- Improve detection and recognition accuracy in noisy, low-resolution, and real-world scenarios.

---

## 🚀 Features

- ✅ YOLOv8-based plate detection.
- ✅ EasyOCR-based character recognition (Bangla + English).
- ✅ Custom dataset annotated via Roboflow.
- ✅ Integration with Google Drive and Google Colab.
- ✅ Support for CCTV image streams and offline image processing.

---

## 🗂️ Project Structure

```
📁 numberplate-recognition/
├── 📂 yolov8_detection/
│   ├── detect.py
│   ├── trained_weights.pt
│   └── utils/
├── 📂 easyocr_ocr/
│   ├── recognize.py
│   └── output_text/
├── 📂 dataset/
│   └── images + labels (via Roboflow)
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🛠️ Tech Stack

| Component            | Library / Tool         |
|---------------------|------------------------|
| Detection Model      | YOLOv8 (Ultralytics)   |
| Character Recognition| EasyOCR                |
| Dataset Management   | Roboflow               |
| Image Storage        | Google Drive           |
| Development Platform | Google Colab / Python  |
| Language Support     | Bangla, English        |

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/numberplate-recognition.git
   cd numberplate-recognition
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Colab:**
   - Mount your Google Drive.
   - Upload the dataset/images to a folder (path configurable in `detect.py` and `recognize.py`).

4. **Run the pipeline:**

   - **Step 1: Detect number plates**
     ```bash
     python yolov8_detection/detect.py
     ```

   - **Step 2: Recognize characters**
     ```bash
     python easyocr_ocr/recognize.py
     ```

---

## 🧾 Dataset

- Custom dataset collected from **CCTV camera feeds** in Bangladesh.
- Annotated using **Roboflow** with YOLO format (`.txt` labels).
- Contains diverse images under real-world conditions (day/night, various plate styles).
- Includes both **Bangla** and **English** number plates.

---

## 🧪 Results & Performance

| Metric             | Value       |
|--------------------|-------------|
| Detection Accuracy | ~92% (YOLOv8) |
| OCR Accuracy       | ~89% (EasyOCR on mixed plates) |
| FPS (Avg)          | 10–15 (Colab, GPU) |
| Bangla Support     | ✅ Full OCR Support |

Sample Output:

> 🚘 Image → 📷 Detected Plate → 🔤 Recognized Text → ✅ Displayed Result

---

## 📈 Use Cases

- Smart traffic monitoring.
- Automated toll collection.
- Law enforcement and vehicle tracking.
- Parking lot automation.

---

## 📚 Future Improvements

- Switch to a custom OCR model trained on Bangla-only datasets for improved accuracy.
- Support for real-time video feed processing.
- Integration with vehicle databases for owner identification.
- Deploy as a web dashboard or mobile app.

---

## 🙌 Acknowledgments

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [Roboflow](https://roboflow.com/) for dataset annotation.
- Daffodil International University for research support.

---

## 📜 License

This project is for academic and research use only. For commercial use, please contact the author.

---

## 👤 Author

**Abdullah Al Noman**  
CSE, Daffodil International University  
📧 Email: noman15-5387@diu.edu.bd 
🌐 GitHub: [@AbdullahAlNoman20](https://github.com/AbdullahAlNoman20)
