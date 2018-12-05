import os
import pandas as pd


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

    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()

            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(r'/Users/Barry/Desktop/wp_txt/'+file+'.txt','a') as f:
                        results = x.get_text()
                        #dprint(results)
                        f.write(results + '\n')
        return file+' done'


if __name__ == '__main__':

    path = '/users/barry/desktop/whitepapers'
    files = os.listdir(path)

    counter = 0
    for file in files:
        counter += 1
        print(counter, file)
        path_wp = path + '/'+ file
        try:
            parse(path_wp, file[:-4])
        except:
            continue

