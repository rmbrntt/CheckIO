__author__ = 'Ryan'
import string
alpha = string.ascii_letters
num = string.digits

pwd = 'Password1'

if alpha in pwd and num in pwd:
    print True

