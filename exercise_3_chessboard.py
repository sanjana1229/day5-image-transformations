import numpy as np
import cv2

# Each square is 50x50 pixels, so an 8x8 board = 400x400 canvas
square_size = 50
board = np.zeros((400, 400, 3), dtype="uint8")

for row in range(8):
    for col in range(8):
        # Calculate pixel coordinates
        y_start = row * square_size
        y_end = (row + 1) * square_size
        x_start = col * square_size
        x_end = (col + 1) * square_size

        # Alternate colors: white if (row+col) is even, black otherwise
        if (row + col) % 2 == 0:
            board[y_start:y_end, x_start:x_end] = (255, 255, 255)  # White
        else:
            board[y_start:y_end, x_start:x_end] = (0, 0, 0)        # Black

# Show and save
cv2.imshow("Chessboard", board)
cv2.waitKey(0)
cv2.imwrite("chessboard.png", board)
cv2.destroyAllWindows()
