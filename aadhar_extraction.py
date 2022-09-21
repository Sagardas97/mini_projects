import pytesseract
from PIL import Image
import datetime
import cv2
import sys
import os
import os.path
import re
import numpy as np
import platform
from pdf2image import convert_from_path
#class to extract text from an image where the image file is passed as an argument
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
poppler_path = "C:/Program Files/poppler-0.68.0/bin/"


# #Function to extract the text from image as string 
# def extract_text(image_file): 

     
#     return text    

path="E:/aadhar_card/"
# image_file_list=[]

for file in os.listdir(path):
    if file.split(".")[-1]== "pdf":
    # print(path+file)
        pdf_pages = convert_from_path(path+file, poppler_path=poppler_path)

        string=''
        for page_enumeration, page in enumerate(pdf_pages, start=1):
            page.save(path+str('images/')+file.split('.')[0]+str(page_enumeration)+'.jpg', "JPEG")
        # image_file_list.append(file)
            im=Image.open(path+str('images/')+file.split('.')[0]+str(page_enumeration)+'.jpg')
            text=pytesseract.image_to_string(im)
            string+=str(text)+'/**/'
        page=string.split('/**/')
        for i in range(len(page)):
            print(page[i])
            print('\n')