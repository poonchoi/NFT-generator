from PIL import Image
import numpy as np

# generates base image based on generated colors
def img_generator(BC, BG, im, data):
    """
    Generates the standard duck image with no accessories
    """
    new_img = []

    for i in data:
        if i == (255,0,0):
            new_img.append(BG)

        elif i == (0,255,0):
            new_img.append(BC)

        else:
            new_img.append(i)

    # new_img = [new_img.append(BG) if i==(255,0,0) else new_img.append(i) new_img.append(BC) if i==(0,255,0) else new_img.append(i) for i in data]
    # new_img = [new_img.append(BG) if i==(255,0,0) else new_img.append(i) for i in data]
    # new_img = [new_img.append(BC) if i==(0,255,0) else new_img.append(i) for i in data]

    # new dimensions for image
    dimensions = (420,420)

    # array handling with numpy
    new_img = np.array(new_img, dtype=np.uint8)
    new_img = new_img.reshape(30,30,3)

    # using PIL to turn the RGB values into an image
    img_data = Image.fromarray(new_img, 'RGB')
    img_data = img_data.resize(dimensions, resample=0)

    return img_data