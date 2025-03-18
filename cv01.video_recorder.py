import cv2
import time

# Initialize the webcam (Camera Index 0)
cap = cv2.VideoCapture(0)

# Check if the webcam is accessible
if not cap.isOpened():
    print("❌ Error: Could not open camera. Ensure your webcam is connected and try again.")
    exit()

# Get frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create a VideoWriter object to save video
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for AVI format
fps = 20.0  # Frames per second
output_filename = "recorded_video.avi"
out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

# State variables
recording = False  # Track recording state
start_time = None  # Store recording start time

print("Press SPACE to start/stop recording. Press ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error: Could not read frame.")
        break

    # If recording, write the frame to the video file
    if recording:
        out.write(frame)
        elapsed_time = int(time.time() - start_time)

        # Display a red recording indicator
        cv2.circle(frame, (50, 50), 10, (0, 0, 255), -1)
        cv2.putText(frame, f"Recording: {elapsed_time}s", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame (Preview)
    cv2.imshow("Video Recorder", frame)

    # Key press detection
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key to exit
        break
    elif key == 32:  # SPACE key to start/stop recording
        recording = not recording
        if recording:
            start_time = time.time()
        print("🎥 Recording started" if recording else "⏹️ Recording stopped")

# Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"The video is saved as '{output_filename}'")
