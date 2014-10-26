__author__ = 'Ryan'
def checkio(numbers_array):
    return sorted(numbers_array, key=abs)

print checkio([-20, 1, -5, 10, 15])