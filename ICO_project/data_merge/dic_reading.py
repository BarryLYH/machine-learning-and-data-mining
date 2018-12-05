import pandas as pd

def classify(word, clas):
    list = []
    for i in range(len(word)):
        if clas[i]!=0:
            list.append(word[i])
    return list

data = pd.read_csv('/users/barry/desktop/LMDic.csv')

word = data['Word']
negative = classify(word,data['Negative'])
positive = classify(word,data['Positive'])
uncertainty = classify(word,data['Uncertainty'])
litigious = classify(word,data['Litigious'])
constraining = classify(word,data['Constraining'])
superfluous = classify(word,data['Superfluous'])
interesting = classify(word,data['Interesting'])
