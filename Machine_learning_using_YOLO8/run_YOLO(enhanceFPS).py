import os
import django
import cv2
from picamera2 import Picamera2
from ultralytics import YOLO
from datetime import datetime

# Load Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yolo_project.settings')
django.setup()

from detections.models import Detection  # Import Django model

# Set up the camera with Picam
picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280, 1280)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# Load YOLOv8 model
model = YOLO("yolov8n_ncnn_model")

while True:
    # Capture a frame from the camera
    frame = picam2.capture_array()

    # Run YOLO model on the captured frame and store results
    results = model(frame)

    # Process detection results
    for detection in results[0].boxes.data:
        class_id, confidence, x1, y1, x2, y2 = detection[:6]
        
        # Optionally save the frame as an image file
        image_filename = f"frame_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(f"media/images/{image_filename}", frame)
        
        # Save detection to PostgreSQL via Django model
        Detection.objects.create(
            image_name=image_filename,  # Store filename if saving images
            class_id=int(class_id),
            confidence=float(confidence),
            detected_at=datetime.now()
        )

    # Draw bounding boxes and display annotated frame
    annotated_frame = results[0].plot()

    # Display FPS
    inference_time = results[0].speed['inference']
    fps = 1000 / inference_time  # Convert to milliseconds
    text = f'FPS: {fps:.1f}'
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, 1, 2)[0]
    text_x = annotated_frame.shape[1] - text_size[0] - 10
    text_y = text_size[1] + 10
    cv2.putText(annotated_frame, text, (text_x, text_y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Show camera feed
    cv2.imshow("Camera", annotated_frame)

    # Exit loop on "q" key press
    if cv2.waitKey(1) == ord("q"):
        break

# Cleanup
cv2.destroyAllWindows()


if(){
    
}