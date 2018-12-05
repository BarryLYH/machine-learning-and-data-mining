import pandas as pd
import os
import shutil
import random

num_120 = [1, 28, 27, 16, 48]
num_500 = [5, 118, 114, 62, 201]

path_wp = '/users/barry/desktop/whitepapers'
files =os.listdir(path_wp)

'''
# 100mil sampling method
b = pd.read_csv('/users/barry/desktop/wp_classified/100mil.csv', encoding = "ISO-8859-1")
length = len(b['Name'])
i = 0
while i < num_120[0]:
    selected = random.randint(1, length) - 1
    if b['sampled'][selected] == 0:
        for file in files:
            if file[:-4] == b['Name'][selected]:
                srcfile = os.path.join(path_wp, file)
                path = '/users/barry/desktop/wp_sample/100mil'
                targetfile = os.path.join(path, file)
                shutil.copyfile(srcfile, targetfile)
                break
        b['sampled'][selected] = 1
        i += 1
b.to_csv('/users/barry/desktop/wp_classified/100mil.csv')
'''

# 10mil sampling method
b = pd.read_csv('/users/barry/desktop/wp_classified/10mil.csv', encoding = "ISO-8859-1")
length = len(b['Name'])
i = 0
while i < num_120[1]:
    selected = random.randint(1, length) - 1
    if b['sampled'][selected] == 0:
        for file in files:
            if file[:-4] == b['Name'][selected]:
                srcfile = os.path.join(path_wp, file)
                path = '/users/barry/desktop/wp_sample/10mil'
                targetfile = os.path.join(path, file)
                shutil.copyfile(srcfile, targetfile)
                break
        b['sampled'][selected] = 1
        i += 1
b.to_csv('/users/barry/desktop/wp_classified/10mil.csv')

# 1mil sampling method
b = pd.read_csv('/users/barry/desktop/wp_classified/1mil.csv', encoding = "ISO-8859-1")
length = len(b['Name'])
i = 0
while i < num_120[2]:
    selected = random.randint(1, length) - 1
    if b['sampled'][selected] == 0:
        for file in files:
            if file[:-4] == b['Name'][selected]:
                srcfile = os.path.join(path_wp, file)
                path = '/users/barry/desktop/wp_sample/1mil'
                targetfile = os.path.join(path, file)
                shutil.copyfile(srcfile, targetfile)
                break
        b['sampled'][selected] = 1
        i += 1
b.to_csv('/users/barry/desktop/wp_classified/1mil.csv')

# nonmil sampling method
b = pd.read_csv('/users/barry/desktop/wp_classified/nonmil.csv', encoding = "ISO-8859-1")
length = len(b['Name'])
i = 0
while i < num_120[3]:
    selected = random.randint(1, length) - 1
    if b['sampled'][selected] == 0:
        for file in files:
            if file[:-4] == b['Name'][selected]:
                srcfile = os.path.join(path_wp, file)
                path = '/users/barry/desktop/wp_sample/nonmil'
                targetfile = os.path.join(path, file)
                shutil.copyfile(srcfile, targetfile)
                break
        b['sampled'][selected] = 1
        i += 1
b.to_csv('/users/barry/desktop/wp_classified/nonmil.csv')

# nondata sampling method
b = pd.read_csv('/users/barry/desktop/wp_classified/nondata.csv', encoding = "ISO-8859-1")
length = len(b['Name'])
i = 0
while i < num_120[4]:
    selected = random.randint(1, length) - 1
    if b['sampled'][selected] == 0:
        for file in files:
            if file[:-4] == b['Name'][selected]:
                srcfile = os.path.join(path_wp, file)
                path = '/users/barry/desktop/wp_sample/nondata'
                targetfile = os.path.join(path, file)
                shutil.copyfile(srcfile, targetfile)
                break
        b['sampled'][selected] = 1
        i += 1
b.to_csv('/users/barry/desktop/wp_classified/nondata.csv')