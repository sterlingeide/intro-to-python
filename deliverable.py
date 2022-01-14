# ALL README Material gets Tested Here

'''
################################################
Task 2
################################################
'''

#1
idx = 'abcde'.index('d')
idx = idx + 11
print(idx)
idx *= 2
print(idx)

#2
num = 33
isEven = num % 2 == 0
print(isEven)
print(not isEven)

#3
str1 = 'marker'
num = len('whiteboard') - len(str1)
print(num)
str2 = 'bootcamp'
print(str2[num].upper())
char = str2[num].lower()
print(char + '!')

#4
sentence = 'welcome to bootcamp prep'
lastChar = sentence[len(sentence) - 1]
print(lastChar)
print(sentence.index(lastChar))

'''
################################################
Task 3
################################################
'''

#5
age = 30
if age > 30:
    print('older than 30')
else:
    print('30 or younger')

#6
str = 'pizza'
if len(str) > 10:
    print('Long String')
else:
    print('short string')
if str[0] == 'p':
    print('starts with a p')

#7
num = 15
if num % 3 == 0:
    print('divisible by 3')
elif num % 5 == 0:
    print('divisible by 5')

#8
num = 15
if num % 3 == 0:
    print('divisible by 3')
elif num % 5 == 0:
    print('divisible by 5')

#9
str = 'General Assembely'
if str[0] == str[0].upper():
    print('Starts with a capital')
if str[len(str)-1] == str[len(str)-1].upper():
    print('Ends with a capital')

#10
num = -44
if num > 0:
    print('positive')
elif num < 0:
    print('negative')
else:
    print(0)
if num % 2 == 0:
    print('even')
else:
    print('odd')

'''
################################################
Task 4
################################################
'''

#11
num = 11
if num > 5:
    print('if')

#12
num = 5
if num > 5:
    print('if')
else:
    print('else')

#13
num = 0
if num < 0:
    print('if')
elif num > 0:
    print('elif')
else:
    print('else')

'''
################################################
Task 5
################################################
'''

#14
def say_hello(name):
    msg = 'Hello, ' + name + '. How are you?'
    return msg
print(say_hello('bootcamp prep'))

#15
def check_number(num):
    if num > 0:
        return 'positive'
    elif num < 0:
        return 'negative'
    else:
        return 'zero'
print(check_number(5))

#16
def fizz_buzz_1(max):
    i = 0
    while i < max:
        if i % 3 == 0 and not i % 5 == 0:
            print('fizz', i)
        elif i % 5 == 0 and not i % 3 == 0:
            print ('buzz', i)
        i+=1

fizz_buzz_1(16)

#17
def even_caps(sentence):
    newSentence = ''
    i = 0

    while i < len(sentence):
        char = sentence[i]

        if i % 2 == 0:
            capitalChar = char.upper()
            newSentence += capitalChar
        else:
            newSentence += char
        i+=1

    return newSentence

print(even_caps('Hello, my name is Sterling'))