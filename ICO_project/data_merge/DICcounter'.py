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
    nega = posi = unce = liti = cons = supe = inte = 0

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
                    nega += count_word(results, negative)
                    posi += count_word(results, positive)
                    unce += count_word(results, uncertainty)
                    liti += count_word(results, litigious)
                    cons += count_word(results, constraining)
                    supe += count_word(results, superfluous)
                    inte += count_word(results, interesting)
    return [nega, posi, unce, liti, cons, supe, inte]


def count_word(line, list):
    counter = 0
    for word in list:
        counter += line.count(word)
    return counter


if __name__ == '__main__':
    data = pd.read_csv('/users/barry/desktop/LMDic.csv')

    word = data['Word']
    negative = classify(word, data['Negative'])
    positive = classify(word, data['Positive'])
    uncertainty = classify(word, data['Uncertainty'])
    litigious = classify(word, data['Litigious'])
    constraining = classify(word, data['Constraining'])
    superfluous = classify(word, data['Superfluous'])
    interesting = classify(word, data['Interesting'])

    b = pd.read_csv('/users/barry/desktop/LM_dictionary.csv', encoding = "ISO-8859-1")
    base = b.to_dict(orient="list")

    path = '/users/barry/desktop/whitepapers'
    files = os.listdir(path)

    for i in range(len(b['Name'])):
        for file in files:
            name = file[:-4]
            if b['Name'][i] == name:
                try:
                    pa = '/users/barry/desktop/whitepapers/'+ file
                    ne, po, un, li, co, su, inte = process(pa)
                    base['Negative'][i] = ne
                    base['Positive'][i] = po
                    base['Uncertainty'][i] = un
                    base['Litigious'][i] = li
                    base['Constraining'][i] = co
                    base['Superfluous'][i] = su
                    base['Interesting'][i] = inte
                    print(name, ne, po, un, li, co, su, inte)
                    break
                except:
                    break

    ddd = pd.DataFrame(base)
    ddd = ddd[['Name', 'Negative', 'Positive', 'Uncertainty', 'Litigious', 'Constraining', 'Superfluous', 'Interesting']]
    ddd.to_csv('/users/barry/desktop/wp.csv')