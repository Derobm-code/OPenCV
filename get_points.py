import cv2

# List to store points
points = []

# Mouse callback function
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Image", image)
        if len(points) == 4:
            print("Clicked points:", points)
            cv2.destroyAllWindows()

# Load the image
image_path = "pyimagesearch/image.png"  # <-- Update if needed
image = cv2.imread(image_path)

if image is None:
    print("Image not found. Check the path.")
else:
    cv2.imshow("Image", image)
    cv2.setMouseCallback("Image", click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if len(points) == 4:
        print("\nUse these coords in your script:")
        print(points)
    else:
        print("\nYou need to click exactly 4 points.")
