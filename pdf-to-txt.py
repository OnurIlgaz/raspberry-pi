import PyPDF2

with open('in.pdf', 'rb') as file:
    pdf = PyPDF2.PdfReader(file)
    with open('in.txt', 'w') as text_file:
        for page in pdf.pages:
            text = page.extract_text()
            text_file.write(text)