from multiprocessing.spawn import prepare
import os
import pdfplumber
import re
import pandas as pd
import psycopg2


with pdfplumber.open(r"E:\sequel_task\PO_0.1.07.21_DRUGS.pdf") as pdf:
    pages = pdf.pages
    data = ""
    for page in pages:
        text = page.extract_text()
        data += text
        # print(data)


po_number = re.search(r'PO\s+No.\s+\:\s+\d+\/[A-Z0-9]+\/[A-Z]+\/[0-9]+',data).group()
# po_number = re.sub('PO No. : ','',po_number)
print(po_number)

gis_number = re.search(r'GSTIN+\s+No+.\s+\:\s+[0-9]+[A-Z0-9]+',data).group()
# gis_number = re.sub('PO No. : ','',gis_number)
print(gis_number)


total = re.search(r'Total\s+Amt\s+\:\s+[0-9.,]+',data).group()
# gis_number = re.sub('PO No. : ','',gis_number)
print(total)


date = re.search(r'Delivery\s+Date\s+\:\s+[0-9]+\/+[0-9]+\/+[0-9]+',data).group()
# gis_number = re.sub('PO No. : ','',gis_number)
print(date)


prepared = re.search(r'Prepared\s+By\s\:\s+[A-Z]+',data).group()
# gis_number = re.sub('PO No. : ','',gis_number)
print(prepared)


table =re.search(r'(?s)Sr\s+No\s+.*Rupees',data).group()
print(table)


item =re.findall(r'\d.*',table)
print(item)

mrp2=[]
dis2=[]

# for i in item:
#     mrp = i.split()
#     mrp2.append(mrp[-10]) 
#     s= i.split()[1:-10]
#     dis = " ".join(s)
#     dis2.append(dis)
#     print(dis,":",mrp2)

    # discription = re.search(r'[A-Z]+\s+[A-Z]+',i).group()
    # mrp = re.search(r'[0-9]+\.+[0-9]+',i).group()
    # print(discription,":",mrp)


# edata = {'discription':dis2,'MRP': mrp2}
# df = pd.DataFrame(edata)
# df.to_excel("./output.xlsx", sheet_name='DATA', index=False)

con = psycopg2.connect(host="localhost" , database="postgres" , user="postgres", password="admin", port="5432")

cur = con.cursor()
# q= '''create table details (Description varchar(100) , MRP int )'''
# cur.execute(q)
# con.commit()

for i in item:
    mrp = i.split()
    mrp2=mrp[-10]
    s= i.split()[1:-10]
    dis = " ".join(s)
   
    d=(dis,mrp2)
    q1='''insert into details (description,MRP) values(%s,%s)'''
    cur.execute(q1,d)
    con.commit()