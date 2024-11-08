import os
import PyPDF2

path = os.getcwd()
folder_path = os.path.join(path, 'data')

# 폴더가 없으면 생성
if not os.path.exists(folder_path):
    os.makedirs(folder_path, exist_ok=True)

file_list = os.listdir(folder_path)

if file_list == 2:
    # PDF 파일을 읽음
    pdf1 = PyPDF2.PdfReader(open(os.path.join(folder_path, file_list[0]), 'rb'))
    pdf2 = PyPDF2.PdfReader(open(os.path.join(folder_path, file_list[1]), 'rb'))

    # 새 PDF 파일 생성
    pdf_writer = PyPDF2.PdfWriter()

    # 각 페이지를 번갈아가며 추가
    num_pages = max(len(pdf1.pages), len(pdf2.pages))

    for i in range(num_pages):
        if i < len(pdf1.pages):
            pdf_writer.add_page(pdf1.pages[i])
        if i < len(pdf2.pages):
            pdf_writer.add_page(pdf2.pages[i])

    # 결과를 새 파일로 저장
    with open(os.path.join(path, 'merged.pdf'), 'wb') as out_file:
        pdf_writer.write(out_file)

