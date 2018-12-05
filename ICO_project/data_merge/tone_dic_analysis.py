import re
import pandas as pd
import os

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
import os

def countword(sentence, words):
    counter = 0
    for i in words:
        counter += sentence.count(i)
    return counter

def process(path):
    re = ex = sh = 0

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

        allwords = ''
        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()

            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    results = x.get_text().lower()
                    list = results.split()
                    for part in list:
                        allwords = allwords + ' ' + part
        re = countword(allwords, ref)
        ex = countword(allwords, exe)
        sh = countword(allwords, sha)
    return [re,ex,sh]


if __name__ == '__main__':

    infile = open('/users/barry/desktop/reference.txt', 'r')
    content1 = infile.readlines()
    infile.close()

    infile = open('/users/barry/desktop/exe.txt', 'r')
    content2 = infile.readlines()
    infile.close()

    infile = open('/users/barry/desktop/share.txt', 'r')
    content3 = infile.readlines()
    infile.close()

    ref = []
    for part in content1:
        ref.append(part.strip('\n'))

    exe = []
    for part in content2:
        exe.append(part.strip('\n'))

    sha = []
    for part in content3:
        sha.append(part.strip('\n'))


    b = pd.read_csv('/users/barry/desktop/tone.csv', encoding = "ISO-8859-1")
    base = b.to_dict(orient="list")

    path = '/users/barry/desktop/whitepapers'
    files = os.listdir(path)

    for i in range(len(b['Name'])):
        for file in files:
            name = file[:-4]
            if b['Name'][i] == name:
                try:
                    pa = '/users/barry/desktop/whitepapers/'+ file
                    re, ex, sh= process(pa)
                    base['Reference'][i] = re
                    base['Extreme'][i] = ex
                    base['Shareholder'][i] = sh
                    print(i, name, re, ex, sh)
                    break
                except:
                    break

    ddd = pd.DataFrame(base)
    ddd.to_csv('/users/barry/desktop/wp.csv')