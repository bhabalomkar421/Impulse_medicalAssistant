import cv2 as cv
from PIL import Image
import re
import pytesseract
im = Image.open("lab.png")
text = pytesseract.image_to_string(im,lang="eng")
# print(text)
name = re.findall(r"Name",text)
#print(name)
li = []
li1 = []
li = text.split("\n")
for i in li:
    li1 = i.split(" ")
    sIndex = li1.index("Name")
print(i[sIndex+1])