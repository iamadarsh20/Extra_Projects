import pdfplumber
import re

with pdfplumber.open(r"E:\sequel_task\PO_0.1.07.21_DRUGS.pdf") as pdf:
    pages = pdf.pages
    text_all = ''
    for page in pages:
        text  = page.extract_text()
        text_all += text
    # print(text_all)

    data = re.search(r'(?s)Net.*Total\sAmt',text_all).group()
    # print(data)

    line_items = re.findall(r'\d+.*?[0-9.,]+\s[0-9.,]+\s+[0-9.,]+\s+[0-9.,]+\n',data)
    print(line_items)

    for line in line_items:
        print(line)
        