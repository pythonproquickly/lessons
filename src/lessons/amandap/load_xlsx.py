"""
Finds all spreadsheets in PATH
Loads each into a last of dataframes, one per spreadsheet
You can then iterate around that list and process the data

NOTES:
    This doesnt have to load all the spredsheets at once but
    if it can without running out of memory it will perform better
    Be sure to change PATH to the full path where the spreadsheets are located

"""
import pathlib
import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
PATH = r"/Users/andy/data/amandap"
FILE_TYPE = "*.xlsx"


def getfiles():
    return [filepath for filepath in pathlib.Path(PATH).rglob(FILE_TYPE)]


def load_spreadsheets_to_list():
    excel_file_names = getfiles()
    first = True
    for excel_file_name in excel_file_names:
        excel_file = (
            pd.read_excel(
                excel_file_name, header=2, sheet_name="OVI Calculations", index_col=None
            ),
        )
        # usecols="B")
        print(f"processing {excel_file_name}")
        print(excel_file)
        excel_file.rename(
            columns={
                "Unnamed: 1": "CI",
            },
            inplace=True,
        )
        excel_file["FileName"] = excel_file_name.name
        excel_file["Sample"] = excel_file_name.name[6:9]
        excel_file["B#"] = excel_file_name.name[11:13]
        excel_file["Points"] = excel_file_name.name[14]
        excel_file.insert(loc=0, column="num", value=np.arange(len(excel_file)))
        if first:
            first = False
            excel_spreadsheets = excel_file.copy()
        else:
            excel_spreadsheets = pd.concat([excel_spreadsheets, excel_file])
    return excel_spreadsheets.sort_values(
        by=["Sample", "B#", "Points"], ascending=False
    )


def main():
    spreadsheets = load_spreadsheets_to_list()
    spreadsheets.to_excel("all.xlsx", index=False)


if __name__ == "__main__":
    main()
