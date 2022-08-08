import lang_lib

if __name__ == "__main__":
    lang_lib.load_text()
    lang_lib.summary.close()
    lang_lib.generate_summary_report()
