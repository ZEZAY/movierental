def lazyreader(filename):
    file = open(filename, 'r')
    for line in file:
        # return line.split()
        yield line.split(',')  # generator


reader = lazyreader('movies.csv')
for k in range(5):
    input('Enter to read line')
    print(next(reader))
