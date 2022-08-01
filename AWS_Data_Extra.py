import re
import base64
##import datetime
from datetime import datetime
import pdfplumber
import pandas as pd
from datetime import datetime
import psycopg2
import os, shutil
from base64 import b64decode
#Developed Functions
from pdf_parser import data_extractor_numbers,data_extractor_alphanumeric,data_extractor_string
 
from aws_lib_.aws_ocr_main import main_call
import sys

sys.path.append(r"pip")
data_dict = {}
l = ['(', ')', '.', '/', '-']


def Trigger(input_path):

            output_path=r"E:\sequel_training_content\aws_extracted_text1"
            text1=''
            os.chdir(output_path)
            main_call(input_path)
            print('AWS WORKING')
            
            text_all=''
            for file in os.listdir(output_path):
                if file.endswith('text.txt'):
                    file_path= f'{output_path}\\{file}'
                    with open(file_path,encoding='utf-8') as f:
                        lines=f.read()
                        # print(lines)
                        text1=text1+'\n-----------------------------------New page-------------------------------------\n'+lines

            for file in os.listdir(r"E:\sequel_training_content\aws_extracted_text1"):
                # os.remove(r"C:\Users\prati\OneDrive\Desktop\TATA POWER\Desktop\PTC\PTC TEXt\\"+file)

                return text1
        
def main_trigger(input_pdf):

    text = ''
        
    text = Trigger(input_pdf)
    text = ' '.join(text.split('\n'))
    # print(text)

    data_extractor_alphanumeric(text,'GST Registration Number',1,data_dict,'GST Registration Type','Gstin',l,'\d+[a-zA-Z]+[0-9]+[a-zA-Z]+[0-9]+[a-zA-Z]+',0)
    # data_extractor_alphanumerpdf_parser.pyic(text,'Customer Code',1,data_dict,'Customer Name','code',l,'','')
    # data_extractor_alphanumeric(text,'IRN No',1,data_dict,'Billing Address','Invoice_n',l,'\S+',1)
    print(data_dict)


for file in os.listdir(r"E:\sequel_training_content\Spun Micro\Spun Micro"):
    main_trigger(r"E:\sequel_training_content\Spun Micro\Spun Micro\\"+file)