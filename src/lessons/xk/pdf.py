# pip install pypdf2

from PyPDF2 import PdfFileReader


def extract_information(pdf_path):
    doc = []
    with open(pdf_path, "rb") as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        for page in range(pdf.getNumPages()):
            this_page = pdf.getPage(page)
            doc.append(this_page.extractText())

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    for line in doc:
        print(line)
    return information


if __name__ == "__main__":
    paths = [
        "/home/andy/ws/ctpsws/lessons/wm2.pdf",
    ]
    for path in paths:
        extract_information(path)
