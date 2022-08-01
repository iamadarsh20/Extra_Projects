import pdfplumber 
import re


text_all= ''
with pdfplumber.open(r"E:\sequel_task\New folder\New folder\mallareddy\Akna PLPO1520.pdf") as pdf:
    pages = pdf.pages
    for page in pages:
        text = page.extract_text()
        text_all += text

# print(text_all)
data = re.search(r'(?s)Rate\sAmt.*Prepared\sby',text_all).group()
data_new = re.sub(r'(?s)Prepared\sby.*?Thanking\syou,','',data)
# print(data_new)
line_items = re.findall(r'[0-9]+.?[0-9.,]+\s+[0-9.,]+\s+[0-9]+\s+[0-9]+.\n',data_new)
#print(line_items)


splitted_data = data_new.split('\n')
print(splitted_data)
for l in range(len(line_items)):
    # print(line_items[l])
    remaining_data = ''
    for j in range(len(splitted_data)):
        if line_items[l].replace('\n','') == splitted_data[j]:
            # print(l,'yes')
            for k in range(1,11):
                if splitted_data[j+k]+'\n' in line_items:
                    break
                else:
                    remaining_data = remaining_data+' '+splitted_data[j+k]
    
    #print(remaining_data)
    remaining_data = re.sub('\d+\s+Numbers|\d+\s+tab|\d+\s+bottle|\d+\s+syringe','',remaining_data)
    remaining_data= re.sub('\s+',' ',remaining_data)
    print(remaining_data)
    print('-----------')

    # line = line_items[l].split()
    # print(line)