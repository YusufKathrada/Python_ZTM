import os

import PyPDF2
import sys


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        pdf_name = os.path.basename(pdf)
        print(f"Successfully merged {pdf_name}")
        merger.append(pdf)
    print("------------COMPLETED------------")
    merger.write('merged.pdf')

# takes in command line arguments of the pdf file names that you want to merge
def main():
    inputs = sys.argv[1:]
    pdf_merger(inputs)


if __name__ == "__main__":
    main()

