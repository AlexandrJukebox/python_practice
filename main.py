"""
#  -------------------------------------------Черновик-----------------------------------------------------------------


#  --------------------------------------------------------------------------------------------------------------------


def function(first_data):
    a = first_data**2
    b = first_data/123
    c = a + b
    print('a = ', a, ' and b =', b)
    print('a is ', type(a), ' and b is', type(b))
    x = 15
    while x < c:
        x += x * 2
        print(bool(c))
    for i in 'hello world':
        if i == 'e':
            print('Breaked on: ', i)
            break
    else:
        print('Буквы a в строке нет')
   # for i in hello:
     #   print(i)
function(int(input('введите число: ')))


#  --------------------------------------------------------------------------------------------------------------------


# x = divmod(124, 110)

value = 66
print(bin(value))
print(oct(value))
print(hex(value))
print(ord('G'))
i = 33
list = []
while i < 128:
    i += 1
    list += chr(i)
print(list)

#print(float('-1_099_999_231'))


#  ---------------------------------------------------------------------------------------------------------------------


def seconds_in_hour(hours):
    seconds = hours * (60 * 60)
    # print('В ', hours, ' часах(е) - ', seconds, 'секунд')
    # seconds_per_hour = seconds_in_hour(int(input('Введите колличество часов: ')))
    return seconds


def seconds_in_day(days):
    seconds_per_hour = seconds_in_hour(1)
    seconds_per_day = seconds_per_hour * (days * 24)
    print('В ', days, 'дне/днях', seconds_per_day, ' секунд')
    float_division = seconds_per_day / seconds_per_hour
    integer_division = seconds_per_day // seconds_per_hour
    print(float_division)
    print(integer_division)
    print(float_division == integer_division)


seconds_in_day(20)


#  ---------------------------------------------------------------------------------------------------------------------


disaster = False
if disaster:
    print('Run!')
else:
    print('Calm down')


color = "blue"
if color == "red":
    print('1')
elif color == "blue":
    print('2')
else:
    print('3')


number = 5
print(8 - 10 < number != 4)


#  -----------------Вывод типов данных с переменными, boolean значениe которых, отлично от False----------------------


def variables():
    boolean = False
    integer = 2
    float_number = 1.0
    string = ''
    lists = []
    tuples = ()
    dictionary = {}
    quantity = set()
    variable_types = []
    variable_values = []
    variable_dictionary = {'boolean': boolean, 'integer': integer, 'float_number': float_number, 'string': string,\
    'lists': lists, 'tuples': tuples, 'dictionary': dictionary, 'quantity': quantity}
    variable_types += variable_dictionary.keys()
    variable_values += variable_dictionary.values()
    true_list = []
    for i in range(len(variable_types)):
        if variable_values[i]:
            true_list.append(variable_types[i])
            true_list.append(' = ')
            true_list.append(variable_values[i])
            true_list.append(';')
    print(true_list, ' is not False')


variables()


#  -----------------Выполнение нескольких Сравнений с помощью оператора 'in' -------------------------------------------

def vowel_letter():
    letter = 'o'
    vowel_set = {'a', 'b', 'o', 'l'}
    vowel_list = ['a', 'b', 'o', 'l']
    vowel_tuple = ('a', 'b', 'o', 'l')
    vowel_dict = {'a': 'apple', 'e': 'elephant', 'i': 'ibonitic'}
    vowel_string = 'hello'
    question_one = letter in vowel_set
    question_two = letter in vowel_list
    question_three = letter in vowel_tuple
    question_four = letter in vowel_dict
    question_five = letter in vowel_string
    print(question_one, question_two, question_three, question_four, question_five)


vowel_letter()


#  -----------------I am the Walrus. Сравнение с использованием моржового оператора «:=» и модуля числа-----------------


def i_am_the_walrus(number):
    text_limit = 280
    text_string = ("Some text"+"\n") * number
    if condition := text_limit - len(text_string) >= 0:
        print("Thats fine", abs(condition))
    else:
        print("To0 mutch", abs(condition))

i_am_the_walrus(4)


def exercise_one(number_one, number_two):
    secret = number_one
    guess = number_two
    if secret == guess:
        print('just right')
    elif secret + guess < 100:
        print('too low', guess, secret)
    else:
        print('too high', guess)


#  -----------------Упражнение-----------------------------------------------------------------------------------------


def exercise_two(size, color):

    chery = ['small', 'red']
    pea_coal = ['small', 'green']
    watermelon = ['big', 'green']
    pumpkin = ['big', 'orange']
    berries = [chery, pea_coal, watermelon, pumpkin]
    i = 0
    done = 0
    for type in berries:
        if type[0] == size and type[1] == color:
            if i == 0:
                print('It is a', 'CHERY')
                done = 1
            elif i == 1:
                print('It is a', 'PEA-COAL')
                done = 1
            elif i == 2:
                print('It is a', 'WATERMALON')
                done = 1
            elif i == 3:
                print('It is a', 'PUMPKIN')
                done = 1
        if i >= 3 and done == 0:
            print('Who are you, mutant?')
        i += 1
    if size == 'small':
        size = True
    else:
        size = False
    if color == 'green':
        color = True
    else:
        color = False
    if size + color == 2:
        print('Thats my favorite!')
    else:
        print('I dont want it! Lets try another.')


exercise_two('small', 'green')


def some_text(string):
    text = '''Вышел ёжик , \
из \nтумана\rвынул\t\t\tкор\vжи\a\a\aк\a "из"\
'кармана'?!
                '''
    value = 214
    number = '12tf1'
    #c = f'A:%d, B:}'
    #line = f'A:{text}, B:{string}', int(string) - 214442, int(string) % 21
    #print(line, sep=' #### ')
    print(text)
#
# some_text(str(input()))
#
# _list = string.whitespace
# for i in _list:
#      print(i)

#  -----------------Esc - последовательность---------------------------------------------------------------------------


print('this is \t - tabulation')
print('this is \n - new line')
print('\\n\\t - this is backslash (\\) bends over backwards to shield the escape-sequence')
print(r'Type a \n to get a new line in normal string. Type \t for tabulation and \ to shield the escape-sequence')




#  -----------------Конкатинация строки, brakets for line break---------------------------------------------------------


print("Release the kraken! " + "No, wait")

vowels = ('abs'
          'defg'
          'hijk'
          'lmn'
          'opq'
          'rst'
          'uvw'
          'xyz')
print(vowels)


a = 'Duck.'
b = 'Grey Duck!'
c = a
print((a + b + c) * 2 + vowels)


#  -----------------Вывод строки. Начало с большой буквы, всё остальное с маленькой------------------------------------


def string(input):
    line = str(input)
    new_string = []
    index = 0
    for letter in line:
        if index == 0:
            new_string.append(line[0].upper())
        if index > 0:
            new_string.append(letter.lower())
        index += 1
    _line = ''.join(new_string)
    print(_line)


string('ИНСТРУКЦИЯ по накоплению отходов «Аккумуляторы свинцовые отработанные неповрежденные, с электролитом»')


#  -----------------Multiply strings with «*» symbol and using symbols "[]" to  extract symbol-------------------------



def string():
    start = 'Na ' * 4 +'\n'
    middle = 'Hey ' * 3 +'\n'
    end = 'Goodbye.'
    line = []
    line.append(start)
    line.append(middle)
    line.append(end)
    # line = start + middle + end
    li = line[0].strip('\n')
    li += line[1].replace('\n','    ')
    li += line[2]
    # lane = ''
    # for i in li:
    #     print(i)
    lane = ''.join([i for i in li])[2::3]
    print(lane)


string()

x = input('To start developing "ТЗ" press ENTER...')
print(x)

#  -----------------Multiply strings with «*» symbol and using symbols "[]" to  extract symbol-------------------------

def ckuak(count):
    voice = []
    letters = ''
    for x in range(0, count):
        duck = 'quak!'
        voice.append(duck)
    # print(*voice)
    letterts = voice[0]
    newduck = duck.replace('q', 'D')
    print(duck.replace('q', 'D'), duck.replace('a', 'c'))
    print(newduck.replace('a', 'c'))
    print((letterts[0:2] * 2 + (letterts[2:5] * 3) + letterts[-2] + '  ') * 2)

ckuak(6)
"""

#  -----------------Extracting the substring by using colon operator---------------------------------------------------

def colon_operator():
    text = 'Here i brought you some tasty text, so use it wisely'
    text_2 = 'i have hlidledo here some word, try to find it'
    letters = text[19:-18:1]
    letters_2 = text_2[2::3]
    print(letters)
    print(letters_2[0:5])

colon_operator()