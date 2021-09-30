import cv2
import numpy as np

def color_mask(image, color):
    image = cv2.imread(image)
    mask = cv2.inRange(image, color, color)
    return mask

def count_pixels(image, color):
    mask = color_mask(image, color)
    return np.count_nonzero(mask)

def task(image):
    black_mask = color_mask(image, (0, 0, 0))
    white_mask = color_mask(image, (255, 255, 255))
    count_black = np.count_nonzero(black_mask)
    count_white = np.count_nonzero(white_mask)

    if count_black > count_white:
        return f'Ч:{count_black}, Б:{count_white} Черных пикселей больше'
    elif count_black < count_white:
        return f'Ч:{count_black}, Б:{count_white} Белых пикселей больше'
    else:
        return f'Ч:{count_black}, Б:{count_white} Черных и белых одинаково'

if __name__ == '__main__':
    print(task('test.jpg'))