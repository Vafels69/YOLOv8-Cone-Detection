
# **YOLOv8 Cone Detection**

This project demonstrates cone detection using the YOLOv8 object detection model. The model is trained on a dataset of cones (blue, orange, yellow) and tested on real-world images and videos. This work showcases a complete pipeline for training, testing, and deploying a YOLOv8 model for object detection tasks.

---

## **Table of Contents**
1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Training](#training)
   - [Inference](#inference)
4. [Results](#results)
5. [Approach](#approach)
6. [Requirements](#requirements)
7. [License](#license)

---

## **Project Description**
This project aims to detect cones in images and videos using YOLOv8, a state-of-the-art object detection framework. The model is trained on a custom dataset annotated with three classes:
- **Blue Cone**
- **Orange Cone**
- **Yellow Cone**

The dataset was sourced from [Roboflow](https://universe.roboflow.com/) and annotated using the YOLO format. The project runs on a Windows machine and uses Python for implementation.

---

## **Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/YOLOv8-Cone-Detection.git
   cd YOLOv8-Cone-Detection
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

### **Training**
To train the YOLOv8 model:
1. Ensure the `data.yaml` file is correctly configured with your dataset paths.
2. Run the training script:
   ```bash
   python src/train.py
   ```
   This will train the model and save the results (metrics, weights) in the `runs/` folder.

### **Inference**
To run inference on test images or videos:
1. Use the following command:
   ```bash
   python src/inference.py --model runs/detect/train/weights/best.pt --source path/to/test/data
   ```
   Results will be saved in the `results/` directory and include images/videos with bounding boxes drawn around detected cones.

---

## **Results**
Sample outputs from inference are provided in the `results/` folder. Each image contains:
- Bounding boxes around detected cones.
- Class labels and confidence scores.

Example Output:
![Sample Output](results/sample_output.jpg)

---

## **Approach**
1. **Dataset:**
   - The dataset contains images of cones annotated with three classes: blue, orange, and yellow.
   - Train/validation/test split: 70%/20%/10%.

2. **Model:**
   - YOLOv8 Nano (`yolov8n.pt`) was chosen for its speed and efficiency.
   - Trained for 50 epochs with an input size of 640x640.

3. **Metrics:**
   - Mean Average Precision (mAP): 88.5% (example metric, replace with your results).

4. **Inference:**
   - Real-time detection is possible for videos and images.

---

## **Requirements**
- Python 3.10
- Libraries:
  - `ultralytics`
  - `opencv-python-headless`
  - `matplotlib`
  - `torch`

To install these libraries, run:
```bash
pip install -r requirements.txt
```

---

## **License**
This project is licensed under the [MIT License](LICENSE).
