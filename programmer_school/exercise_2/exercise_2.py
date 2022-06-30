def summary(input_file, output_file):
    file = open(input_file, 'r')
    result = open(output_file, 'w')
    # summ = 0
    for line in file:
        if int(line) > 10**4:
            result.write('INVALID NUMBER' + '\n')
        else:
            summ = 0
            for i in range(0, int(line) + 1):
                summ += i
            result.write(str(summ) + '\n')


summary('INPUT.txt','OUTPUT.txt')