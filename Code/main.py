# -*- coding: utf-8 -*-
"""Car_Number_Plate_Detection_And_Character_Recognition .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1taYMNPu8oTpDCt12unsJ-n7rYUCSTBI4

**Car Number Plate Detection And Character Recognition**. In Google Colab, using YOLO-v8 Model And the Datasate from Roboflow.
"""

pip install opencv-python-headless gdown

from google.colab import drive
drive.mount('/content/drive')

dataset_path = "/content/drive/MyDrive/Colab Notebooks/CarPhoto"

import os
print(os.listdir("/content/drive/MyDrive/Colab Notebooks/CarPhoto"))

pip install ultralytics
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

# Train the model
model.train(
    data=f"/content/drive/MyDrive/Colab Notebooks/CarPhoto/data.yaml",
    epochs=5,
    batch=16,
    imgsz=640,
    name="car_number_plate_detector"
)

metrics = model.val()
print(metrics)

# Predict on a test image
test_image_path = "/content/drive/MyDrive/Colab Notebooks/test_image1.jpg"

results = model.predict(source="/content/drive/MyDrive/Colab Notebooks/test_image1.jpg", save=True, conf=0.1)

# Import the necessary module for displaying images
from IPython.display import Image

# Display the result
Image(filename="/content/drive/MyDrive/Colab Notebooks/test_image1.jpg")

metrics.box.map50

import matplotlib.pyplot as plt

if hasattr(metrics.box, 'map50') and hasattr(metrics.box, 'map'):
  map50 = metrics.box.map50
  map = metrics.box.map
  plt.plot([0, 1], [map50, map], marker='o')  # Create the plot
  plt.xlabel("Threshold")
  plt.ylabel("mAP")
  plt.title("Mean Average Precision (mAP)")
  plt.xticks([0, 1], ['0.5', '0.5:0.95'])
  plt.grid(True)  # Add a grid
  plt.show()
else:
  print("Error: 'map50' or 'map' attribute not found in the metrics object")

#For Charecter Recogonation
import locale
def getpreferredencoding(do_setlocale = True):
    return "UTF-8"
locale.getpreferredencoding = getpreferredencoding
!pip install easyocr

import easyocr
import cv2
from matplotlib import pyplot as plt
from ultralytics import YOLO

# Verify the correct path to your best.pt file
best_weights_path = 'runs/detect/car_number_plate_detector8/weights/best.pt' # Make sure this is the actual path where the 'best.pt' file is located

# Check if the file exists
import os
if not os.path.exists(best_weights_path):
    print(f"Error: File not found at {best_weights_path}. Please verify the path or train the model first.")
else:
    model = YOLO(best_weights_path)

    # Predict on a test image
    results = model.predict(source=test_image_path, save=True, conf=0.25)

    # Assuming the first result is the number plate
    crops = results[0].plot()
    cv2.imwrite("detected_plate.jpg", crops)


    # Initialize EasyOCR reader
    reader = easyocr.Reader(['bn', 'en'])


    # Perform OCR on the cropped image
    result = reader.readtext('detected_plate.jpg')

    # Print the detected text
    for detection in result:
        text = detection[1]
        print(f"Detected Text: {text}")

try:
  metrics_dict = metrics.box
  # Extract mAP values
  map50 = metrics_dict.map50
  map = metrics_dict.map

  # Create the plot
  plt.plot([0, 1], [map50, map], marker='o')
  plt.xlabel("Threshold")
  plt.ylabel("mAP")
  plt.title("Mean Average Precision (mAP)")
  plt.xticks([0, 1], ['0.5', '0.5:0.95'])
  plt.grid(True)
  plt.show()

except AttributeError:
  print("Metrics not available or in an unexpected format.")
  if isinstance(metrics, dict) and 'metrics' in metrics and isinstance(metrics['metrics'], dict):
      print(metrics['metrics'])
  else:
    print(metrics)

try:
  metrics_dict = metrics.box
  # Print the F1-score
  print("F1 Score:", 2 * (metrics_dict.p * metrics_dict.r) / (metrics_dict.p + metrics_dict.r))
except AttributeError:
  print("Metrics not available or in an unexpected format.")
  if isinstance(metrics, dict) and 'metrics' in metrics and isinstance(metrics['metrics'], dict):
      print(metrics['metrics'])
  else:
    print(metrics) # Indented 'print(metrics)' to be part of the 'else' block

!pip install python-Levenshtein # This line installs the Levenshtein module
!pip install easyocr
import easyocr
import cv2
from matplotlib import pyplot as plt
from ultralytics import YOLO
import Levenshtein


# Verify the correct path to your best.pt file
best_weights_path = 'runs/detect/car_number_plate_detector8/weights/best.pt'  # Make sure this is the actual path where the 'best.pt' file is located

# Check if the file exists
import os

if not os.path.exists(best_weights_path):
    print(
        f"Error: File not found at {best_weights_path}. Please verify the path or train the model first.")
else:
    model = YOLO(best_weights_path)

    # Predict on a test image
    results = model.predict(source=test_image_path, save=True, conf=0.25)

    # Assuming the first result is the number plate
    crops = results[0].plot()
    cv2.imwrite("detected_plate.jpg", crops)

    # Initialize EasyOCR reader
    reader = easyocr.Reader(['bn', 'en'])

    # Perform OCR on the cropped image
    result = reader.readtext('detected_plate.jpg')

    # ---  CER/WER calculation starts here ---
    ground_truth_text = "For OCR"

    # Initialize variables to store CER and WER
    cer_sum = 0
    wer_sum = 0
    num_detections = 0

    for detection in result:
        text = detection[1]
        print(f"Detected Text: {text}")

        # Calculate CER
        cer = Levenshtein.distance(text, ground_truth_text) / len(
            ground_truth_text)
        cer_sum += cer

        # Calculate WER (word error rate)
        text_words = text.split()
        ground_truth_words = ground_truth_text.split()
        wer = Levenshtein.distance(" ".join(text_words),
                                   " ".join(ground_truth_words)) / len(
            ground_truth_words)
        wer_sum += wer

        num_detections += 1

    if num_detections > 0:
        average_cer = cer_sum / num_detections
        average_wer = wer_sum / num_detections
        print(f"\nAverage Character Error Rate (CER): {average_cer}")
        print(f"Average Word Error Rate (WER): {average_wer}")
    else:
        print("\nNo text detections found to calculate CER/WER.")

try:
    metrics_dict = metrics.box
    # Print relevant metrics from the dictionary, including computation time
    print("Precision:", metrics_dict.p)
    print("Recall:", metrics_dict.r)
    print("mAP@0.5:", metrics_dict.map50)
    print("mAP@0.5:0.95:", metrics_dict.map)

    # Accessing speed metrics (adjust keys as needed)
    print("Training time:", metrics.speed.get('train', 'Not available'))
    print("Inference time:", metrics.speed.get('inference', 'Not available'))

except AttributeError:
    print("Metrics not available or in an unexpected format.")
    if isinstance(metrics, dict) and 'metrics' in metrics and isinstance(metrics['metrics'], dict):
        print(metrics['metrics'])
    else:
        print(metrics)

import matplotlib.pyplot as plt

try:
    metrics_dict = metrics.box
    # Extract training and test accuracy (replace with your actual metric names)
    train_accuracy = [metrics_dict.p, metrics_dict.r]
    test_accuracy = [metrics_dict.map50, metrics_dict.map]

    # Create the plot
    plt.plot(train_accuracy, label='Training Accuracy')
    plt.plot(test_accuracy, label='Test Accuracy')

    plt.xlabel('Epochs')  # Replace with appropriate x-axis label if needed
    plt.ylabel('Accuracy')
    plt.title('Training and Test Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()

except AttributeError:
    print("Metrics not available or in an unexpected format.")
    if isinstance(metrics, dict) and 'metrics' in metrics and isinstance(metrics['metrics'], dict):
        print(metrics['metrics'])
    else:
        print(metrics) # Indented 'print(metrics)' to be part of the 'else' block