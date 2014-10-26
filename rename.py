__author__ = 'Ryan'
import os
def rename():
    file_list = os.listdir(r'D:\Dev\Projects\CheckIO\prank')
    os.chdir(r'D:\Dev\Projects\CheckIO\prank')
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, '0123456789'))


rename()