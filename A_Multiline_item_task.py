import os
import re
import pdfplumber
import psycopg2
import pandas as pd

#Connection for database............................
pd_data = psycopg2.connect(host="localhost",database="postgres",user="postgres",password="ADMIN",port="5432")
cur= pd_data.cursor()

# table = '''create table multi_task (ItemName varchar(150), ItemCode varchar(15), HSN varchar(10), Amount varchar(12)) '''
# cur.execute(table)
# pd_data.commit()


for file in os.listdir(r"D:\BACKUP\E DRIVE\sequel_task\Ayushman\Ayushman"):
    # print(file)
    file = file.lower()

    if file.endswith('.pdf'):
        # print(file)
        print('=====================================================*NEW PDF*==============')

        with pdfplumber.open(r"D:\BACKUP\E DRIVE\sequel_task\Ayushman\Ayushman\\"+file) as pdf:
            text_all= ''
            pages = pdf.pages
            for page in pages:
                text = page.extract_text()
                text_all += text
            # print(text_all)

        # new_patch = re.search(r'(?s)Amount.*?\*\s[A-Za-z]+',text_all).group()
        # new_patch = re.sub(r'(?s)Amount.*?\%\s\%|\*\sFree','',new_patch)
        # # print(new_patch)

        # single_line = re.findall(r'[0-9]+.*?[0-9.,]+\s+[0-9\,\.]+\s+.*?\n',new_patch) 
        # # print(single_line)

        # # print('==============================================================================')

        # splitted_data = new_patch.split('\n')
        # # print(splitted_data)

        # for i in range(len(single_line)):
        #     # print(single_line[i])
        #     remaining_text = ''
        #     for j in range(len(splitted_data)):
        #         # print(splitted_data[j])
        #         if single_line[i].replace('\n','') == splitted_data[j]:
        #             # print('Its a Match')
        #             try:
        #                 for x in range(1,11):
        #                     if splitted_data[j+x]+'\n' in single_line:
        #                         break
        #                     else:
        #                         remaining_text = remaining_text+' '+splitted_data[j+x]
        #             except:
        #                 pass            

        #     # print(remaining_text)
        #     new_text = re.sub(r'\s+Tablets|\s+Capsules','',remaining_text)
        #     print(new_text)

        #     lines = single_line[i].split()
        #     # print(lines)
            
        #     new_lines = ' '.join(lines)
        #     # print(new_lines)

        #     description = lines[2:-9]
        #     description = ' '.join(description)
        #     description = re.sub(r'\d{8}|\d{4}','',description)
        #     # print(description)

        #     # # #Description Full--------------------------------------------------------------------------------------------------
        #     full_description = description + new_text
        #     print('Description:--',full_description)

        #     # # #Item Code---------------------------------------------------------------------------------------------------------
        #     item_code = lines[1]
        #     print('Item_Code:--',item_code)

        #     # # #HSN----------------------------------------------------------------------------------------------------------------
        #     hsn = re.findall(r'\s+\d{8}|\s\d{4}\s|\d{6}',new_lines)
        #     final_hsn = ' '.join(hsn)
        #     print('HSN:--',final_hsn)

        #     # # #Amount--------------------------------------------------------------------------------------------------------------
        #     amt = lines[-1]
        #     print('Amount : ',amt)  
        #     print('--------------------------------------------------------------------------')
        # print('**********************************************************************************************************************')


        # Inserting all values into database..........................................................
        # all_data = (full_description, item_code, final_hsn, amt)
        # insert = '''insert into multi_task( ItemName, ItemCode, HSN, Amount) values (%s,%s,%s,%s)'''
        # cur.execute(insert,all_data)
        # pd_data.commit()