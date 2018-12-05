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
    nega = posi = unce = liti = cons = supe = inte = master = total = 0

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
                    total += len(results)
                    for part in list:
                        if count_word(part, word) > 0 :
                            master += 1
                        if count_word(part, negative ):
                            nega += 1
                        if count_word(part, positive):
                            posi += 1
                        if count_word(part, uncertainty):
                            unce += 1
                        if count_word(part, litigious):
                            liti += 1
                        if count_word(part, constraining):
                            cons += 1
                        if count_word(part, superfluous):
                            supe += 1
                        if count_word(part, interesting):
                            inte += 1
    return [master, total, nega, posi, unce, liti, cons, supe, inte]


def count_word(line, list):
    counter = 0
    for word in list:
        counter += line.count(word)
        if counter >0:
            return 1
    return counter


if __name__ == '__main__':
    data = pd.read_csv('/users/barry/desktop/word.csv')

    w = data.to_dict(orient="list")
    word = []
    for part in w['Words']:
        try:
            word.append(part.lower())
        except:
            print(part)

    data = pd.read_csv('/users/barry/desktop/LMDic.csv')

    words = data['Word']
    negative = classify(words, data['Negative'])
    positive = classify(words, data['Positive'])
    uncertainty = classify(words, data['Uncertainty'])
    litigious = classify(words, data['Litigious'])
    constraining = classify(words, data['Constraining'])
    superfluous = classify(words, data['Superfluous'])
    interesting = classify(words, data['Interesting'])


    b = pd.read_csv('/users/barry/desktop/LM_master.csv', encoding = "ISO-8859-1")
    base = b.to_dict(orient="list")

    path = '/users/barry/desktop/whitepapers'
    files = os.listdir(path)

    for i in range(len(b['Name'])):
        for file in files:
            name = file[:-4]
            if b['Name'][i] == name:
                try:
                    pa = '/users/barry/desktop/whitepapers/'+ file
                    master,total, ne, po, un, li, co, su, inte= process(pa)
                    base['Master'][i] = master
                    base['Total'][i] = total
                    base['Negative'][i] = ne
                    base['Positive'][i] = po
                    base['Uncertainty'][i] = un
                    base['Litigious'][i] = li
                    base['Constraining'][i] = co
                    base['Superfluous'][i] = su
                    base['Interesting'][i] = inte
                    print(name, master, total, ne, po, un, li, co, su, inte)
                    break
                except:
                    break

    ddd = pd.DataFrame(base)
    ddd = ddd[['Name', 'Master', "Total",'Negative', 'Positive', 'Uncertainty', 'Litigious', 'Constraining', 'Superfluous', 'Interesting']]
    ddd.to_csv('/users/barry/desktop/wp.csv')