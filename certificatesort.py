import PyPDF2
import os
import mysql.connector as mys

# Run this file to sort all the certificates into the database with the corresponding unique student number depending on the name in the certificate.

with open('./static/File_list.txt') as f:
    L = f.read().split('\n')
    L.pop()
    file_list = []  
    database_list = []

    for i in L:
        database_list.append("Certificates/" + i)
        file_list.append("./static/Certificates/" + i)

    print(database_list)

txt_file_path = './static/output.txt'  

for pdf_file_path in file_list:
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        extracted_text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()

        with open(txt_file_path, 'a', encoding='utf-8') as txt_file:  
            txt_file.write(extracted_text)
            txt_file.write('\n')

print(f'Text extracted and saved to {txt_file_path}')


with open(txt_file_path) as f1, open('./static/modified_output.txt', 'a') as f2:
    L1 = f1.readlines()  

    for i in L1:
        if i.startswith('P r i n c i p a l'):
            parts = i.split('P r i n c i p a l')
            for x in parts:
                end = x.split('Certificate\n')
                f2.write(end[0])
                f2.write('\n')
        elif i.startswith('Principal'):
            parts = i.split('Principal')
            for x in parts:
                end = x.split('Certificate\n')
                f2.write(end[0])
                f2.write('\n')
        elif i.endswith('Certificate\n'):
            na = i.split('Certificate\n')
            f2.write(na[0])
            f2.write('\n')


with open('./static/modified_output.txt', 'r') as f:
    lines = f.readlines()
non_blank_lines = [line for line in lines if line.strip()]
with open('./static/modified_output.txt', 'w') as f:
    f.writelines(non_blank_lines)


Names = []

with open('./static/modified_output.txt', 'r') as f:
    lines = f.readlines()
    for i in lines:
        Names.append(i[:-1])

db = mys.connect(host='localhost', user='root', password='guavas4lyfe', database='hackathon', charset='utf8')
cur = db.cursor()

cur.execute("delete from files")
db.commit()

for i in range(len(Names)):
    query = "INSERT INTO files (Name, filename) VALUES (%s, %s)"
    values = (Names[i], database_list[i])
    cur.execute(query, values)
    db.commit()


if os.path.exists('./static/modified_output.txt'):
    os.remove('./static/modified_output.txt')

if os.path.exists('./static/output.txt'):
    os.remove('./static/output.txt')