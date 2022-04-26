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
