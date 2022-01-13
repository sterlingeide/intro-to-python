#this is a comment
# TODO build this fnuction 

from operator import truediv


def add(num, num2):
    '''
    this is a multiline comment in a function
    '''

name = "Johnny"
print(name)

nothing = None 
print(nothing)

is_working = True
car_off = False

print(is_working)
print(False)
# print(false)
    #this won't work

if is_working and car_off: 
    print('This is true')
elif is_working:
    print('this is the second condition')
else:
    print('This is not true')

if is_working or car_off: 
    print('This is true')
else:
    print('This is not true')


print(15/6)
print(15//6) #force it into an integer
print(15//8) #rounds down


print(2 ** 3) #using power


print("ace of spades".split(" "))
print("qqxzzz".index("x"))
print("qqxzzz".index("z"))
print("boo".upper())
print("WHY???".lower())
print("then I went to the store I like".replace("I", "you"))
print("eggs" in "green eggs and ham")
print(len('Hawaii'))
print('Is it a digit', '7'.isdigit())

string = 'My name is Sterling'
print(string[8])
print(string[-7])
print(string[11:19])
print(string[11:19:2])
print(string[:10])
print(string[8:])
print(string[::-1])
print(string[::2])


if 7 == 7:
    print('These are equal')
if 7 != 8:
    print('these are not equal')
if 7 == 7 and 8==8:
    print('These are both equal')
if 7 == 8 or 8==8:
    print('One of these equals 8')
if True:
    print('True is a truthy value')
if not False:
    print('False is a falsey value')


arr = [1, "two", 3, "four", True, False, "hello"]
print(len(arr))
print(arr[1])
print(arr[-1])
one_through_ten = list(range(10))
print(one_through_ten)
five_zeroes = [0] * 5
print(five_zeroes)
three_through_ten = list(range(3,10))
print(three_through_ten)


a = [1, 23, 12, 99, 82]
a.sort()
print(a)
print(a[::-1])
a.append(42)
print(a)
a.pop()
print(a)
a.insert(2, 123)
print(a)
if 123 in a:
    print('123 is in the list')


cat = {
    "name": 'Hamlet',
    'breed': 'American Shorthair',
    "fav_food": "Prosciutto"
}
print(cat['name'])
cat["name"] = 'Garfield'
print(cat['name'])
print(cat.get('breed'))
cat["age"] = 3
print(cat.get("age"))
print ('ITEMS', cat.items())
print ('KEYS', cat.keys())


print(int("42"))
print(str(42))
print(float(42))
print(bool(42))
print(bool(0))
print(bool("food"))
print(bool(""))


#string interpulation
state = "Washington State"
year = 1889
n = 42
def st_nd_rd_th(n):
  # add one to 13 because range is exclusive at the end.
  if n in range(11, 13 + 1):
    return "th"
  if n % 10 == 1:
    return "st"
  elif n % 10 == 2:
    return "nd"
  elif n % 10 == 3:
    return "rd"
  else:
    return "th"
my_message = f"{state} was the {n}{st_nd_rd_th(n)} state to join the union in {year}."
print(my_message)

topic = 'Inflation'
num = 7
y =1982
another_message = "{} is at {} percent. Highest since {}".format(topic,num,y)
print(another_message)

name = 'Sterling'
age = '23'
introduction = f"My name is {name} and I am {age} years old"
print(introduction)
intro = "My name is {} and I am {} years old".format(name, age)
print(intro)

template = "My name is {name} and I like {food}"
template.format(food="Cheese", name="Steve")
'My name is Steve and I like Cheese'


n = 0
while n < 5:
  print(n)  
  n+=1

for i in range(0, 10, 2):
  if i % 2 == 0:
    print("{} is even".format(i))
  if i % 2 == 1:
    print("{} is odd".format(i))

nums = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(nums)):
    element = nums[i]
    if element % 2 == 0:
        print(f"{element} is even")

    if element == 8:
        print('this is 8')
        
students = [
    {
        "name": "Kimmie",
        'city': 'Atlanta'
    },
    {
        "name": "John",
        'city': 'LA'
    },
    {
        "name": "Sammie",
        'city': 'Boston'
    },
]
for i in range(len(students)):
    student = students[i]
    print(student.get("name"))

    if student.get("city") == "LA":
        print(f'{student.get("name")} wins an iPad for {student.get("city")}')

for student in students:
    print(student)

for key in students[0]:
    print('key', key)
    print('value', students[0].get(key))

for key in students[1]:
    print('key', key)
    print('value', students[1][key])

for key, value in students[2].items():
    print('key', key)
    print('value', value)


# def say_hello():
#   print("Hello, World!")


def say_hello(friend="Tim"):
  print("Hello, {}!".format(friend))
say_hello()

def move(name, city="Seattle", state="Washington"):
  msg = "{} is moving to {}, {}"
  msg = msg.format(name, city, state)
  print(msg)
move('Charlie')
move('Deborah', 'LA', 'California')

def order(food, drink="Soda"):
  msg = "The order is {} and {}"
  msg = msg.format(food, drink)
  print(msg)
order('Pizza')
order('Cheese Burger', 'Sprite')