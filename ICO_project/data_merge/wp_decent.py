import re
import pandas as pd
import os

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def parse(path,file):
    fp = open(path, 'rb')
    praser = PDFParser(fp)
    doc = PDFDocument()
    praser.set_document(doc)
    doc.set_parser(praser)

    doc.initialize()
    fp.close()
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        counter_de = 0
        counter_th = 0
        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()

            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    results = x.get_text().lower()
                    counter_de += results.count('decentralized')
                    counter_th += results.count('third-party')

        return [counter_de, counter_th]


if __name__ == '__main__':

    base = {'Name':[], 'Decentralized':[]}

    path = '/users/barry/desktop/wp_txt_sentence'
    files = os.listdir(path)

    counter = 0
    for file in files:
        if file == '.DS_Store': continue
        name = file[:-4]
        base['Name'].append(name)
        counter += 1
        print(counter, file)
        infile = open(path+'/'+file, 'r', encoding='utf-8')
        lines = infile.readlines()
        infile.close()
        counter_d = 0
        for line in lines:
            counter_d += line.count('decentralized')
        base['Decentralized'].append(counter_d)

    ddd = pd.DataFrame(base)
    ddd.to_csv('/users/barry/desktop/wp_decentralized_2.csv')

