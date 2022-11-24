from rembg import remove
from PIL import Image
import easygui as eg
from pathlib import Path

input_paths = eg.fileopenbox(title='Select image file', filetypes=[["*.png", "*.jpg", "Image files"]], multiple=True)
output_path = 'output/'

for input_path in input_paths:
   image = Image.open(input_path)
   filename = Path(input_path).stem
   print(filename)
   output = remove(image)
   saved = output.save(output_path + filename + '.png')
