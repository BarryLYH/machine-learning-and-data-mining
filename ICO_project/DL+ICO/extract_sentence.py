import nltk
import re
import os
from nltk.tokenize import WordPunctTokenizer

path ='/users/barry/desktop/wp_txt'
files =os.listdir(path)

statistic = open('/users/barry/desktop/words_sqes.txt', 'a+')
total = 0
c=0
for file in files:
    word_num = 0
    c+=1
    print(c)
    print(file)
    if file == '.DS_Store': continue

    infile = open('/users/barry/desktop/wp_txt/'+file, 'r', encoding='utf-8')
    content = infile.read()
    infile.close()

   # outfile = open('/users/barry/desktop/wp_txt_sentence/'+file, 'a+')

    content = content.lower().replace('\n', ' ').strip()
    content = re.sub(r'\s+', ' ', content)
    #print(content)

    pattern = r"""(?x)                   # set flag to allow verbose regexps
                  (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A.
                  |\d+(?:\.\d+)?%?       # numbers, incl. currency and percentages
                  |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe
                  |\.\.\.                # ellipsis
                  |(?:[.,;"'?():-_`])    # special characters with meanings
                """

    #print(num)

    sen_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sen_tokenizer.tokenize(content)

    counter = 0
    for sentence in sentences:
        num = len(sentence.split())
        word_num  = word_num + num
        counter += 1
            #print(counter)
            #print(sentence)
          #  outfile.write(sentence)
          #  outfile.write('\n')
          #  outfile.flush()
    #outfile.close()
    #print(counter)
    total += counter
    statistic.write(file[:-4]+' '+str(word_num)+' '+str(counter))
    statistic.write('\n')
    statistic.flush()

statistic.close()

print(total)