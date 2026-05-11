import cv2
import os

# Folder containing videos
video_folder = "videos"

# Folder to save frames
output_folder = "frames"

# Create output folder
os.makedirs(output_folder, exist_ok=True)

# Get all video files
video_files = [f for f in os.listdir(video_folder) if f.endswith(".mp4")]

for video_file in video_files:

    video_path = os.path.join(video_folder, video_file)

    print(f"\nProcessing: {video_file}")

    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    saved_count = 0

    # Create subfolder for each video
    video_name = os.path.splitext(video_file)[0]

    video_output_folder = os.path.join(output_folder,video_file)

    os.makedirs(video_output_folder, exist_ok=True)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Save every 10th frame
        if frame_count % 10 == 0:

            filename = os.path.join(
                video_output_folder,
                f"frame_{saved_count}.jpg"
            )

            cv2.imwrite(filename, frame)

            print(f"Saved: {filename}")

            saved_count += 1

        frame_count += 1

    cap.release()

print("\nDone!")