# author: github.com/teo113
# desc: This script performs various directory and file management tasks (copying, making, deleting etc.)

import os
import shutil
import time
from datetime import datetime
from zipfile import ZipFile

# directories
dir = r'C:\Users\theo\Documents\tasks_c\dir_editing\main'
subdir = dir + r'\subdir'

# if dir does not exist, make it
if not os.path.exists(dir):
    os.mkdir(dir)
    print(dir + ' created')
time.sleep(5)

# in dir, create .txt file with text
with open(dir + r'\test.txt', 'w') as file:
    file.write('Here is some text')
print('text file created')
time.sleep(5)

# in dir, create sub-dir
if not os.path.exists(subdir):
    os.mkdir(subdir)
    print(subdir + ' created')
time.sleep(5)

# in sub-dir, create copy of .txt file with new name (using shutil)
txt_orig = dir + r'\test.txt'
txt_copy = subdir + r'\test_copy.txt'
shutil.copy(txt_orig, txt_copy)
print(txt_copy + ' created')
time.sleep(5)

# zip copy .txt file in sub-dir, add date stamp
date = datetime.now().strftime('%Y%m%d')
zipped = os.path.join(subdir, 'test_' + date + '.zip')
with ZipFile(zipped, 'w') as zipf:
    zipf.write(txt_copy, arcname='test_copy.txt')
print(zipped + ' created')
time.sleep(5)

# move zip file from subdir to dir
shutil.move(zipped, dir + r'\test_' + date + '.zip')
print('zip file moved to dir')
time.sleep(5)

# in sub-dir, delete .txt file
if os.path.exists(txt_copy):
    os.remove(txt_copy)
    print(txt_copy + ' deleted')
time.sleep(5)

# if dir exists, rename it
if os.path.exists(dir):
    os.rename(dir, dir + '_renamed')
    print(dir + ' renamed')
time.sleep(5)

# if dir exists, delete it and its contents
if os.path.exists(dir + '_renamed'):
    shutil.rmtree(dir + '_renamed')
    print(dir + '_renamed deleted')
time.sleep(5)
