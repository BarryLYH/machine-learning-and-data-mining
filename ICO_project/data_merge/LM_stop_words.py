import re
import pandas as pd
import os

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
import os

def classify(word, clas):
    list = []
    for i in range(len(word)):
        if clas[i]!=0:
            list.append(word[i].lower())
    return list

def process(path):
    aud=cur=dat=gen=genlong=geo=nam=0

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

        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()

            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    results = x.get_text().lower()
                    list = results.split()
                    for part in list:
                        aud += count_word(part, auditor)
                        cur += count_word(part, currency)
                        dat += count_word(part, datesand)
                        gen += count_word(part, generic)
                        genlong +=  count_word(part, genericlong)
                        geo += count_word(part, geographic)
                        nam += count_word(part, names)
    return [aud, cur, dat, gen, genlong, geo, nam]


def count_word(line, list):
    counter = 0
    for word in list:
        if line == word:
            counter += 1
    return counter


if __name__ == '__main__':
    infile = open('/users/barry/Desktop/stop-word/StopWords_Auditor.txt', 'r')
    stops = infile.readlines()
    infile.close()
    auditor = []
    for stop in stops:
        stop =stop.strip('\n')
        auditor.append(stop.lower())

    infile = open('/users/barry/Desktop/stop-word/StopWords_Currencies.txt', 'r')
    stops = infile.readlines()
    infile.close()
    currency = []
    for stop in stops:
        stop = stop.strip('\n')
        currency.append(stop.lower())

    infile = open('/users/barry/Desktop/stop-word/StopWords_DatesandNumbers.txt', 'r')
    stops = infile.readlines()
    infile.close()
    datesand = []
    for stop in stops:
        stop = stop.strip('\n')
        datesand.append(stop.lower())

    infile = open('/users/barry/Desktop/stop-word/StopWords_Generic.txt', 'r')
    stops = infile.readlines()
    infile.close()
    generic = []
    for stop in stops:
        stop = stop.strip('\n')
        generic.append(stop.lower())

    infile = open('/users/barry/Desktop/stop-word/StopWords_GenericLong.txt', 'r')
    stops = infile.readlines()
    infile.close()
    genericlong = []
    for stop in stops:
        stop = stop.strip('\n')
        genericlong.append(stop.lower())

    infile = open('/users/barry/Desktop/stop-word/StopWords_Geographic.txt', 'r')
    stops = infile.readlines()
    infile.close()
    geographic = []
    for stop in stops:
        stop = stop.strip('\n')
        geographic.append(stop.lower())

    infile = open('/users/barry/Desktop/stop-word/StopWords_Names.txt', 'r')
    stops = infile.readlines()
    infile.close()
    names = []
    for stop in stops:
        stop = stop.strip('\n')
        names.append(stop.lower())


    b = pd.read_csv('/users/barry/desktop/LM_stop.csv', encoding = "ISO-8859-1")
    base = b.to_dict(orient="list")

    path = '/users/barry/desktop/whitepapers'
    files = os.listdir(path)

    for i in range(len(b['Name'])):
        for file in files:
            name = file[:-4]
            if b['Name'][i] == name:
                try:
                    pa = '/users/barry/desktop/whitepapers/'+ file
                    aud, cur, dat, gen, genlong, geo, nam = process(pa)

                    base['Auditor'][i] = aud
                    base['Currencies'][i] = cur
                    base['DatasandNumbers'][i] = dat
                    base['Generic'][i] = gen
                    base['GenericLong'][i] = genlong
                    base['Geographic'][i] = geo
                    base['Names'][i] = nam

                    print(aud, cur, dat, gen, genlong, geo, nam)
                    break
                except:
                    break

    ddd = pd.DataFrame(base)
    ddd = ddd[['Name', 'Auditor', 'Currencies', 'DatasandNumbers', 'Generic', 'GenericLong', 'Geographic', 'Names']]
    ddd.to_csv('/users/barry/desktop/wp1.csv')