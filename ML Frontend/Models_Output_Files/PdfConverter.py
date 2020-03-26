import tempfile
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
# with tempfile.TemporaryDirectory() as path:
#     images_from_path = convert_from_path(
#         'D:\\IT\\Hackathon\\Impulse\\ML Frontend\\templates\\pdfTest.pdf', output_folder='D:\\IT\\Hackathon\\Impulse\\ML Frontend\\Received_Files')
#     print("working")

with tempfile.TemporaryDirectory() as path:
    images_from_path = convert_from_path(
        'D:\\IT\\Hackathon\\Impulse\\ML Frontend\\templates\\pdfTest.pdf', output_folder='D:\\IT\\Hackathon\\Impulse\\ML Frontend\\Received_Files')
for image in images_from_path:
    image.save('sample.png', 'PNG')
print("working")
