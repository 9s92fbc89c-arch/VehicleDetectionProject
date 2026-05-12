import cv2

# Your extracted frame path
image_path = "frames/traffic1.mp4/frame_0.jpg"

# Read image
image = cv2.imread(image_path)

# Check if image loaded
if image is None:
    print("Image not found!")
    exit()

# Draw rectangle around vehicle
cv2.rectangle(
    image,
    (150, 200),    # top-left corner
    (550, 400),    # bottom-right corner
    (0, 255, 0),   # green color
    3              # thickness
)

# Add text label
cv2.putText(
    image,
    "Vehicle",
    (100, 140),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0,255,0),
    2
)

# Show image
cv2.imshow("Vehicle Detection", image)

# Save image
cv2.imwrite("vehicle_box.jpg", image)

cv2.waitKey(0)

cv2.destroyAllWindows()