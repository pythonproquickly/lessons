import sys
import csv

import pandas as pd

ANALYSIS_FILE = "/Users/andy/ws/ctpsws-clients/lessons/src/lessons/samuelo/data/log_summary.csv"

def generate_report():
    la = pd.read_csv(ANALYSIS_FILE, sep='\t', engine='python', quoting=csv.QUOTE_NONE)
    la.head()
    
    """la_result = la.groupby(by=("time[:10"))["host", "agent"].count()
    la_result.head()"""
 
def main():
    generate_report()
    


if __name__ == "__main__":
    main()