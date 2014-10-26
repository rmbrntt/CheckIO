__author__ = 'Ryan'
def checkio(first, second):
    result = []
    for word in first.split(','):
        if word in second.split(','):
            result.append(word)
    return ','.join(sorted(result))

#def checkio(first, second):
#    return ','.join(sorted([s for s in first.split(',') if s in second.split(',')]))

first = "hello,world,the,end,near,is"
second = "hello,earth,test,end"

print checkio(first, second)

