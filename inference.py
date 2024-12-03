from ultralytics import YOLO


def run_inference(model_path, source, save_dir="results/"):
    
    model = YOLO(model_path)  # Load the trained model
    results = model.predict(source=source, save=True, save_dir=save_dir, conf=0.5)
    print(f"Inference complete. Results saved in {save_dir}.")


if __name__ == "__main__":
    # Specify the model weights and source for inference
    MODEL_PATH = "runs/detect/train/weights/best.pt"
    SOURCE = "C:/Users/user/Downloads/fsd1"  # Path to test images or videos
    run_inference(model_path=MODEL_PATH, source=SOURCE)
