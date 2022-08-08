# in an interactive python shell run:
#
# import nltk
# nltk.download()
# https://www.nltk.org/

from loguru import logger
import nltk
from pathlib import Path
import os
import string
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import pdfplumber

PATH = r"/Users/andy/tmp/pdf/"
OUTPUT_PATH = r"/Users/andy/tmp/output/"

LOG_DIR = "./logs/"
logger.remove()


def info_filter(record):
    return record["level"].name == "INFO"


logger.add(f"{LOG_DIR}info.log", filter=info_filter)
error_filter = (
    lambda record: record["level"].name == "ERROR"
    and "traceback" not in record["extra"]
)
logger.add(f"{LOG_DIR}error.log", filter=error_filter)
debug_filter = (
    lambda record: record["level"].name == "DEBUG"
    and "traceback" not in record["extra"]
)
logger.add(f"{LOG_DIR}debug.log", filter=debug_filter)

summary = open(f"{OUTPUT_PATH}summary.csv", "w")  # pipe delimited due to
# embedded commas
summary.write("pdf`file\n")


def remove_special_chars(text):
    text = text.lower()
    for char in string.punctuation + "\n\t ":
        text.replace(char, " ")
    new_text = ""
    valid_chars = string.ascii_lowercase + " "
    for char in text:
        if char in valid_chars:
            new_text += char
    return new_text


def replace_bad_characters(filepath):
    for character in filepath:
        if character in ";:(), '\"":
            filepath = filepath.replace(character, "_")
    return filepath


def remove_stop_words(tokens):
    stop_words = set(stopwords.words("english"))
    return [w for w in tokens if w.lower() not in stop_words]


def tokenize_it(text):
    document = nltk.tokenize.word_tokenize(text)
    return document


def lemmatize_text(tokens):
    lemmatize = WordNetLemmatizer()
    lemmatized_words = []
    for word in tokens:
        root_word = lemmatize.lemmatize(word)
        lemmatized_words.append(root_word)
    return ' '.join(lemmatized_words)


def extract_pdf_information(pdf_path):
    contents = ""
    try:
        with pdfplumber.open(pdf_path) as f:
            for page in range(len(f.pages)):
                this_page = f.pages[page]
                try:
                    new_contents = this_page.extract_text()
                except:  # refine
                    logger.error(
                        f"text extract failed; page {page} of {pdf_path} ignored"
                    )
                    continue
                contents = contents + new_contents
    except:
        logger.error(f"fatal pdf error for {pdf_path} ignored")
        return ""
    return contents


def analyze_content(pdf_path, contents):
    contents = remove_special_chars(contents)
    contents = contents.strip()
    if len(contents) == 0:
        logger.error(f"Nothing to tokenize: {pdf_path}")
        return ""
    contents = tokenize_it(contents)
    contents = remove_stop_words(contents)
    contents = lemmatize_text(contents)
    return contents


def write_files(pdf_path, contents, sentiments):
    filedir = str(Path(pdf_path).resolve().parent)
    filedir = filedir.replace(PATH, OUTPUT_PATH)
    filedir = replace_bad_characters(filedir)
    try:
        os.system(f"mkdir -p {filedir}")
    except FileExistsError:
        pass
    new_file = str(pdf_path).split("/")
    new_file = new_file[-1][:-3] + "txt"
    new_file = str(pdf_path)[: str(pdf_path).rfind("/")] + "/" + new_file
    new_file = new_file.replace(PATH, OUTPUT_PATH)
    new_file = replace_bad_characters(new_file)
    try:
        with open(new_file, "w") as f:
            f.write(contents)
            logger.info(f"Wrote {new_file}")
    except FileNotFoundError:
        logger.error(f"Can't find file {pdf_path}")
    summary.write(f"{pdf_path} ` {sentiments}\n")


def getfiles():
    paths = []
    for filepath in Path(PATH).rglob("*.pdf"):
        paths.append(filepath)
    return paths


def process_text():
    logger.info("START")
    paths = getfiles()
    for filepath in paths:
        logger.info(f"Attempting to convert {filepath}")
        contents = extract_pdf_information(filepath)
        contents = analyze_content(filepath, contents)
        sentiments = SentimentIntensityAnalyzer().polarity_scores(contents)
        write_files(filepath, contents, sentiments)

    logger.info("END")


def generate_summary_report():
    summary = pd.read_csv(f"{OUTPUT_PATH}summary.csv", delimiter="`")
    # df to play with!
    print(summary.to_string())
