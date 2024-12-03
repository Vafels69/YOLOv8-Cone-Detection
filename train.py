from ultralytics import YOLO


def train_yolov8(data_yaml, model_path='yolov8n.pt', epochs=50, img_size=640):

    model = YOLO(model_path)  # Load a YOLOv8 model
    model.train(data=data_yaml, epochs=epochs, imgsz=img_size, verbose=True)
    print("Training complete. Results saved in the runs/ folder.")


if __name__ == "__main__":
    # Specify the path to your data.yaml file
    DATA_YAML = "C:/Users/user/Downloads/yolo DV.v7i.yolov8/data.yaml"
    train_yolov8(data_yaml=DATA_YAML)
