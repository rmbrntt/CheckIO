__author__ = 'Ryan'
#Find the median in a list of numbers
def checkio(data):
    if len(data) % 2 == 0:
        return float(sorted(data)[(len(data)/2)] + sorted(data)[((len(data)/2)-1)])/2
    return sorted(data)[(len(data)/2)]

data = [1, 2, 47, 45, 4, 5]
print checkio(data)
