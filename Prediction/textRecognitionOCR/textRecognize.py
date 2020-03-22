import cv2 as cv
from PIL import Image
import re
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"D:\Software Setups\Tesseract-OCR\tesseract.exe"


im = Image.open("LabRep.png")
text = pytesseract.image_to_string(im, lang="eng")
print(text)
li = text.split("\n")
dictionary = {}
for line in li:
    # print(line)
    if ":" in line:
        s = line.split(":")
        key = s[0]
        value = s[1]
        key = key.strip()
        value = value.strip()
        dictionary[key] = value
print(dictionary)
val = list(dictionary.values())
print("------------------------------------------------------")
print(val)
