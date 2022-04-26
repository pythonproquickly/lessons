import pathlib
import pandas as pd
pd.set_option('display.max_columns', None)
PATH = r"/Users/andy/ws/ctpsws-clients/lessons/src/lessons/drewl"
FILE_TYPE = '*.xlsx'


def getfiles():
    return [filepath for filepath in pathlib.Path(PATH).rglob(FILE_TYPE)]

def load_spreadsheets_to_list():
    excel_file_names = getfiles()
    excel_spreadsheets = []
    for excel_file_name in excel_file_names:
        excel_file = pd.read_excel(excel_file_name, usecols="A:F")
        print(f"processing {excel_file_name}, {excel_file_name.name}")
        excel_spreadsheets.append(excel_file[:-2])
    return excel_spreadsheets


def main():
    spreadsheets = load_spreadsheets_to_list()
    for spreadsheet in spreadsheets:
        print(spreadsheet)
        print()


if __name__ == "__main__":
    main()
