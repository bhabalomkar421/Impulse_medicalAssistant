import tempfile
from pdf2image import convert_from_path
from pdf2image.exceptions import (
	PDFInfoNotInstalledError,
	PDFPageCountError,
	PDFSyntaxError
)
with tempfile.TemporaryDirectory() as path:
	images_from_path = convert_from_path('/home/omkar/Documents/Impulse_medicalAssistant/ML Frontend/templates/pdf_to_imageConvertor/pdfTest.pdf', output_folder='/home/omkar/Documents/Impulse_medicalAssistant/ML Frontend/templates/pdf_to_imageConvertor/output')
for image in images_from_path:
    image.save('sample.png','PNG')
print("working")
