import cv2
import os

# Path to your video file
video_path = r'C:\Users\Pal\Downloads\Telegram Desktop\Security camera inside Pepper Grill restaurant.mp4'

# Output folder for frames
output_folder = 'frames'
os.makedirs(output_folder, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_path)

frame_rate = 1  # Save 1 frame every 1 second
fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = int(fps * frame_rate)

frame_count = 0
saved_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        filename = os.path.join(output_folder, f'frame_{saved_count:04d}.jpg')
        cv2.imwrite(filename, frame)
        saved_count += 1

    frame_count += 1

cap.release()
print(f"Saved {saved_count} frames to '{output_folder}'")



import shutil
shutil.make_archive('frames_zip', 'zip', 'frames')
