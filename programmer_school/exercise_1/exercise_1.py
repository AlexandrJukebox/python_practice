def summary(input_file):
    file = open(input_file,'r')
    for line in file:
        line = line.split(' ')
        print(line[0])


summary('INPUT.txt')