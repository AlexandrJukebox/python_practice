def summary(input_file, output_file):
    file = open(input_file,'r')
    result = open(output_file, 'w')
    for line in file:
        line = line.split(' ')
        summ = int(line[0]) + int(line[1])
        if summ > 10**9:
            result.write('INVALID NUMBER' + '\n')
        else:
            result.write(str(summ) + '\n')


summary('INPUT.txt', 'OUTPUT.txt')

