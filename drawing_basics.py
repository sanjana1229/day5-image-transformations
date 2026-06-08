import numpy as np
import cv2

# Black canvas
canvas = np.zeros((400, 400, 3), dtype="uint8")
cv2.imshow("Black Canvas", canvas)
cv2.waitKey(0)

# White canvas
white_canvas = np.ones((400, 400, 3), dtype="uint8") * 255
cv2.imshow("White Canvas", white_canvas)
cv2.waitKey(0)

cv2.destroyAllWindows()
canvas = np.zeros((400, 400, 3), dtype="uint8")

# Green diagonal
cv2.line(canvas, (0, 0), (400, 400), (0, 255, 0), 3)

# Red diagonal
cv2.line(canvas, (400, 0), (0, 400), (0, 0, 255), 5)

# Blue horizontal
cv2.line(canvas, (0, 200), (400, 200), (255, 0, 0), 2)

# Yellow vertical
cv2.line(canvas, (200, 0), (200, 400), (0, 255, 255), 2)

cv2.imshow("Lines", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
canvas = np.zeros((400, 400, 3), dtype="uint8")

# Outlined rectangle
cv2.rectangle(canvas, (50, 50), (150, 150), (0, 255, 0), 3)

# Another outlined rectangle
cv2.rectangle(canvas, (200, 50), (350, 150), (255, 0, 0), 5)

# Filled rectangles
cv2.rectangle(canvas, (50, 200), (150, 300), (0, 0, 255), -1)
cv2.rectangle(canvas, (200, 200), (350, 300), (0, 255, 255), cv2.FILLED)

cv2.imshow("Rectangles", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
canvas = np.zeros((400, 400, 3), dtype="uint8")
center = (200, 200)

# Single circle
cv2.circle(canvas, center, 50, (255, 255, 255), 3)

# Concentric circles
for r in range(20, 200, 20):
    color = (0, 0, 255) if r % 40 == 20 else (255, 255, 255)
    cv2.circle(canvas, center, r, color, 3)

cv2.imshow("Circles", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
canvas = np.zeros((400, 400, 3), dtype="uint8")

cv2.putText(canvas, "Hello OpenCV!", (50, 100),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

cv2.imshow("Text", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

