"""
Finds all spreadsheets in PATH
Loads each into a last of dataframes, one per spreadsheet
You can then iterate around that list and process the data

NOTES:
    I didnt rename all the columns yet
    This doesnt have to load all the spredsheets at once but
    if it can without running out of memory it will perform better
    Be sure to change PATH to the full path where the spreadsheets are located

"""
import pathlib
import pandas as pd

PATH = r"/Users/andy/data/amandap"
FILE_TYPE = '*.xlsx'


def getfiles():
    return [filepath for filepath in pathlib.Path(PATH).rglob(FILE_TYPE)]
# OVI Calculations

def load_spreadsheets_to_list():
    excel_file_names = getfiles()
    excel_spreadsheets = []
    for excel_file_name in excel_file_names:
        excel_file = pd.read_excel(excel_file_name,
                                   header=2,
                                   sheet_name='OVI Calculations',
                                   index_col=None,
                                   usecols="B")
        print(f"processing {excel_file_name}")
        excel_file.drop(excel_file.filter(regex="Unname"), axis=1,
                        inplace=True)
        excel_file.dropna(subset=["Session"], inplace=True)
        excel_file['Session'] = excel_file['Session'].astype(int)
        excel_file.set_index('Session')
        excel_file.rename(columns={
            'bx1': 'Escape_Rate_bx1',
            'bx1 SR+': 'Escape_Rate_bx1_SR+',
            # etc
        }, inplace=True)
        excel_file['FileName'] = excel_file_name.name
        excel_spreadsheets.append(excel_file)
    return excel_spreadsheets


def main():
    spreadsheets = load_spreadsheets_to_list()
    print(spreadsheets)


if __name__ == "__main__":
    main()
