import re
import cv2
from PIL import Image
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"D:\Software Setups\Tesseract-OCR\tesseract.exe"


def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite("removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite("thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open("thres.png"))

    # Remove template file
    # os.remove(temp)

    return result


result = get_string("Sample.png")

# result = result.split("\n")
print(result)

final = []

for sentence in result:
    pattern = ".* : (.*)"
    output = re.search(pattern, sentence)
    if output:
        final.append(output.group(1))

print("\n\n\n")
print(final)
name = final[0]
age = final[1]
sex = final[2]
reportID = final[3]

final = final[4:]
print("\n\n\n")

print("Name : ", name, "\nAge : ", age, "\nSex : ", sex)
print()
print("Report final resuls :- \n", final)
