def multiply(input_file, output_file):
    file = open(input_file, 'r')
    result = open(output_file, 'w')
    for line in file:
        if int(line) < 4*(10**5):
            number = int(line)**2
            result.write(str(number) + '\n')
        print(4*(10**5))
    else:
        result.write('INVALID NUMBER')


multiply('INPUT.txt', 'OUTPUT.txt')
