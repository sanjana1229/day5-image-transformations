import numpy as np
import cv2

# Create canvas (white background)
canvas = np.ones((500, 500, 3), dtype="uint8") * 255

# House body
cv2.rectangle(canvas, (150, 250), (350, 450), (0, 0, 0), 3)

# Roof (triangle)
cv2.line(canvas, (150, 250), (250, 120), (0, 0, 255), 3)
cv2.line(canvas, (250, 120), (350, 250), (0, 0, 255), 3)

# Door
cv2.rectangle(canvas, (220, 350), (280, 450), (255, 0, 0), -1)

# Windows
cv2.rectangle(canvas, (170, 280), (220, 330), (0, 255, 0), -1)
cv2.rectangle(canvas, (280, 280), (330, 330), (0, 255, 0), -1)

# Sun
cv2.circle(canvas, (400, 80), 40, (0, 255, 255), -1)

# Title
cv2.putText(canvas, "My Dream House", (150, 70),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2)

cv2.imshow("House", canvas)
cv2.waitKey(0)
cv2.imwrite("house.png", canvas)
cv2.destroyAllWindows()
