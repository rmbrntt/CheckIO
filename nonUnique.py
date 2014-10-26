__author__ = 'Ryan'
def checkio(data):
    return [n for n in data if data.count(n) > 1]


print checkio([1, 2, 3, 1, 3])
#print checkio([1, 2, 3, 4, 5])