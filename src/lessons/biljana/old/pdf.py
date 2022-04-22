# pip install pypdf2

from PyPDF2 import PdfFileReader
from pathlib import Path
import os

# PATH is input dir. Program recurses on this
# OUTPUT_PATH mirrored dir structure of PATH

PATH = r"/home/andy/"  # use raw string in case it needs to run on windows
OUTPUT_PATH = r"/home/andy/tmp/"  # due to M$ non standard dir delimiter


def replace_bad_characters(filepath):
    for character in filepath:
        if character in ";:(), '\"":
            filepath = filepath.replace(character, "_")
    return filepath


def extract_information(pdf_path):
    doc = []
    with open(pdf_path, 'rb') as f:
        try:
            pdf = PdfFileReader(f)
        except:
            print(f"error opening {pdf_path}; can't read")
            return
        try:
            num_pages = pdf.getNumPages()
        except:
            print(f"Can't read {pdf_path}: possibly encrypted")
            return
        for page in range(num_pages):
            this_page = pdf.getPage(page)
            try:
                doc.append(this_page.extractText())
            except:
                print(
                    f"error reading pdf: {pdf_path} name too long or file malformed")
                return
    filedir = str(Path(pdf_path).resolve().parent)
    filedir = filedir.replace(PATH, OUTPUT_PATH)
    filedir = replace_bad_characters(filedir)
    try:
        os.system(f"mkdir -p {filedir}")
    except FileExistsError:
        pass
    new_pdf_path = str(pdf_path)[:-3] + "txt"
    new_pdf_path = new_pdf_path.replace(PATH, OUTPUT_PATH)
    new_pdf_path = replace_bad_characters(new_pdf_path)
    try:
        with open(new_pdf_path, 'w') as f:
            f.writelines(doc)
    except FileNotFoundError:
        print(f"can't find file {pdf_path}")


def getfiles():
    paths = []
    for filepath in Path(PATH).rglob('*.pdf'):
        paths.append(filepath)
    return paths


if __name__ == '__main__':
    paths = getfiles()
    for filepath in paths:
        extract_information(filepath)
