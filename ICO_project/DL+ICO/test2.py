import os
import shutil

path_txt = '/users/barry/desktop/whitep'
files_txt =os.listdir(path_txt)

path = '/users/barry/desktop/need'


for file_txt in files_txt:
    name = file_txt.split('.pdf')[0]+'.txt'
    srcfile = os.path.join(path_txt, file_txt)
    targetfile = os.path.join(path, name)
    shutil.copyfile(srcfile, targetfile)