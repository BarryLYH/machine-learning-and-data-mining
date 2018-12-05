import os
import shutil

path_txt = '/users/barry/desktop/wp_txt'
files_txt =os.listdir(path_txt)

path_pdf = '/users/barry/desktop/whitepapers'
files_pdf =os.listdir(path_pdf)


for file_pdf in files_pdf:
    name = file_pdf[:-4]
    j = True
    for file_txt in files_txt:
        if name == file_txt[:-4]:
            j = False
            break
    if j:
        srcfile = os.path.join(path_pdf, file_pdf)
        targetfile = os.path.join('/users/barry/desktop/12', file_pdf)
        shutil.copyfile(srcfile, targetfile)