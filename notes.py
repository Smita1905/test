# print('hello world', end='*****')
# print('hello universe')     #hello world*****hello universe

# print('hello', 'python')        #hello python
# print('hello', 'python', sep='####')        #hello####python

# print('python', end=' ')
# print('selenium', 'django', sep='&&&&', end='****')
# print('Ruby')

#####################################################
'''type() =
Inbuilt function which Returns the type of the variable passed
We can check only one variable at a time
Syntax : type(var_name)  <class datatype>
'''
# a = 10
# print(type(a))          #<class 'int'>
# print(type(9.7))        #<class 'float'>
# print(type(8+9j))       #<class 'complex'>
# print(type(True))       #<class 'bool'>

####################################################
'''id() - 
* Its an inbuilt function which returns the address of any user defined identifier.
* id() takes only 1 parameter.
* Syntax : id(user_defined_identifier)
'''
# num = 50
# print(id(num))          #3081579923216
# num1 = 50
# print(id(num1))         #3081579923216
####################################
'''int to other datatypes'''
# a = 10
# print(id(a))
# print(float(a))     #10.0
# print(type(a))      #<class 'int'>
# print(id(a))
#
# a = 5
# print(complex(a))       #(5+0j)
# print(complex(a, 6))        #(5+6j)
# print(complex(a, -5.3))     #(5-5.3j)
#
# a = 5
# print(bool(a))          #True
# print(bool(-8))         #True
# print(bool(0))          #False

#####
# a = 9.999
# print(int(a))       #9
# print(complex(a))       #(9.999+0j)
# print(complex(a, 7))    #(9.999+7j)
# print(bool(a))      #True
# print(bool(0.1))    #True
# print(bool(1.0))    #True
# print(bool(0.0))    #False

#############
# a = 6+5j
# print(int(a))       #TypeError
# print(float(a))         #TypeError
# print(bool(a))          #True
# print(bool(0 + 7j))         #True
# print(bool(9+0j))       #True
# print(bool(0+0j))       #False

######################
'''Typecasting : Converting one datatype to the another is called typecasting
Conversion from int to float, complex is  possible
Conversion from float to int, complex is possible
BUt the conversion from complex to anyother datatype is not possible
'''
#############################################################################
'''Default values : The boolean false values are the default values'''
'''For integers, 0 and int() are the default values'''
# print(bool(0))              #False
# print(bool(int()))          #False

'''For float, 0.0 and float() are the default values'''
# print(bool(0.0))                #False
# print(bool(float()))            #False

'''For complex, 0+0j/0j and complex() are the default values'''
# print(bool(complex(0j)))        #False
# print(bool(complex(0 + 0j)))        #False
# print(bool(complex()))          #False

############################################################################
'''ord() : To check the ASCII values'''
# print(ord('a'))     #97
# print(ord('b'))     #98
# print(ord('A'))     #65
# print(ord('B'))     #66

'''chr()'''
# print(chr(65))      #A
# print(chr(97))      #a

############################################################################
'''dir() : Gives the list of attributes'''
# a = 10
# print(dir(a))
# print(dir(complex))

#####################################################################
# a = 'python'
# print(a)
# print("python is awesome")
# print('''python is fun''')

# a = 'I'm from Bangalore'
# print(a)        #SyntaxError

# a = "I'm from Bangalore"
# print(a)        #I'm from Bangalore
# b = '''I'm from Bangalore'''
# print(b)

# b = 'My name is "RAM"'
# print(b)
# c = '''My name is "Ram"'''
# print(c)

# a = '''My name is "RAM", I'm from Bangalore'''
# print(a)
# b = """My name is "RAM", I'm from Bangalore"""
# print(b)

'''default values'''
# print(bool(''))     #False
# print(bool(""))     #False
# print(bool(str()))  #False

# a = 125
# b = str(a)
# print(type(a))      #<class 'int'>
# print(type(b))      #<class 'str'>

'''to find the length of a string, we use len() inbuilt function'''
# a = 'python is a programming language'
# print(len(a))

###################################################################
'''Raw strings'''
# print('hello \n python')
#               '''hello
#               python'''

# print(r'hello \n python')

# Hi \nick, Happy bir\thday.
# print('Hi \\nick, Happy bir\\thday')        #Hi \nick, Happy bir\thday
# print(r'Hi \nick, Happy bir\thday')         #Hi \nick, Happy bir\thday

###############################################################
'''June 29 2022'''
'''format strings
Infusing data dynamically into a string during the time of execution is called
    formatting.
    There are 3 ways of string formatting.
        Formatting with placeholders.
        Formatting with .format() method.
        Formatting with string literals called f-strings.
'''
'''1. Formatting with placeholders
    *Oldest method of string formatting
    *Here we use % operator
    * The modulo % is known as 'string formatting operator'. 
        %s = Used to  inject strings
        %f = Used to inject floating values
        %d = Used to inject integers
'''
# print('My name is %s'%'John')       #My name is John
# print('My name is %s, I am %d years old'%('John', 60))  #My name is John, I am 60 years old
# print('The value of PI is %f'%3.14)     #The value of PI is 3.140000
# print('The value of PI is %d'%3.142)
# print('My name is %s, I am %d years old'%(55, 'John'))      #TypeError

###################################
'''Formatting with .format() string method
    *Formatting is done by calling .format() method
    *Here the placeholders {} are used to infuse the data at the runtime  '''
# print('Hi, My name is {}, I am {} years old'.format('John', 60))    #Hi, My name is John, I am 60 years old
# print('Hi, My name is {}, I am {} years old'.format(60, 'John'))        #Hi, My name is 60, I am John years old
# print('Hi, My name is {1}, I am {0} years old'.format(60, 'John'))  #Hi, My name is John, I am 60 years old
# print('Hi, My name is {name}, I am {age} years old'.format(age=60, name='John'))    #Hi, My name is John, I am 60 years old

################################################
'''Formatted string literals(f-strings)
    *Here we can use the outside variables directly into the string instead of passing them
    as arguments
    * Here placeholders {variable} are used to infuse the data at the runtime
'''
# name = 'Ram'
# age = 60
# print(f'My name is {name}, I am {age} years old')   #My name is Ram, I am 60 years old
#
# a = 24
# b = 60
# print(f'There are {a} hours in a day')      #There are 24 hours in a day
# print(f'There are {b * a} minutes in a day')    #There are 1440 minutes in a day

# name = input('Enter the name: ')
# print(f'My name is {name}')

'''
NOTE: 
If number of placeholders is greater than number of values inside .format()
method Index Error
If number of placeholders is less than number of values inside .format()
method  takes required number of values from first, rest is ignored.
Here we have a disadvantage that we cannot perform operations inside
placeholders. Were we can do this in f-strings.
'''
##########################################
'''input: 
* Standard function used to take the user’s input at the runtime.
* The input() always reads the input as a string even if it comprises of digits.
* Syntax : input() or input(“specification about the input”)
* Example :
     var_name = input(“enter a number”)
     Here the var_name holds the value which is assigned at runtime
'''
# a = input('Enter the value of a: ')
# print(f'The value of a is {a}')
# print(type(a))      #<class 'str'>
#
# a = int(input('Enter the value of a: '))
# print(type(a))      #<class 'int'>

###########################################
'''isinstance :
* An in built function which is use to check the value or variable is of the same
    data type we specified or not.
* It returns the Boolean data type, True if the value is of specified data types,
    False if the value is not of specified data type
* It have two required parameter, one is value or variable, another one is the data
    type we need to specify.
* We can insert multiple data as a second argument but we should give those
    multiple data type in a tuple
* It will return True if the value belongs to any of the data types mentioned with
    in the tuple
Syntax1 : isinstance(var_name or value, data type)
Syntax2: isinstance(var_name or value, (data type1, datatype2, …))

'''
# print(isinstance(10, int))      #True
# print(isinstance(5.8, int))     #False
# print(isinstance(8-9j, complex))    #True
# print(isinstance(10.9, (int, float, complex)))      #True
# print(isinstance('John', (int, float, bool, complex)))      #False

######################################################################
# a = 'hello python'
# print(a[0])     #h
# print(a[6])     #p
# print(a[11])    #n
# print(a[20])      #IndexError

# print(a[-2])        #o
# print(a[-6])        #p
#######################################################################
'''July 4 2022'''
'''type() = type(var_name)'''
# a = 100
# print(a)
# print(type(a))
# print(type(2.4))

#####################################################################################
'''July 5 2022'''
'''integer
* It specifies the data stored in the memory location to be an integer
* It can be positive or negative
* To convert a decimal value to an integer we use constructor int()
    Syntax : var_name = int(decimal value or decimal variable)

float
* It specifies the data stored inside the memory location is of type decimal.
* It can be positive or negative.
* Default value of float is 0.0
* To convert integer into a float value we use constructor float()
    Syntax: var_name = float(integer variable or integer value)

complex
* The data type in the form of a+bj , where a is the real part and b is the
    imaginary part
* It can be positive or negative
* Default value of complex is 0+0j
* To convert integer or float into a complex value we use constructor complex()
    Syntax: var_name = complex(integer/float variable or integer/float value)

boolean
* Useful in conditional statements
* Boolean variables are defined by the True and False keyword
* Default value of Boolean data type is False
* To convert any value to Boolean type we use constructor bool()
    Syntax : var_name = bool(value or variable)    
'''
#########################################################################

'''Typecasting : The process of converting one datatype to other is called Typecasting'''
'''converting integer to other datatypes'''
# a = 10
# print(float(a))         #10.0
# print(complex(a))       #(10+0j)
# print(complex(a, 7))    #(10+7j)
# print(bool(a))          #True
# print(bool(-9))         #True
# print(bool(1000))
# print(bool(0))          #False

'''NOTE: The boolean of any non-zero value is always True'''

#############################################################
'''Converting float to other datatypes'''
# a = 9.8
# print(int(a))       #9
# print(complex(a))   #(9.8+0j)
# print(complex(a, -3))   #(9.8-3j)
# print(bool(a))      #True
# print(bool(0.00001))    #True
# print(bool(0.0))        #False

################################################################
'''Converting complex to other datatypes'''
# a = 5-9j
# print(int(a))       #TypeError
# print(float(a))         #TypeError
# print(bool(a))          #True
# print(bool(5 + 0j))     #True
# print(bool(0 + 9j))     #True
# print(bool(0 + 0j))     #False

'''NOTE: We can't convert complex to anyother datatype'''

#####################################################################
'''Default Values
* The default value of integer is 0/int()
* The default value of float is 0.0/float()
* The default value of complex is 0+0j/complex()
* The defalt value of bool is False/bool()
'''
# print(bool(0))      #False
# print(bool(int()))  #False
#
# print(bool(0.0))    #False
# print(bool(float()))    #False
#
# print(bool(0+0j))   #False
# print(bool(complex()))  #False
#
# print(bool(False))  #False
# print(bool(bool())) #False

####################################################################
'''id() = To get the memory allocation'''
# a = 10
# print(id(a))

#####################################################################
'''6 July 2022'''
'''print() = 
* standard function used to print the output to the console.
	syntax: print(value1, value 2, ...)
* It has 2 parameters:
    end : it is used to combine two or more print statement
	    syntax: print(value, end='string')  		→ default value→ '\n'
    sep : it is used to combine two or more values in single print statement.
	    syntax: print(value1, value2, sep='string')	→ default value→ (space) '''
# print('python', end='*****')
# print('selenium')       #python*****selenium
#
# print('python', end='***')
# print('selenium', end='$$$')
# print('javascript')         #python***selenium$$$javascript
#
# print('Batman','Spiderman','hulk')        #Batman Spiderman hulk
# print('Batman', 'Spiderman', 'hulk', sep='@')    #Batman@Spiderman@hulk
#
# print('Batman', 'Spiderman', 'thor', sep='##', end='^')
# print('ironman', 'superman', sep='@', end='*')
# print('hulk')       #Batman##Spiderman##thor^ironman@superman*hulk

###################################################################################
'''input() 
* Inbuilt function which is used take the user's input at runtime of code.
* The input() function always reads the input data as string,even if it comprises of digit.
	Syntax: input() / input('description about input')
'''
# a = input('Enter the value of a: ')
# print(a)

###################################################################################
'''isinstance() 
* This is a inbuilt function which will check whether given variable or value is of 
    specified datatype or not.
* Syntax: isinstance(variable, datatype) ⇒ True/False (return type)
* We can mention two or more datatype as group inside (), this will return True if it 
matches with any one of the type mentioned
'''
# a = 10
# print(isinstance(a, int))
# print(isinstance(9.8, complex))
# print(isinstance(2, int, float, complex))       #TypeError
# print(isinstance(2, (float, complex)))            #False

###################################################################################
'''Collection datatypes'''
'''String :
* Set or collections of characters
* Boundary: “....” 	or 	‘....’ 		or	 ‘‘‘...... ’’’ 
* It is an immutable data type
* Syntax:var_name = “string”
* Default value of string is  “” or str() [empty string]g
* Length of a string: len("string") or len(var_name)
    len function on strings gives the number of character present in a string
'''
# a = 'hello python'
# b = "hello python"
# c = '''hello python'''
# print(type(a))      #<class 'str'>

'''Using string constructor: 
    word = str('Hello world')
    num = str(123) ⇒ ‘123’

NOTE: Zero Length string or an empty string: word = "" or word = str()
       bool() value for empty string is False.'''

# a = 'My name is John. I'm from Bangalore'
# print(a)        #SyntaxError

# a = "My name is John. I'm from Bangalore"
# print(a)        #My name is John. I'm from Bangalore

# a = 'My name is "John"'
# print(a)        #My name is "John"
#
# a = '''My name is John. I'm from "Bangalore"'''
# print(a)        #My name is John. I'm from "Bangalore"
#
# a = """My name is John. I'm from "Bangalore" """
# print(a)

###########################################################################
'''len() = len(a)'''
# a = 'stranger things'
# print(len(a))

#######################################################################
'''raw strings
* Python raw strings are the string literals prefixed with "r" or "R".
* Raw strings do not treat backslashes as a part of an escape sequence. 
    It will be printed normally as a string.
* There must be a literal succeeding the backslash.
* Note: ‘\’ is known as the escape character and its used to skip some special 
    functionality like ‘\n’(new line), ‘\t’(tab space).
'''
# a = 'hello py\thon'
# print(a)        #hello py   hon
#
# b = 'hai \\nandhini'
# print(b)        #hai \nandhini
#
# a = 'hello\'
# print(a)        #SyntaxError
#
# a = R'happy bir\thday \nick'
# print(a)        #happy bir\thday \nick
##############################################################################
'''format strings
i. formatting with placeholders
ii. formatting with .format() method
iii. formatting with string literals
'''
'''formatting with placeholders
* oldest method of string formatting
* here we use % modulo operator
* %s is used to inject string
  %d is used to inject integers
  %f is used to inject float
'''
# print('My name is %s'%'John')
# a = input('Enter the name: ')
# print('My name is %s'%a)
#
# print('My name is %s, I am %d years old'%('Ram', 40)) #My name is Ram, I am 40 years old
# print('The value of PI is %f'%3.14)     #The value of PI is 3.140000
# print('My name is %s, I am %d years old'%(40, 'Ram'))       #TypeError

######################################################################
'''formatting with .format() method 
* Formatting is done by calling.format() method.Here placeholders ({}) are used to infuse
 the data at the runtime.
'''
# a = 'My name is {} and I am {} years old'.format('Raavan', 55)
# print(a)    #My name is Raavan and I am 55 years old

# a = 'My name is {} and I am {} years old'.format(55, 'Raavan')
# print(a)    #My name is 55 and I am Raavan years old
#
# a = 'My name is {1} and I am {0} years old'.format(55, 'Raavan')
# print(a)    #My name is Raavan and I am 55 years old
#
# a = 'My name is {name} and I am {age} years old'.format(age=55, name='Raavan')
# print(a)        #My name is Raavan and I am 55 years old

#################################################################################
'''formatted string literals (f-strings)
* Here we can use outside variables directly into the string instead of passing them as 
    arguments.
* Here placeholders ( {variable} ) are used to infuse the data at the runtime
'''
# a = 'Raavan'
# b = 55
# print(f'My name is {a} I am {b} years old') #My name is Raavan I am 55 years old
#
# a = 24
# b = 60
# print(F'A day has {a} hours, {a*b} minutes')    #A day has 24 hours, 1440 minutes

#################################################################################
'''7  y 2022'''
'''Indexing:
* Process of extracting single character at a time.
* Indexing can be positive(starts with 0) or negative(starts with-1).
* Throws IndexError if the index is out of range
    Syntax: var_name[index]
'''
# a = 'hello python'
# print(a[0])     #h
# print(a[8])     #t
# print(a[15])    #IndexError: string index out of range
#
# print(a[-12])       #h
# print(a[-2])        #o
# print(a[-20])       #IndexError: string index out of range

########################################################################
'''Slicing
Process of extracting multiple characters at a time/simultaneously.
Syntax : var_name[start index: End index :Step value]
start index default value 0
End index : default value length of the string
Step value default value 1(optional)
Element at the end index will not be added in the slice.

Note: Positive step value indicate the slice from left to right(forward) and negative step value indicate the slice from right left(reverse).
	Wrong slicing will give Empty string, Slicing never gives us error
'''

# a = 'hello python'
# print(a[1:5:1])     #ello
# print(a[1:5])       #ello
# print(a[3:10:1])    #lo pyth
# print(a[::])        #hello python
# print(a[::2])       #hlopto
# print(a[1::2])      #el yhn

############################################################################
'''8 July 2022'''
# a = 'happy friday'
# print(a[-9:-3:1])   #py fri
# print(a[-6:])       #friday
# print(a[-12:-6])    #happy
# print(a[-6:0:1])    #''
# print(a[0:35])      #happy friday,  even if the end index is out of range, sliicing will
# slice till the end of the string. It'll not throw any error
'''NOTE : Slicing will never give error'''

# print(a[0:-7])      #happy
# print(a[-12:5])     #happy

######################################################################
# a = 'python is a programming language'
# print(a[0:6])       #python
# print(a[-32:-26])   #python
# print(a[0:-26])     #python
# print(a[-32:6])     #python

# print(a[12:23:1])   #programming
# print(a[-20:-9])    #programming
# print(a[12:-9])     #programming
# print(a[-20:23])    #programming

# print(a[24:32])     #language
# print(a[-8:])       #language
# print(a[24: ])      #language
# print(a[-8:32])     #language

#######################################################################
# a = 'happy friday'
# print(a[11:5:-1])       #yadirf
# print(a[4::-1])         #yppah

# a = 'python is a programming language'
# print(a[5::-1])         #nohtyp
# print(a[-27::-1])       #nohtyp
# print(a[5:-33:-1])      #nohtyp

# print(a[22:11:-1])      #gnimmargorp
# print(a[-10:-21:-1])    #gnimmargorp
# print(a[22:-21:-1])     #gnimmargorp
# print(a[-10:11:-1])     #gnimmargorp

# print(a[31:23:-1])      #egaugnal
# print(a[-1:-9:-1])      #egaugnal
# print(a[31:-9:-1])      #egaugnal
# print(a[-1:23:-1])      #egaugnal

'''print the string in reversed order'''
# print(a[::-1])      #egaugnal gnimmargorp a si nohtyp
# print(a[31::-1])      #egaugnal gnimmargorp a si nohtyp
# print(a[-1:-33:-1])     #egaugnal gnimmargorp a si nohtyp
# print(a[-1::-1])        #egaugnal gnimmargorp a si nohtyp

'''print every alternate characters in the above string in reverse order and also normal'''
# print(a[-1::-2])    #eaga nmagr  inhy
# print(a[0::2])      #pto sapormiglnug

'''print the extension of the filename = youtube.txt '''
# a= 'youtube.txt'
# print(a[8:11:1])        #txt
# print(a[-3:])           #txt

'''print only filename = youtube.txt '''
# a= 'youtube.txt'
# print(a[0:7:1])     #youtube

'''printing only protocol = https://google.com'''
# a = 'https://google.com'
# print(a[0:5:1])     #https
# print(a[:-13:1])    #https

'''print only domain = https://google.com'''
# a = 'https://google.com'
# print(a[8:14])      #google
# print(a[-10::1])    #google.com

##################################################################################
'''9 July 2022'''
'''String methods'''
'''lower() = var_name.lower() 
* It will convert all the uppercase alpha char to lower, it will be idle for special 
    char and numeric char.
	Syntax: 'string_obj'.lower() ==> new string.'''
# a = 'HELLO WORLD'
# print(a.lower())    #hello world
#
# b = 'HELlO 1234 @# UniverSE'
# print(b.lower())    #hello 1234 @# universe
#
# c = '1234 @#$%^&*'
# print(c.lower())    #1234 @#$%^&*
#
# print(a.lower(1))   #TypeError
#############################################################
'''upper() = var_name.upper() 
* It will convert all the lowercase alpha char to upper, it will be idle for special 
    char and numeric char.
	Syntax: 'string_obj'.upper() ==> new string.
'''
# a = 'hello world'
# print(a.upper())            #HELLO WORLD

############################################################
'''swapcase = var_name.swapcase() 
* It will convert all the uppercase alpha char to lower and lowercase alpha char to
 upper, it will be idle for special and numeric char.
	Syntax: 'string_obj'.swapcase() ==> new string.
'''
# a = 'HeLlO UniVErsE'
# print(a.swapcase())     #hElLo uNIveRSe

########################################################################
'''capitalize() = var_name.capitalize()
* It’s an inbuilt method which returns a string where the first character is upper
    case, and the rest to the lower case.
* If the first character is not lower case alphabet, then it will returns the same
    string as original.
'''
# a = 'hello world'
# print(a.capitalize())       #Hello world
#
# b = 'helLO WORlD'
# print(b.capitalize())   #Hello world
#
# c = '123heLLo UnIVErse'
# print(c.capitalize())       #123hello universe

##############################################################################
'''title() = var_name.title()
* It’s an inbuilt method which returns a string where the first character of each
    word converted into uppercase and rest is converted to lower case.
    i.e. All the alpha characters which are present after any special character or
    number is converted to upper case.[including first character of string]. 
'''
# a = 'python is a programming language'
# print(a.title())        #Python Is A Programming Language
#
# b = 'python@is%123a program*ming(language)'
# print(b.title())        #Python@Is%123A Program*Ming(Language)

###########################################################################
'''index() = var_name.index(value, [startvalue=0], [endvalue=len(str)])
* It will give the index value of first occurrence of the specified string in the 
original string. We can also give a range to search using start and end parameter.
Syntax : 'string_obj'.index('specified_str', [start], [end]) ⇒ int 
'''
# a = 'python'
# print(a.index('n'))     #5
# print(a.index('t'))     #2
# print(a.index('z'))     #ValueError
#
# b = 'hello world'
# print(b.index('l'))
# print(b.index('l', 4, 8))   #ValueError
# print(b.index('o', 4, 8))   #4
# print(b.index('l', 5))      #9

#############################################################################3
'''rindex() = var_name.rindex(value, [startvalue], [endvalue])
it will return the last occurrence of specified string in the original string
'''
# a = 'malayalam'
# print(a.index('m'))     #0
# print(a.rindex('m'))    #8
# print(a.rindex('a'))
# print(a.rindex('r'][))        #ValueError


'''find() = var_name.find(value, [startvalue], [endvalue])
it will give the index value of first occurrence of the specified string in the original 
string. We can also give a range to search using start and end parameter.
Syntax : 'string_obj'.index('specified_str', [start], [end]) ⇒ int 
'''
# a = 'happy weekend'
# print(a.find('e'))      #7
# print(a.find('r'))      #-1
# print(a.find('@'))      #-1
g
############################################################################
'''rfind() 
 it will return the last occurrence of specified string in the original string
	Syntax: 'string_obj'.rindex('specified_str', [start], [end]) ==> int 
'''
# a = 'happy weekend'
# print(a.rfind('e'))     #10
# print(a.rfind('9'))     #-1

###############################################################################
'''11 July 2022'''
'''count = var_name.count(substring, start, end)
*It will return the number of occurrences of a specified string present in  original string.
* count takes 3 arguments, where
    “substring” is required argument which will match with original string.
    Start is from where to start counting the given substring (optional),
        default value is 0
    End – stops counting the given substring at this index(optional), 
        default value is len(string), i.e. end of the string.
'''
# a = 'python is a programming language'
# print(a.count('a'))
# print(a.count('p'))
# print(a.count('z'))
# print(a.count('a', 3, 15))
# print(a.count())        #TypeError
#
# b = 'she sells seashells on the seashore'
# print(b.count('s'))         #8
# print(b.count('s', 0, 15))  #5
# print(b.count('e'))         #7
# print(b.count('e', 3, 9))   #1

############################################################################
'''startswith() = var_name.startswith(substring, start, end)
It will return True if the original string is starting with specified string, 
else it will return False.
'''
# a = 'python is awesome'
# print(a.startswith('p'))    #True
# print(a.startswith('o'))    #False
# print(a.startswith('P'))    #False
# print(a.startswith('t', 2)) #True
# print(a.startswith('t', 3, 10))     #False
# print(a.startswith('pyth'))     #True
# print(a.startswith('ypth'))     #False
# print(a.startswith('P'))        #False
# print(a.startswith('P'.lower()))        #True
#############################################################################
'''ord() : To get the ASCII values'''
# print(ord('A'))     #65
# print(ord('a'))     #97
'''The difference of ASCII values between uppercase and lowercase letters is 32'''

'''chr() : It'll give the character of that value'''
# print(chr(65))      #A
# print(chr(97))      #a

############################################################################
'''endswith() : var_name.endswith(substring, [start], [end])
It will return True if the original string is ending with specified string, 
else it will return False.
'''
# a = 'python is a programming language'
# print(a.endswith('e'))      #True
# print(a.endswith('g'))      #False
# print(a.endswith('age'))    #True
# print(a.endswith('n', 0, 5))    #False

##########################################################################
'''replace() = var_name.replace(oldvalue, newvalue, [count])
it will replace the old string with a new string specified in method argument. it won't modify original string, 
it will return a new string.
'''
# a = 'RRR'
# print(a.replace('R', 'S'))      #SSS
# print(a.replace('R', 'S', 1))   #SRR
# print(a.replace('R', 'S', 2))   #SSR
# print(a.replace('R', 'S', 0))   #RRR

# b = 'Good Morning'
# print(b.replace('o', '@'))      #G@@d M@rning
# print(b.replace('o', '@', 2))   #G@@d Morning

#############################################################################
'''split() = var_name.split(substring, [maxsplit=-1])
* Splits the string at the specified separator, and returns a list.
    – syntax : string.split([separator], [maxsplit])
* here both the arguments are optional , by default separator is single space , maxsplit
    is for all the separator present in the original string. 
'''
# a = 'she sells seashells on the seashore'
# print(a.split('e'))     #['sh', ' s', 'lls s', 'ash', 'lls on th', ' s', 'ashor', '']
# print(a.split('s'))     #['', 'he ', 'ell', ' ', 'ea', 'hell', ' on the ', 'ea', 'hore']
# print(a.split('e', maxsplit=3)) #['sh', ' s', 'lls s', 'ashells on the seashore']
# print(a.split('s', maxsplit=3))     #['', 'he ', 'ell', ' seashells on the seashore']
# print(a.split())        #['she', 'sells', 'seashells', 'on', 'the', 'seashore']

####################################################################################
'''12 July 2022'''
'''rsplit() = var_name.rsplit(substring, [maxsplit])
* Splits the string from the last at the specified separator, and returns a list.
* syntax: string.rsplit([separator], [maxsplit])
* There is no difference between split() and rsplit() if we did not mention
    maxsplit argument. Both will return the same outout for default maxsplit.
'''
# a = 'malayalam'
# print(a.split('a'))     #['m', 'l', 'y', 'l', 'm']
# print(a.rsplit('a'))    #['m', 'l', 'y', 'l', 'm']
# print(a.split('a', maxsplit=2))     #['m', 'l', 'yalam']
# print(a.rsplit('a', maxsplit=2))    #['malay', 'l', 'm']
# print(a.rsplit('m'))            #['', 'alayala', '']
#
# b = 'hello universe how are you'
# print(b.rsplit())   #['hello', 'universe', 'how', 'are', 'you']
#
# c = '007 James Bond'
# print(c.split(7))       #TypeError
# print(c.split('7'))         #['00', ' James Bond']
# print(c.split('9'))         #['007 James Bond'], since the substring is not present in the
##main string, it'll not throw any error, instead it'll give the entire string as a list element

###################################################################################
'''strip() = var_name.strip(substring)
* It’s an inbuilt method which strips the specified char from both the ends of
    original string.
* syntax: string.strip([characters])  New string
* Strip takes maximum 1 argument, i.e. characters to strip from string . Default
    value is whitespace. If no argument is passed then leading and trailing whitespaces
    in the original string is removed
'''
# a = '****hello******'
# print(a.strip('*'))     #hello
#
# b = '*!@#python *$^&*%'
# print(b.strip('*!@#$^&% '))     #python
# print(b.strip('*!#&^% '))       #@#python *$
#
# c = '     hello        '
# print(c.strip(' '))     #hello
# print(c.strip())        #hello
#
# c = '  *   hello   *  '
# print(c.strip())        #*   hello   *
# print(c.strip('*'))     #'  *   hello   *  '
#
'''lstrip() :
* lstrip() is also an inbuilt method, which have same syntax as strip() and also
    work same like strip, but only difference is it just removes the leading char
    only (not the trailing char).'''
# d = '  *   hello   *  '
# print(d.lstrip(' *'))       #'hello   *  '
#
# b = '*!@#python *$^&*%'
# print(b.lstrip('*!@#'))     #python *$^&*%

####################################################################################
'''rstrip()
* rstrip() is also an inbuilt method, which have same syntax as strip() and also
    work same like strip, but only difference is it just removes the trailing char
    only (not the leading char).
'''
# d = '  *   hello   *  '
# print(d.rstrip(' *'))       #'  *   hello'
#
# b = '*!@#python *$^&*%'
# print(b.rstrip('*!@#'))     #*!@#python *$^&*%
# print(b.rstrip('%*&^$!@#')) #*!@#python

############################################################################
'''partition() 
partition() : searches for a first occurance of specified string, and splits the
    string into a tuple containing three elements.
    Syntax : string.partition(value/substring)
        The first element contains the part before the specified string.
        The second element contains the specified string
        The third element contains the part after the string.
'''
# a = 'python'
# print(a.partition('t'))     #('py', 't', 'hon')
#
# b = 'exploration'
# print(b.partition('r'))     #('explo','r' , 'ation')
#
# c = 'malayalam'
# print(c.partition('a'))     #('m', 'a', 'layalam')

'''rpartition()
 This works similar to partition, but it will split at the last occurrence and
returns 3 element tuple where first element contains the first part of last
occurrence of specified value, second element is the specified value and third
element is the elements

 '''
# c = 'malayalam'
# print(c.rpartition('a'))    #('malayal', 'a', 'm')
#
# a = 'she sells seashells on the seashore'
# print(a.partition('sea'))   #('she sells ', 'sea', 'shells on the seashore')
# print(a.rpartition('sea'))  #('she sells seashells on the ', 'sea', 'shore')
######################################################################################
'''join() = 'string'.join(var_name)
*  It’s an inbuilt method which will join the elements of iterables (collection data
    type) with a specified string.
* Syntax: “string”.join(iterable)
* It takes only one argument and it’s a required argument.'''
# a = 'friends'
# print('*'.join(a))      #f*r*i*e*n*d*s
#
# b = ['sh', ' s', 'lls s', 'ash', 'lls on th', ' s', 'ashor', '']
# print('e'.join(b))      #she sells seashells on the seashore
#
# c = ['Hi', 'there', 'I', 'am', 'using', 'whatsapp']
# print('@'.join(c))      #Hi@there@I@am@using@whatsapp
#
# d = [1, 2, 3, 4]
# print('@'.join(d))  #TypeError, because the iterablles should contain strings as elements

###############################################################################
'''July 13 2022'''
'''isalpha() = var_name.isalpha()
 Returns True if all characters in the string are in the alphabet
'''
# a = 'hello'
# print(a.isalpha())      #True
# b = 'hello universe'
# print(b.isalpha())      #False, because space is there

############################################################################
'''isnumeric()/isdigit() = var_name.isnumeric() or var_name.isdigit()
 Returns True if all characters in the string are digits/numeric.
'''
# a = '1234321567876'
# print(a.isnumeric())        #True
# print(a.isdigit())          #True
#
# b = '1234  @ hai'
# print(b.isnumeric())        #False
# print(b.isdigit())          #False

################################################################################
'''isalnum = var_name.isalnum()
Returns True if all characters in the string are alphanumeric
'''
# a = 'python 1223'
# print(a.isalnum())      #False
# b = 'brooklynn999'
# print(b.isalnum())      #True
# c = 'brooklynn'
# print(c.isalnum())      #True
# d = '9876543'
# print(d.isalnum())      #True

############################################################################
'''islower() = var_name.islower()
Returns True if all alpha characters in the string are lower case
'''
# a = 'hello @12234'
# print(a.islower())      #True
# b = 'HEllO'
# print(b.islower())      #False

##############################################################################
'''isupper() = var_name.isupper()
Returns True if all alpha characters in the string are upper case.
'''
# a = 'NOBITA'
# print(a.isupper())      #True
# b = 'DoREMON'
# print(b.isupper())      #False

#########################################################################3
'''isspace() = var_name.isspace()
Returns True if all characters in the string are whitespaces
'''
# a = '                     '
# print(a.isspace())      #True
# b=' '
# print(b.isspace())      #False

#########################################################################
'''istitle() = var_name.istitle()
Returns True if the string follows the rules of a title
'''
# a = 'Alice@In Wonderland'
# print(a.istitle())      #True
#
# b = 'alice in wonderland'
# print(b.istitle())      #False

##################################################################################
'''LISTS
* Collection of homogenous or heterogeneous data.
* Separated by comma.
* Elements in the lists are ordered.
* Lists can hold duplicate elements
* It is a mutable type
* Boundary: […….]
* Syntax: var_name = [ele1, ele2, ele3, ele4……]
* Length of a list: len(var_name)
'''
#########################################################################
'''Different ways to construct a list object:
* my_list = [ ]
* my_list = list( )'''
# a = 'hai'
# print(list(a))      #['h', 'a', 'i']
#
# b = 1234
# print(list(b))      #TypeError: 'int' object is not iterable
#
# c = [10, 20, 2.3, 4+0j, True]
# print(list(c))      #[10, 20, 2.3, (4+0j), True]
'''
Indexing a list:
* This is a process of extracting single element at a time.
* Indexing can be positive(Starts with 0) or negative(starts with -1)
 Syntax: var_name[index number]


Slicing a list:
* Process of extracting multiple elements at a time/simultaneously
* Syntax: var_name[start index : end index : step value]
    Start index : default value = 0
    End index : default value = len(var_name)
    Step value : defa5ult value : 1(Optional)

NOTE : Element at the end index will not be added in the slice.
'''

##################################################################################
'''14 July 2022'''
'''
Immutable:
* Immutable object can’t be changed or modified once after it is created.
    In other words it’s the ability of the data type which hold the values as it its
    once after it is created

Mutable:
* Mutable objects can be modified or changed even after it is created.
* In other words it’s the ability of the data type which allows its values to be
    changed even after created.
* In mutable data type if we make any changes in values, adding element, removing
    element etc. it is reflected in the original object.
'''
#########################################################################
'''assigning the values through indexing'''
# a = ['friends', 'blue', 82, '50', 50, 'riverdale', 'suits', '1.75', 'himym']
# print(a[1])     #blue
# print(a[6])     #suits
# a[3] = 'abc'
# print(a)    #['friends', 'blue', 82, 'abc', 50, 'riverdale', 'suits', '1.75', 'himym']. here the original list gets modified

################################################################################
# a = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'orange', 'white']
# print(a[0])     #red
# print(a[0][2])  #d
# print(a[3][4])  #o
#
# a = ['nexon', 'bmw', 'audi', 'ertiga', 'jaguar', 'verna', 'hondacity', 'seltos', ['ritz', 'alto']]
# print(a[8])     #['ritz', 'alto']
# print(a[8][0])  #ritz
# print(a[8][0][1])       #i
###############################################################################
# a = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'orange', 'white']
# print(a[0][1])      #e
# print(a[1][3])      #e
#
# print(id(a[0][1]))  #2281735097392
# print(id(a[1][3]))  #2281735097392
##############################################################################
'''merging of two lists'''
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# print(a + b)    #[1, 2, 3, 4, 5, 6, 7, 8]
# a = a + b
# print(a)        #[1, 2, 3, 4, 5, 6, 7, 8]
# b = a + b
# print(b)    #[1, 2, 3, 4, 5, 6, 7, 8, 5, 6, 7, 8]
#
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# c = [*a, *b]
# print(c)        #[1, 2, 3, 4, 5, 6, 7, 8]

####################################################################################
'''LIST METHODS'''
'''adding the elements to a list'''
'''append() = var_name.append(element)
* Adds an element at the end of the list.
* Elements can be of any data type '''
# a = ['nexon', 'bmw', 'audi', 'ertiga', 'jaguar', 'verna', 'hondacity']
# print(a.append('seltos'))       #None
# print(a)    #['nexon', 'bmw', 'audi', 'ertiga', 'jaguar', 'verna', 'hondacity', 'seltos']
# a.append('ritz', 'alto')    #TypeError: list.append() takes exactly one argument (2 given)
# a.append(['ritz', 'alto'])
# print(a)    #['nexon', 'bmw', 'audi', 'ertiga', 'jaguar', 'verna', 'hondacity', 'seltos', ['ritz', 'alto']]

######################################################################################
'''extend() = var_name.extend(iterable)
Extends the existing list with the items of the given sequence.'''
# a = ['apple', 'grapes', 'plum', 'pomegranate', 'kiwi', 'mango']
# print(a.extend(['orange', 'guava', 'banana', 'avocado']))   #None
# print(a)    #['apple', 'grapes', 'plum', 'pomegranate', 'kiwi', 'mango', 'orange', 'guava', 'banana', 'avocado']
#
# a = ['pen', 'pencil']
# a.extend('book')
# print(a)        #['pen', 'pencil', 'b', 'o', 'o', 'k']
# a.extend(10) #TypeError, Cannot pass individual datatypes. Only collections


###############################################################################
'''July 15 2022'''
'''insert() = var_name.insert(position, element)
Adds an element at the specified position.
'''
# a = ['mon', 'tues', 'wed', 'thur', 'fri']
# print(a.insert(2, 'sat'))       #None
# print(a)        #['mon', 'tues', 'sat', 'wed', 'thur', 'fri']
# # a.insert('sun')     #TypeError, Both position and the element are mandatory paratemeters
# a.insert(-1, 'sun')
# print(a)        #['mon', 'tues', 'sat', 'wed', 'thur', 'sun', 'fri']
# a.insert(100, 'jan')
# print(a)    #['mon', 'tues', 'sat', 'wed', 'thur', 'sun', 'fri', 'jan']

#########################################################################################
'''Removing the elements from the list'''
'''pop() = 
* Removes the element at the specified position.
* Syntax: var_name.pop([position])
    i. By default pop() removes and returns the last element in the list.
    ii. Returns removed value
'''
# a = ['jan', 'feb', 'mar', 'april', 'may', 'june', 'july', 'aug']
# print(a.pop(3))     #april, pop returns the deleted element
# print(a)            #['jan', 'feb', 'mar', 'may', 'june', 'july', 'aug']
# print(a.pop())          #aug
# print(a)            #['jan', 'feb', 'mar', 'april', 'may', 'june', 'july']
# print(a.pop(100))       #IndexError: pop index out of range
# print(a.pop(-1))        #aug

##########################################################################################
'''remove() : var_name.remove(element)
* Removes the first occurrence of the element specified
'''
# a = ['jan', 'feb', 'mar', 'april', 'may', 'june', 'july', 'aug']
# print(a.remove('may'))      #None
# print(a)        #['jan', 'feb', 'mar', 'april', 'june', 'july', 'aug']
#
# a = ['jan', 'feb', 'mar', 'april', 'may', 'june', 'july', 'aug', 'may']
# print(a.remove('may'))      #None
# print(a)    #['jan', 'feb', 'mar', 'april', 'june', 'july', 'aug', 'may'].
'''Incase we are truing to remove the duplicated elements from the list, remove method will
remove only the first occurance of the element specified'''

#######################################################################################
'''del : It is a keyword to deallocate the memory in an iterable'''
# a = ['jan', 'feb', 'mar', 'april', 'may', 'june', 'july', 'aug', 'may']
# del a[0]
# print(a)        #['feb', 'mar', 'april', 'may', 'june', 'july', 'aug', 'may']
#
# del a[2:6]
# print(a)        #['feb', 'mar', 'aug', 'may']
#
# del a[::2]
# print(a)        #['feb', 'april', 'june', 'aug']
#
# del a[::-2]
# print(a)        #['feb', 'april', 'june', 'aug']

#####################################################################################
'''count() = var_name.count(element)
It gives the number of occurances of a specified element in the list
'''
# a = [1, 2, 3, 1, 2, 4, 5, 3, 6, 2, 3, 7, 1, 8, 2, 3, 2, 9, 3, 0, 3]
# print(a.count(3))       #6
# print(a.count(2))       #5

####################################################################################
'''index() = var_name.index(element)
Returns the index of the first element with the specified value.
'''
# a = ['fastrack', 'gucci', 'wildcraft', 'zara', 'prada', 'puma', 'gucci', 'zara']
# print(a.index('zara'))      #3
# print(a.index('gucci'))     #1

####################################################################################
'''reverse() = var_name.reverse()
* It reverses the original list irrespective of the order.
* The list can either be homogenous list or heterogenous list.
* Modifies the original list.
'''
# a = ['fastrack', 'gucci', 'wildcraft', 'zara', 'prada', 'puma', 'gucci', 'zara']
# print(a[::-1])      #['zara', 'gucci', 'puma', 'prada', 'zara', 'wildcraft', 'gucci', 'fastrack']
# print(a.reverse())      #None
# print(a)        #['zara', 'gucci', 'puma', 'prada', 'zara', 'wildcraft', 'gucci', 'fastrack']
'''
NOTE : We can reverse the list using two syntaxes.
i) Slicing[ : : -1]
ii) Reverse method
The main difference between these two is that slicing will not modify the original
list but gives a new list in reverse order, whereas reverse method will reverse the
original list itself.
'''
###############################################################################################
'''sort() = var_name.sort([reverse=False], [key])
* In order to sort, the list should be homogenous.
* Modifies the original list itself  returns None
'''
# a = [9, 3, 7, 1, 2, 5, 8, 4]
# print(a.sort())     #None
# print(a)        #[1, 2, 3, 4, 5, 7, 8, 9]
# a.sort(reverse=True)
# print(a)        #[9, 8, 7, 5, 4, 3, 2, 1]
#
# b = ['praveen', 'nandhini', 'vijay', 'mukesh', 'anurag', 'smita', 'archana', 'radhika']
# b.sort()
# print(b)     #['anurag', 'archana', 'mukesh', 'nandhini', 'praveen', 'radhika', 'smita', 'vijay']
# b.sort(reverse=True)
# print(b)    #['vijay', 'smita', 'radhika', 'praveen', 'nandhini', 'mukesh', 'archana', 'anurag']
# b.sort(key=len)
# print(b)     #['vijay', 'smita', 'mukesh', 'anurag', 'praveen', 'archana', 'radhika', 'nandhini']
# b.sort(reverse=True, key=len)
# print(b)
#
# b = ['praveen', 'nandhini', 'Vijay', 'mukesh', 'anurag', 'smita', 'archana', 'radhika']
# b.sort()
# print(b)    #['Vijay', 'anurag', 'archana', 'mukesh', 'nandhini', 'praveen', 'radhika', 'smita']

############################################################################################
'''July 18 2022'''

'''Shallow copy  
* A Shallow copy constructs a new compound object and then inserts
    references to it. If a list has a nested list then the nested list will be shared by both
    original as well as copied list.
Shallow copy can be done by using slicing syntax or copy method.
'''
# a = [1, 2, 3, [4, 5]]
# b = a[:]
# print(b)        #[1, 2, 3, [4, 5]]
# a[3][0] = 400
# print(a)        #[1, 2, 3, [400, 5]]
# print(b)        #[1, 2, 3, [400, 5]]

'''deepcopy
Deepcopy copies everything and stores it in different memory location, that
    means the changes made in the original object will not be reflected in the copied object
'''
# from copy import deepcopy
# a = [1, 2, 3, [4, 5]]
# b = deepcopy(a)
# print(b)        #[1, 2, 3, [4, 5]]
# a[3][0] = 400
# print(a)        #[1, 2, 3, [400, 5]]
# print(b)        #[1, 2, 3, [4, 5]]

'''copy = var_name.copy()
 Returns a copy of the list.
* It follows Shallow copy principle
* The memory allocation will be different for both references
* If there is a nested copy in the list then it has same memory location for both references.'''
# a = [1, 2, 3, [4, 5]]
# b = a.copy()
# print(b)        #[1, 2, 3, [4, 5]]
# a[3][0] = 400
# print(a)        #[1, 2, 3, [400, 5]]
# print(b)        #[1, 2, 3, [400, 5]]
###############################################################################################
'''Converting list to a string'''
# s = 'hello'
# print(list(s))          #['h', 'e', 'l', 'l', 'o']
# print(s.split())        #['hello']
# print(''.join(['h', 'e', 'l', 'l', 'o']))       #hello
# print(' '.join(['h', 'e', 'l', 'l', 'o']))      #h e l l o
# print(''.join(['hello']))       #hello
#
# a = 'hello world'
# print(list(a))      #['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# print(a.split())    #['hello', 'world']
# print(''.join(['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'])) #hello world
# print(''.join(['hello', 'world']))      #helloworld
# print(' '.join(['hello', 'world']))     #hello world

##########################################################################################
'''Tuple
* Collection of homogenous or heterogeneous data.
* Separated by comma.
* Elements in the tuples are ordered.
* Tuples can hold duplicate elements
* It is an immutable type
* tuple() is used as a constructor to create tuple elements
* Boundary: (…….)
* Syntax: var_name = (ele1, ele2, ele3, ele4……)
'''
'''Ways to create tuple:'''
# t = ()
# print(type(t))      #<class 'tuple'>
# t1 = tuple()

'''single element tuple'''
# t = (10)
# print(type(t))
# t1 = (10,)
# print(type(t1))     #<class 'tuple'>

########################################################################################
'''
Indexing:
    This is a process of extracting single element at a time.
    Indexing can be positive(Starts with 0) or negative(starts with -1)
        Syntax: var_name[index number]

Slicing a tuple:
    Process of extracting multiple elements at a time/simultaneously
    Syntax: var_name[start index : end index : step value] 
'''
# a = (10, 1.25, 'hello', True, 49)       #(10, 1.25)
# print(a[0:2])       #(10, 1.25)
# print(a[-5:-3])     #(10, 1.25)
# print(a[0:-3])      #(10, 1.25)
# print(a[-5:2])      #(10, 1.25)

#####################################################################################
'''
NOTE : Tuples are more memory efficient than lists. Since lists are of mutable, there
will be some memory reserved in case if we want to add elements to the list. But tuples
are immutable, there will be no memory reserved as there is no addition of data to the
tuples.
'''
#####################################################################################
'''Tuple Methods'''
'''count() = var_name.count(element)'''
# a = ('hai', 10, 'hai', 20, True, False, 0, 'hai')
# print(a.count('hai'))       #3

'''index() = var_name.index(element, [start], [end])'''
# a = ('hai', 10, 'hai', 20, True, False, 0, 'hai')
# print(a.index(10))      #1
# print(a.index('hai', 1, 4))     #2
###################################################################################
# a = (1, 2, 3)
# b = (4, 5, 6)
# print(a + b)        #(1, 2, 3, 4, 5, 6)
'''Here, either tuple a or b is not getting modified, whatever the operations takes place,
that takes place in some temporary memory,, the original tuples will never get affected. '''
######################################################################################
'''NOTE : '''
# a  = (1, 2, 3, 4, 5)
# b = list(a)     #[1, 2, 3, 4, 5]
# b.append(6)
# print(b)        #[1, 2, 3, 4, 5, 6]
# c = tuple(b)        #(1, 2, 3, 4, 5, 6)
# print(c)

###############################################################################################
'''July 19 2022'''
'''sets
* Sets are unordered
* Elements inside the sets are unique[Duplication Not Allowed]
* Sets are mutable, but elements inside the set must be hashable
* Sets cannot be indexed or sliced
* Python Sets can only include hashable objects[Immutable]
* Boundary : {  ,  ,  ,  }
* Syntax: var_name = {ele1, ele2, ele3, …}
* Empty Set is represented by set()	→ [default value].
'''

'''
Hashable objects:  Hashable objects are the objects which returns a value when we applied a 
hash() function on it. 
Only immutable objects will have hash values, hence hash() can be used to check the mutability
and immutability of the objects 
'''
# a = {10, '10', True, 'hai', False, 7.8, [6-9j, 10, False]}
# print(a)        #TypeError: unhashable type: 'list'
#
# a = {10, '10', True, 'hai', False, 7.8, 6-9j}
# print(hash(a))    #TypeError: unhashable type: 'set'

##########################################################################################
# print(hash(True))       #1
# print(hash(False))      #0
# print(hash(1))          #1
# print(hash(0))          #0
#
# a = {10, True, 0, 'hai', False, 1, 7.0}
# print(a)
###########################################################################################
'''set methods'''
'''union() = baseset.union(set1, set2, set3, set4,...) --> New set
Returns a set that contains all items from the original set, and all items from the reference sets.'''
# a = {1, 2, 3, 4, 5, 6}
# b = {2, 4, 6, 8, 10}
# c = {10, 20, 30}
# print(a.union(b))       #{1, 2, 3, 4, 5, 6, 8, 10}
# print(a.union(b, c))    #{1, 2, 3, 4, 5, 6, 8, 10, 20, 30}
######################################################################################
'''update() = baseset.update(set1, set2, set3,...) --> None
 updates the base set with the elements present in the reference sets.'''
# a = {1, 2, 3, 4, 5, 6}
# b = {2, 4, 6, 8, 10}
# c = {10, 20, 30}
# print(a.update(b))      #None
# print(a)        #{1, 2, 3, 4, 5, 6, 8, 10}
# print(b.update(a, c))       #None
# print(b)        #{1, 2, 3, 4, 5, 6, 8, 10, 20, 30}

######################################################################################
'''intersection() = baseset.intersection(set1, set2,...) --> New set
Returns a set that contains the similar elements(common elements) between two or more sets.
'''
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# b = {2, 4, 6, 8, 10}
# c = {1 ,3 ,5 ,7 ,9}
# print(a.intersection(b))        #{8, 2, 4, 6}
# print(a.intersection(c))        #{1, 3, 5, 7, 9}
# print(b.intersection(c))        #set()
# print(a.intersection(b, c))     #set()

########################################################################################
'''intersection_update = baseset.intersection_update(set1, set2,...) --> None
updates the base set with intersection property'''
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# b = 8on_update(b))     #None
# print(a)            #{8, 2, 4, 6}, now the value of set a is {2, 4, 6, 8}
# print(a.intersection_update(c))     #since a = {2, 4, 6, 8} and c = {1, 3, 5, 7, 9}, no common elements
# print(a)

# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# b = {2, 4, 6, 8, 10}
# c = {1 ,3 ,5 ,7 ,9, 2}
# print(a.intersection_update(b, c))      #None
# print(a)        #{2}

#######################################################################################
'''difference() = baseset.difference(set) --> New set
Returns set contains items that exist only in the base set, but not in other sets.
'''
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# b = {2, 4, 6, 8, 10}
# c = {1 ,3 ,5 ,7 ,9}
# print(a.difference(b))      #{1, 3, 5, 7, 9}
# print(b.difference(a))      #{10}
# print(a.difference(c))      #{8, 2, 4, 6}
# print(b.difference(c))      #{2, 4, 6, 8, 10}
# print(a.difference(b, c))   #set()

##########################################################################################
'''difference_update() = baseset.difference_update(set) --> None
updates the base set with the elements that are present in base set but not in other set.
(updates base set with difference property).'''
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# b = {2, 4, 6, 8, 10}
# c = {1 ,3 ,5 ,7 ,9}
# print(a.difference_update(b))       #None
# print(a)        #{1, 3, 5, 7, 9}
# a.difference_update(c)
# print(a)            #{2, 4, 6, 8}
#  b.difference_update(a, c)
# print(b)            #{10}
###########################################################################################
'''symmetric difference : base_set.symmetric_difference(arg set) ⇒ New set
returns a set that contains all items that are not common among both the sets.
'''
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# b = {2, 4, 6, 8, 10}
# c = {1 ,3 ,5 ,7 ,9, 11, 13}
# print(a.symmetric_difference(b))        #{1, 3, 5, 7, 9, 10}
# print(a.symmetric_difference(c))        #{2, 4, 6, 8, 11, 13}
# print(a.symmetric_difference(b , c))        #TypeError: set.symmetric_difference() takes exactly one argument
# print(b.symmetric_difference(c))    #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13}

############################################################################################
'''symmetric_difference_update : base_set.symmetric_difference_update(arg set) ⇒ None
updates the base set with the items that are not common among both the sets.
'''
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# b = {2, 4, 6, 8, 10}
# c = {1 ,3 ,5 ,7 ,9, 11, 13}
# print(a.symmetric_difference_update(b))     #None
# print(a)        #{1, 3, 5, 7, 9, 10}
# print(b.symmetric_difference_update(c))
# print(b)        #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13}

#############################################################################################
'''20 July 2022'''
'''Note : The elements of the sets are generally referred as keys. '''

'''add() = set_name.add(element)
This method adds an element to the set. If the element already exists, this
method does not add the element.
It takes exactly one argument, so u can add one element at a time.

Note : The element must be immutable datatype , because elements of sets has to hash
values. 
'''
# a = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
# print(a.add('saturday'))        #None
# print(a)    #{'monday', 'thursday', 'friday', 'tuesday', 'saturday', 'wednesday'}
# print(a.add('sunday', 'january')) #TypeError, add takes only one argument
# a.add('monday'), #if we add the element which is already present, it'll not throw any error.
# print(a)
###########################################################################################
'''remove() = set_name.remove(element)
Removes the specified element from the set. Raises an error if element is not
present.
It takes exactly one argument, so u can remove one element at a time
'''
# a = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
# print(a.remove('wednesday'))        #None
# print(a)    #{'monday', 'saturday', 'thursday', 'tuesday', 'friday', 'sunday'}
# a.remove('december')        #KeyError
# a.remove('tuesday', 'monday')       #TypeError, can only remove one element

#######################################################################################
'''discard() : set_name.discard(element)
Removes the specified element from the set. If element is not present, it doesn’t
give error like remove() method.
It takes exactly one argument, so u can remove one element at a time
'''
# a = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
# print(a.discard('sunday'))      #None
# print(a)        #{'saturday', 'thursday', 'monday', 'wednesday', 'tuesday', 'friday'}
# a.discard('december')
# print(a)        #{'monday', 'wednesday', 'saturday', 'tuesday', 'thursday', 'friday'}

###########################################################################################
'''pop() = var_name.pop()
This method removes a random element from a set and returns that removed
element. If the set is empty then it will returns KeyError.
It takes no arguments or parameter'''
# a = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
# print(a.pop())  #monday
# print(a)
# print(a.pop())
# print(a.pop('wednesday'))   #TypeError
#nb
# b = set()
# b.pop()     #KeyError: 'pop from an empty set'
###########################################################################################
'''issubset = set1.issubset(set2)
Returns True if all the items in the baseset exists in the reference set,
otherwise returns False
It takes exactly one argument or parameter.'''
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# b = {2, 4, 6, 8}
# c = {1, 3, 5, 7, 9}
# print(b.issubset(a))        #True
# print(a.issubset(b))        #False
# print(c.issubset(a))        #True
# print(a.issubset(a))        #True

#######################################################################################
'''superset() = set1.issuperset(set2)
Returns True if all items in the specified set exists in the baseset, otherwise
it returns False.
It takes exactly one argument or parameter'''
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# b = {2, 4, 6, 8}
# c = {1, 3, 5, 7, 9}
# print(a.issuperset(b))      #True
# print(b.issuperset(c))      #False
# print(a.issuperset(c))      #True
########################################################################################
'''isdisjoint() = set1.isdisjoint(set2)
Returns True if None of the items are present in both sets, otherwise it
returns False. i.e. There shouldn’t be any common element between baseset and
argument set.
It takes exactly one argument or parameter.
NOTE : x.isdisjoint(y) and y.isdisjoint(x) both will return the same .'''
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# b = {2, 4, 6, 8}
# c = {1, 3, 5, 7, 9}
# d = {10, 20, 30}
# print(a.isdisjoint(d))      #True
# print(b.isdisjoint(c))      #True
# print(c.isdisjoint(a))      #False

##########################################################################################
'''clear() = set_name.clear()
Removes all the elements from the set. It takes no argument.
'''
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(id(a))
# print(a.clear())        #None
# print(a)        #set()
# print(id(a))

###########################################################################################
'''Dictionary
* Collection of key value pairs, Each element is considered as a key : value pair.
* Each element in dictionary is separated by comma operator.
* Boundary: { key1:value1, key2:value2, …}
* Syntax : var_name = { key1:value1, key2:value2, …}
* Length : returns the number of keys present in the dictionary, len(var_name)
* It does not support indexing/slicing.
* Keys should be unique in dictionary, but values can be repeated.
* Keys should be of immutable datatype, but values can be of any datatype.
* It doesn’t support indexing/slicing.
* Empty dictionary (default value) : { }
'''
#######################################################################################
'''accessing the values'''
# d = {c}
# print(d)
# print(d['karnataka'])       #kannada
# print(d['kerala'])          #malayalam
# print(d['maharashtra'])     #KeyError

#######################################################################################
# d = {'jan':31, 'feb':28, 'mar':31, 'april':30, 'may':31, 'feb':29}
# print(d)    #{'jan': 31, 'feb': 29, 'mar': 31, 'april': 30, 'may': 31},
'''if the keys are duplicated, the latest updated value will be considered for the key'''

#############################################################################################
'''
1 ) What is the major advantage of using a tuple over a list?
2 ) create a single value tuple
3) The output of following is
	a = (1, 2, 3, 4)
	b = (5, 6, 7, 8)
	print(c = (*a , *b))

4) Output of: t = [1, 2, 3, 4, ["hai", "hello", 23], "python"]
	 t[4][0][-1] = “y” 
             print(t)
6. What is the output of the following
	a = [1, 2, 3]
	b = [4, 5, 6]
	print([a, b])
	print((a, b))
1. Difference between pop, remove and discard
2. difference between difference and symmetric difference method
3. what is the output of 
        a = {'apple', 'google', 'facebook'}
        a.add({'instagram'})
4. Output of
        s = {1, 2, 3, 4, 5, 6}
        s.add([10, 20]). Justify your answer
        s.add(1, 2, 3)
'''

#################################################################################################
'''21 July 2022'''
'''
Characteristics of key and values:
* keys can not be duplicated.
* Keys will be a single element
* Values can be of any datatype
* Values can be accessed through keys only
* Keys must be of immutable datatype or hashable
'''

'''Different ways of creating a dictionary'''
# d = dict()      #Empty dictionary,{}
# print(d)
#
# d = {}      #Empty  dictionary
#
# d = dict(Bangalore=25, Mysore=35, Shimoga=40)
# print(d)        #{'Bangalore': 25, 'Mysore': 35, 'Shimoga': 40}
#
# d = dict([('bangalore', 25), ('mysore', 35), ('Shimoga', 40)])
# print(d)        #{'bangalore': 25, 'mysore': 35, 'Shimoga': 40}
#
# d = dict((('bangalore', 25), ('mysore', 35), ('Shimoga', 40)))
# print(d)        #{'bangalore': 25, 'mysore': 35, 'Shimoga': 40}

##########################################################################################
'''creating keys and values in a dictionary'''
# d = {}
# d['harry potter'] = 'JK Rowling'
# print(d)        #{'harry potter': 'JK Rowling'}
# d['the Alchemist'] = 'Paulo Coelho'
# d['Wings of fire'] = 'APJ Adbul Kalam'
# print(d)        #{'harry potter': 'JK Rowling', 'the Alchemist': 'Paulo Coelho', 'Wings of fire': 'APJ Adbul Kalam'}

###########################################################################################
'''composite 1`` : If we give tuples as keys. '''
# d = {}
# d[(15, 'Aug')] = 'Independence day'
# print(d)        #{(15, 'Aug'): 'Independence day'}

############################################################################################
'''Accessing values from a dictionary
Syntax : var_name[key]
'''
# d = {'Harry Potter':'JK Rowling', 'The Alchemist':'Paulo Coelho', 'Wings of fire':'Abdul Kalam', 'three thousand stiches':'SudhaMurthy'}
# print(d['Harry Potter'])    #JK RowlingJK Rowling
# print(d['three thousand stiches'])      #SudhaMurthy
# print(d['five point someone'])      #KeyError

##############################################################################################
'''Dictionary methods'''
'''get() = var_name.get(keyname, [defaultvalue=None])
Its an inbuilt method which returns the value of a specified key. If specified
key is not present, it won’t give us an error, instead it will return the second argument
as value
Default value of second argument is None.'''

# d = {'ITC':280, 'Bhartiairtel':650, 'Idea':8, 'JSWenergy':300, 'adaniports':3000, 'mrf':80000}
# print(d.get('Idea'))        #8
# print(d.get('adaniports'))  #3000
# print(d.get('Hikal'))       #None
# print(d.get('Hikal', 'Key not found'))      #Key not found
# print(d)    #{'ITC': 280, 'Bhartiairtel': 650, 'Idea': 8, 'JSWenergy': 300, 'adaniports': 3000, 'mrf': 80000}

'''This method will never modify the original dictionary'''
##############################################################################################
'''keys() = var_name.keys()
Returns a view object which contains list of all the keys.'''
# d = {'ITC':280, 'Bhartiairtel':650, 'Idea':8, 'JSWenergy':300, 'adaniports':3000, 'mrf':80000}
# print(d.keys())     #dict_keys(['ITC', 'Bhartiairtel', 'Idea', 'JSWenergy', 'adaniports', 'mrf'])

#############################################################################################
'''values() = var_name.values()
Returns a view object which contains list of all the values.'''
#d = {'ITC':280, 'Bhartiairtel':650, 'Idea':8, 'JSWenergy':300, 'adaniports':3000, 'mrf':80000}
# print(d.values())       #dict_values([280, 650, 8, 300, 3000, 80000])

#############################################################################################
'''items() = var_name.items()
Returns a view object which contains key-value pairs of the dictionary as tuples
in list.'''
# d = {'ITC':280, 'Bhartiairtel':650, 'Idea':8, 'JSWenergy':300, 'adaniports':3000, 'mrf':80000}
# print(d.items())

################################################################################################
'''setdefault() = var_name.setdefault(key, [value=None])
Its adds the key value pair if the key is not present and returns the specified
value, If the key is already present it won’t change anything and returns the existing
value of key.'''
#
# print(d.setdefault('IRB'))      #None
# print(d)        #{'ITC': 280, 'Bhartiairtel': 650, 'Idea': 8, 'JSWenergy': 300, 'IRB': None}
# d.setdefault('fretail', 10)
# print(d)    #{'ITC': 280, 'Bhartiairtel': 650, 'Idea': 8, 'JSWenergy': 300, 'IRB': None, 'fretail': 10}
# d.setdefault('ITC', 500)
# print(d)    #{'ITC': 280, 'Bhartiairtel': 650, 'Idea': 8, 'JSWenergy': 300, 'IRB': None, 'fretail': 10}

#############################################################################################
'''update() = var_name.update(iterable)
updates the existing dictionary with specified iterable.'''
# d = {'name':'Ram', 'empid':1234, 'salary':10000}
# print(d.update({'place':'bangalore', 'bonus':2000}))  #Nnne
# print(d)    #{'name': 'Ram', 'empid': 1234, 'salary': 10000, 'place': 'bangalore', 'bonus': 2000}
# d.update({'salary':20000})
# print(d)        #{'name': 'Ram', 'empid': 1234, 'salary': 20000}
# d.update([('PAN', 'abcd1234'), ('adhar', 1234567890)])
# print(d)    #{'name': 'Ram', 'empid': 1234, 'salary': 10000, 'PAN': 'abcd1234', 'adhar': 1234567890}
# d.update((('PAN', 'abcd1234'), ('adhar', 1234567890)))
# print(d)    #{'name': 'Ram', 'empid': 1234, 'salary': 10000, 'PAN': 'abcd1234', 'adhar': 1234567890}
#c
# print(d)    #{'name': 'Ram', 'empid': 1234, 'salary': 10000, ('hello', 5): 10}

################################################################################################
'''fromkeys() = dict.fromkeys(iterable, [value])
Returns a dictionary with the specified keys(element of iterable) and the
specified value.
Here elements of iterable are considered as keys of new dictionary (so they should be
immutable . and whatever the value specified in second argument is considered as value
for all the keys. By default value will be None.
'''
# a = 'python'
# print(dict.fromkeys(a)) #{'p': None, 'y': None, 't': None, 'h': None, 'o': None, 'n': None}
# print(dict.fromkeys(a, 1000))   #{'p': 1000, 'y': 1000, 't': 1000, 'h': 1000, 'o': 1000, 'n': 1000}
#
# b = [1, 2, 3, 4, 5]
# print(dict.fromkeys(b)) #{1: None, 2: None, 3: None, 4: None, 5: None}
# print(dict.fromkeys(b, 200))        #{1: 200, 2: 200, 3: 200, 4: 200, 5: 200}

##################################################################################################
'''pop() = var_name.pop(key, [value])
Removes the specified key from the dictionary and returns value of that key.
'''
# d = {'name': 'Ram', 'empid': 1234, 'salary': 10000, 'PAN': 'abcd1234', 'adhar': 1234567890}
# print(d.pop('PAN'))     #abcd1234
# print(d)        #{'name': 'Ram', 'empid': 1234, 'salary': 10000, 'adhar': 1234567890}
# print(d.pop())  #TypeError. Key is the mandatory parameter
# print(d.pop('place'))   #KeyError
# print(d.pop('place', 'key not found'))      #key not found
####################################################################################################
'''popitem() = var_name.popitem()
removes the key value pair that was inserted at last into the dicrionary. It
returns the removed key, value pair as tuple.'''
# d = {'name': 'Ram', 'empid': 1234, 'salary': 10000, 'PAN': 'abcd1234', 'adhar': 1234567890}
# print(d.popitem())      #('adhar', 1234567890)
# print(d)    #{'name': 'Ram', 'empid': 1234, 'salary': 10000, 'PAN': 'abcd1234'}
################################################################################################
'''merging two dictionaries'''
# d1 = {'one':1, 'two':2, 'three':3}
# d2 = {1:'one', 2:'two', 3:'three'}
# d3 = {**d1, **d2}
# print(d3)       #{'one': 1, 'two': 2, 'three': 3, 1: 'one', 2: 'two', 3: 'three'}
#
# d3 = d1 | d2
# print(d3)   #{'one': 1, 'two': 2, 'three': 3, 1: 'one', 2: 'two', 3: 'three'}

################################################################################################
'''July 22 2022'''
'''some inbuiltt functions'''
'''abs() : Gives the absolute value'''
# print(abs(-9))      #9
# print(abs(-8.9))    #8.9

###############################################################################
'''round() = rounds off the value
Syntax : round(number, precision)
'''
# a = 1.2345
# print(round(a))     #1
# print(round(9.98))  #10
# print(round(1.234567, 4))       #1.2346

##############################################################################
'''trunc()'''
# import math
# print(math.trunc(5.89))     #5
# print(math.trunc(1.2345))   #1

#################################################################################
'''Operators
i. Arithmatic operators
ii. Assignment operator
iii. Comparison/Relational Operator
iv. Logical Operator
v. Bitwise Operator
vi. Identity Opeartor
vii. Membership operator
'''

'''Arithmatic Operator'''
'''Addition = +
Performs addition operation
'''
# print(4 + 7)        #11
# print(1.1 + 2.2)        #3.3
# print(8+9j + 7+6j)      #15+15j
# print(True + True)      #2
# print('hai'+'python')   #haipython, concatenation takes place
# print(3 + 'hai')        #TypeError
# print([1, 2, 3] + [1, 2, 3])    #[1, 2, 3, 1, 2, 3], Merge into a single list
# print((1, 2, 3) + (4, 5, 6))    #(1, 2, 3, 4, 5, 6), Merge into a single tuple
# print({1, 2, 3} + {4, 5, 6})    #TypeError. Sets donot support addition operation
# print({1:11, 2:22, 3:33} + {4:44, 5:55, 6:66})  #TypeError. dict donot support addition operation

###########################################################################################
'''Subtraction : Performs subtracction operation ( - )'''
# print('hai' - 'h')
# print([1, 2, 3] - {2, 3})
# print((1, 2, 3) - (2, 3))
# print({1, 2, 3, 4} - {2, 4, 6})     #{1, 3}. Subtraction operation acts as a differene method
# print({1:1, 2:2}-{1:1})     #TypeError
'''NOTE: Only Sets support subtraction operation, Other collection datatypes donot support'''
#######################################################################################
'''Multiplication : *
Performs multiplicaton operation'''
# print('hai' * 'h')      #TypeError
# print('hai' * 3)    #haihaihai
# print([1, 2] * 2)   #[1, 2, 1, 2]
# print((1, 2) * 2)   #(1, 2, 1, 2)
# print({1, 2} * 2)   #TypeError
# print({1:1, 2:2} * 2)   #TypeError
###########################################################################################
'''Division'''
'''NOTE : Only Individual datatypes support Division operation, none of the collection datatypes 
support division'''
################################################################################################
'''Modulus = % 
It will perform the division operation only once and it will return the remainder.
Applicable only for the individual datatypes'''
# print(7 % 2)        #1
# print(11 % 4)       #3
###########################################################################################
'''floor : Performs division operation and rounds off the quotient to the nearest value'''
# print(8 // 3)
# print(15//8)
###########################################################################################
'''exponent ( ** )'''
# print(2 ** 3)       #8
# print(3 ** 4)       #81
################################################################################################
'''Relational Operator/Comparison'''
'''Greater than(>)'''
# print(8 > 4)    #True
# print(7 > 9)    #False
# print('python'>'java')      #True, It'll check the ASCII values of the first character
# print('hello' > 'hey')      #False
# print([1, 2, 3] > [2, 4])   #False, Check the first character
# print('hai' > 23)       #TypeError. Cannot compare strings with numbers
############################################################################################
'''greater than or equal to(>=) :
Returnns True if right operand is either greater than or equal to left operand'''
# print(2 > 2)    #False
# print(2 >= 2)   #True

##############################################################################################
'''less than'''
# print('hello' < 'hey')      #True
# print([1, 2, 3] <= [2, 3])  #True

######################################################################################
'''lessthan or equal to : Returns True if left operand is either greater than or equal to right operand'''
# print([1, 2, 3] <= [1, 3])      #True

#####################################################################################
'''equal to ( == ) : Checks if the left operand and right operand are same'''
# print(4 == 4)       #True
# print('hai' == 'hi')    #False

################################################################################################3
'''Not equal to( != )'''
# print(4 != 5)   #True
# print('hi' != 'hi')     #False

############################################################################################
'''ASSIGNMENT OPERATOR(=) : Assign the value of the right side of an expression to the left side.
+= is called as compound assignment opeartor'''

# a = 10
# a += 5      #a = a+5
# print(a)
#
# a = 10
# a -= 3      #a = a-3, a=10-3, a=7
# print(a)    #7
#
# a = 10
# a *= 2      #a = a * 2, a=10*2 = 20
# print(a)        #20

#########################################################################################
'''23 July 2022'''
'''Identity Operators
* Used to check if two values are located on the same part of the memory.
* Used to compare the object, not if they are equal, but if they are actually the same
    object, with the same memory location
is : Returns True if both the variables are pointing to the same id.
is not : Returns True if both the variables are not pointing to the same id.
'''
# a = 10
# b = 10
# c = 20
# print(a is b)       #True
# print(a is c)       #False
#
# a = 'hello'
# b = a
# c = a[:]
# print(c)
# print(a is b)       #True
# print(a is c)       #True
#
# a = 10
# b = 20
# print(a is not b)       #True

######################################################################################
'''Membership Operator
* Used to test if a sequence is present in an object.
* In : Evaluates to True if it finds a value in the specified sequence, otherwise False.
* Not in : Evaluates to True if it does not finds a value in the specified sequence, otherwise
    False
'''
# print('o' in 'python')      #True
# print('r' in 'python')      #False
# print('pn' in 'python')     #False
# print(1 in [1, 2, 3, 4])    #True
# print([1] in [1, 2, 3, 4])  #False
# print(1, 2 in (2, 4, 6))        #1, True
# d = {1:'one', 2:'two', 3:'three'}
# print(1 in d)       #True
# print('one' in d)   #False
# print('one' not in d)   #True

'''
NOTE : Membership operators will take only iterables as right operands, left operand can be
of any typet
‘==’ checks the elements, not the id
‘is’’ checks the id of variables4
'''
###########################################################################################
'''Logical Operator'''
'''and  : : Returns True if both statements are True. Returns False if any one of the
operands evaluates to false.
1 represents True. 0 represents False

    INPUT       INPUT           OUTPUT
     1           1                1
     1           0                0
     0           1                0
     0           0                0
'''
# print(1 and 9)      #9
# print(0 and -9)     #0
# print(-1 and -3)    #-3
################################################################################
'''or : Returns True if one of the statements is True

        INPUT           INPUT           OUTPUT
          1               0               1
          0               1               1
          1               1               1
          0               0               0
'''
# print(1 or 0)       #1
# print(0 or -1)      #-1
# print(10 or 6)      #10

##################################################################################
'''not
It reverse the result.
Returns False if the result is True.
'''
# print(not 0)        #True,.  not bool(0), not False = True
# print(not -7)       #False

####################################################################################
'''Bitwise Operator
Bitwise AND ( & )
Bitwise OR ( | )
Bitwise XOR ( ^ )
Bitwise NOT ( ~ )
Bitwise leftshift ( << )
Bitwise rightshift (  >> )
'''

'''Bitwise AND( & ) : Returns 1 if both the bits are 1 else 0.'''
# print(7 & 5)
# print(25 & 27)
# print(88 & 97)

#######################################################################
'''Bitwise OR : Returns 1 if either of the bits are 1, else 0.'''
# print(88 | 97)

####################################################################
'''Bitwise XOR ( ^ ) : Sets each bit to 1 if only one of the two bits is 1, else 0
        INPUT           INPUT               OUTPUT
          0               1                   1
          1               0                   1
          0               0                   0
          1               1                   0
'''
# print(4 ^ 11)

###################################################
'''Bitwise NOT( ~ )
It is a unary operator. It inverts all the bits
Eg : ~3 = -4 (adds 1 and inverts the sign), 3+1 = 4, inverts sign → -4
'''
# print(~3)
# print(~-9)

#####################################################################################
'''25 July 2022'''
'''Bitwise leftshift(<<)'''
# print(2 << 3)
# print(23 << 4)

'''Bitwise rightshift(>>)'''
# print(23 >> 4)

##########################################################################################
'''Conditional Statements
Conditional statements in programming languages decides the direction of flow of program execution.
Types: 
    if statements
    if-else statements
    elif statements
    Nested if-else statement

INDENTATION: Indentation refers to spaces given at the beginning of any line of code 
 Python uses Indentation to represent a Block of code
'''
#############################################################################################
'''if
An if statement is written by keyword called 'if' followed by any data and ':' infront of data.
interpreter checks the boolean value of the data given in front of if keyword, 
and suppose the outcome is True then it will execute the statement present inside the if block.
Syntax: if <data/condition> :
			statement 1
			statement 2
			....

In-line if statement: 
Syntax: if <data/condition>: statement1, statement 2, …
'''
# a = 10
# if a > 0:
#     print('positive')

'''inline if conditional statements'''
# if a>0:print('positive')

#######################################################################################
'''if-else
Whenever data in front of if keyword become False, it will search for else keyword and it will 
execute the statement present in that else block.
Syntax:     if <data/condition>:
					statement 1
					statement 2..## True Block ##
			else:
					statement 1
					statement 2..## False Block ##

In-line if-else :
Syntax: True_statement if <data/condition> else False_statement.
Note : More than one else block can not be present for a single if block.
'''
# a = int(input('Enter the number: '))
# if a > 0:
#     print('Positive')
# else:
#     print('Negative')
'''Inline if-else statements
Trueblock if <condition> else Falseblock
'''
# # a = int(input('Enter the number: '))
# # print('positive') if a > 0 else print('negative')
#############################################################################################
'''if-elif-else statements
if-elif-else:
Syntax: if <data/condition>:
			statement 1
			statement 2..
		elif <data/condition>:
			statement 1
			statement 2..
		else:
			statement 1
			statement 2..
For a single if statement , we can have multiple elif statements, but we can not have multiple
else statement.
else statement is always unique and also it will executed whenever all the conditions are False,
 that’s why we say else as False block.
'''
# a = int(input('Enter the number: '))
# if a > 0:
#     print(f'{a} is positive')
# elif a < 0:
#     print(f'{a} is Negative')
# else:
#     print(f'{a} is Zero number')

#######################################################################################
'''Check if the iterable is empty or not'''
# a = ' '
# print(len(a))       #0, If len is 0
# print(bool(a))          #False. If bool(iterable is False, then empty iterable, else not)
#
# if bool(a):
#     print('Iterable is not empty')
# else:
#     print('Iterable is empty')

##########################################################################################
'''26 July 2022'''
'''Check if the user input character is vowel or not'''
# user_input = input('Enter the character: ')
# if user_input in 'aeiouAEIOU':
#     print(f'{user_input} is vowel')
# else:
#     print(f'{user_input} is not vowel')
########################################################
# user_input = input('Enter the character: ')
# if user_input.isalpha():
#     if user_input in 'aeiouAEIOU':
#         print(f'{user_input} is vowel')
#     else:
#         print(f'{user_input} is not vowel')
# elif user_input.isnumeric():
#     print(f'{user_input} is a number')
# else:
#     print(f'{user_input} is a special character')
###############################################################
# user_input = input('Enter the character: ')
# if 'a'<=user_input<='z' or 'A'<=user_input<='Z':
#     if user_input in 'aeiouAEIOU':
#         print(f'{user_input} is vowel')
#     else:
#         print(f'{user_input} is not vowel')
# elif '0'<=user_input<='9':
#     print(f'{user_input} is a number')
# else:
#     print(f'{user_input} is a special character')

#########################################################################################
'''check if the user input character is vowel or not, if it is vowel then create a dictionary with
the user input character as a key and its ascii number as a value'''
# user_input = input('Enter the character: ')
# d = {}
# if 'a'<=user_input<='z' or 'A'<=user_input<='Z':
#     if user_input.lower() in 'aeiou':
#         d[user_input] = ord(user_input)
#         print(d)
#     else:
#         print(f'{user_input} is not a vowel')
# else:
#     print(f'{user_input} is not an alphabet')
#############################################################################################
'''wap to check if the user input number is even or odd'''
# number = int(input('Enter the number: '))
# if number % 2 == 0:
#     print(f'{number} is a even number')
# else:
#     print(f'{number} is a odd number')
#####################################################################################
'''check if the user input string is even length or odd length'''
# user_input = input('Enter the string: ')
# if len(user_input) % 2 == 0:
#     print(f'{user_input} is of even length')
# else:
#     print(f'{user_input} is of odd length')

#######################################################################################
'''Take a user input alphabet, if it is in lowercase, convert it into uppercase and viceversa'''
# user_input = input('Enter the character: ')
# if user_input.isalpha():
#     if user_input.isupper():
#         print(chr(ord(user_input) + 32))
#     else:
#         print(chr(ord(user_input) - 32))
# else:
#     print(f'{user_input} is not an alphabet')
#############################################################################################
'''wap to check whether the user input string is palindrome or not'''
# user_input = input('Enter the string: ')
# if user_input == user_input[::-1]:
#     print(f'{user_input} is a palindrome')
# else:
#     print(f'{user_input} is not a palindrome')
##########################################################################################
'''wap to find the greatest of three numbers'''
# a = int(input('enter the value of a: '))
# b = int(input('enter the value of b: '))
# c = int(input('enter the value of c: '))
# if a>b and a>c:
#     print(f'{a} is greater')
# elif b>c:
#     print(f'{b} is greater')
# else:
#     print(f'{c} is greater')
##########################################################################################
'''Check if the user input character is alphabet or number or special character'''
# user_input = input('Enter the character: ')
# if user_input.isalpha():
#     print(f'{user_input} is an alphabet')
# elif user_input.isnumeric():
#     print(f'{user_input} is a number')
# else:
#     print(f'{user_input} is a special character')
#
# user_input = input('Enter the character: ')
# if 'a'<=user_input<='z' or 'A'<=user_input<='Z':
#     print(f'{user_input} is an alphabet')
# elif '0'<=user_input<='9':
#     print(f'{user_input} is a number')
# else:
#     print(f'{user_input} is a special character')
#########################################################################################
'''Check if the given year is leap year or not'''
# year = int(input('Enter the year: '))
# if year % 400 == 0:
#     print(f'{year} is a leap year')
# elif year % 4 == 0 and year % 100 != 0:
#     print(f'{year} is a leap year')
# else:
#     print(f'{year} is not a leap year')

########################################################################################
'''Check if the user input string is starting with vowel or not'''
# user_input = input('Enter the string: ')
# if user_input[0] in 'aeiouAEIOU':
#     print(f'{user_input} is starting with vowel')
# else:
#     print(f'{user_input} is not starting with vowel')
#######################################################################################
'''Check if the user input string is ending with vowel or not'''
# user_input = input('Enter the string: ')
# if user_input[-1] in 'aeiouAEIOU':
#     print(f'{user_input} is ending with vowel')
# else:
#     print(f'{user_input} is not ending with vowel')
#######################################################################################
'''check if the entered marks are pass, fail, firstclass, second class or distinction'''
# user_input = int(input('Enter the marks obtained: '))
# if 0<=user_input<=100:
#     if 85<=user_input<=100:
#         print('You have secured Distinction')
#     elif 70<=user_input<85:
#         print('You have secured first class')
#     elif 55<=user_input<70:
#         print('You have secured second class')
#     elif 35<=user_input<55:
#         print('PASS')
#     else:
#         print('FAIL')
# else:
#     print('PLEASE ENTER THE VALID MARKS')


'''
1. wap to check if the list has even number of elements or not
2. wap to check if the user input number is a palindrome
3. wap to check if the number is positive, negative or zero
4. wap to check whether a person is eligible for voting(>=18)
'''

################################################################################################################
# a = int(input('Enter the numbers:'))        #12321
# b = str(a)      #'12321'
# if b.isnumeric():
#     if b==b[::-1]:
#         print(f'{a} is a palindrome number.')
#     else:
#         print(f'{a} is not a palindrome number')
# else:
#     print(f'{a} is not a valid number')


#####################################################################################################
'''27 July 2022'''
'''wap to check if the user input number is perfect square or not'''
# num = int(input('Enter the number: '))
# b = num ** 0.5
# print(b)
# if int(b) ** 2 == num:
#     print(f'{num} is a perfect square')
# else:
#     print(f'{num} is not a perfect square')

##############################################################################################
'''check if the number of keys present in dictionary is even or not, if it is even, leave it as it is,
else add a key-value pair to make it even'''
# d = {'harry potter':'JK Rowling', 'The Alchemist':'Paulo Coelho', 'The little prince':'Antionio De Exupery'}
# if len(d) % 2 == 0:
#     print('Dictionary is of even length')
#     print(d)
# else:
#     print('Dictinary is of odd length')
#     d['rich dad poor dad'] = 'Robert kiosaki'
#     print(d)

################################################################################################
'''In a number, check if the first element is even or odd'''
# num = int(input('Enter the number: '))
# a = str(num)
# if int(a[0]) % 2 == 0:
#     print('First digit is even')
# else:
#     print('First digit is odd')

##################################################################################################
'''In a number, check if the last element is even or odd'''
# num = int(input('Enter the number: '))
# a = str(num)
# if int(a[-1]) % 2 == 0:
#     print('last digit is even')
# else:
#     print('last digit is odd')

##################################################################################################
'''wap to check if the ASCII value of the user input character is even or odd'''
# user_input = input('Enter the character: ')
# if ord(user_input) % 2 == 0:
#     print(f'The ASCII value of {user_input} is {ord(user_input)} and is even')
# else:
#     print(f'The ASCII value of {user_input} is {ord(user_input)} and is odd')

#################################################################################################
'''remove a random element from set and create a dictionary with removed element as key and it's length as value'''
# s = {'ironman', 'batman', 10, 7.8, 7-9j, True, False, 'KGF'}
# removed_element = s.pop()
# d = {}
# if isinstance(removed_element, str):
#     d[removed_element] = len(removed_element)
# else:
#     d[removed_element] = 'Cannot find length'
# print(d)
####################################################################################################
'''check if the user input str is even or not, if it is even retain as it is else, reverse it'''
# user_input = input('Enter the string: ')
# if len(user_input) % 2 == 0:
#     print('length of user input data is even')
#     print(user_input)
# else:
#     print('length of user input data is odd')
#     print(user_input[::-1])
######################################################################################################
'''take a user input, create a dictionary with the first element as key and user input as a value 
if the first element is even'''
# user_input = input('Enter the string: ')
# d = {}
# if user_input[0] in 'aeiouAEIOU':
#     d[user_input[0]] = user_input
#     print(d)
# else:
#     print('First character is not vowel')

###########################################################################################################
'''LOOPS
A loop is a process which will repeats execution of the set of instructions as many times as we want.
    Types: 
        while loop
        for loop

############################################################3
while loop
used to iterate over a block of code as long as the data/condition present in front of while keyword is True.
Syntax: while <data/condition>:
					statement 1
					statement 2     } Body of loop
					...
Note:
In while loop the data entered in front of while keyword should return False after finite of iterations, 
or else we will end up in a infinite loop.
Incrementation/Decrementation inside while loop must go towards the terminating condition

#################################################
Categories of while loop
    * An infinite loop
    * While loop with an else statement
    * Single statement while loop.

1. An infinite loop
    * If the condition or the body of while loop is incorrect, then we get infinite loop.
    * To stop execution, press Ctrl+C.
    * May be useful in client/server programming.
    Eg :while(True):
            print(“in loop”)

2. While loop with else
    * A while loop may have an else statement after it.
    * When the condition is false, else block gets executed.
    * Else block doesn’t execute if you break out of the loop or if an exception is raised.
    Eg : a=3
        while(a>0):
            print(a)
            a-=1
        else:
            print("Reached 0”)

3. Single statement while
Syntax : while <condition> : statement 1;statement2;
Eg : a=3
while(a>0):print(a);a-=1;

'''
# count = 0
# while count < 5:
#     print('hello world')
#     count += 1
# else:
#     print('Execution completed')

'''
27 July Assignment questions

* Check whether a given number is divisible by 7 or not.
* Check whether a given number is divisible by both 7 and 5 or only 7 or only 5 or not divisible by both.
* Wap to check whether the ASCII value of second char is less than ASCII value of last char in you name.
    If True, print your name as it is, else print the name reversed.
* Wap to replicate abs function (i.e. convert the number to positive if it is negative, keep it as it is if 
    its positive
    ex: a = -5, a should be 5 after executing your program.)
* Given an integer n, perform the following conditional actions.
    * If n is odd , print Bangalore
    * If n is even and in the inclusive range of 2 to 9, print Pune.
    * If n is even and in the inclusive range of 10 to 20, print Bangalore.
    * If n is even and greater than 20, print Pune.
    * Note: choose n between 1 to 100.
* Wap to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
Cost price (in Rs)                  Tax
 > 100000                           15 %
 > 50000 and <= 100000              10%
 <= 50000                           5%
*Accept the kilo meters covered and calculate the bill accordingto the following criteria:
    * First 10 Km Rs11/km
    * Next 90Km Rs10/km
    * After that Rs9/km 
'''

#####################################################################################################
'''29 July 2022'''
'''wap to print the numbers from 1-10'''
# count = 1
# while count <= 10:
#     print(count)
#     count += 1
##################################################################################
'''wap to print the numbers from 10 - 1'''
# count = 10
# while count > 0:
#     print(count)
#     count -= 1
####################################################################################
'''wap to print the alternate numbers from 1- 30'''
# count = 1
# while count <= 30:
#     print(count)
#     count += 2          #odd  numbers
#
# count = 2
# while count <= 30:
#     print(count)
#     count += 2      #even numbers
##################################################################################
'''wap to print the even numbers from 1-50'''
# count = 1
# while count <= 50:
#     if count % 2 == 0:
#         print(count)
#     count += 1
########################################################################################
'''wap to print the even numbers from 1-50'''
# count = 1
# while count <= 50:
#     if count % 2 != 0:
#         print(count)
#     count += 1
########################################################################################
'''wap to print the numbers from -10 to -1'''
# count = -10
# while count < 0:
#     print(count)
#     count += 1
########################################################################################
'''wap to iterate over a string'''
# string = 'hello world'
# count = 0
# while count < len(string):
#     print(string[count])
#     count += 1

######################################################################################
'''wap to print the element of string with its index number'''
# string = 'hello world'
# count = 0
# while count < len(string):
#     print(string[count], count)
#     count += 1

######################################################################################
'''wap to print the alternate characters in the string'''
# a = 'spiderman away from home'
# count = 0
# while count < len(a):
#     print(a[count])
#     count += 2
#
# a = 'spiderman away from home'
# count = 0
# while count < len(a):
#     print(a[count], end='')     #siemnaa rmhm
#     count += 2

########################################################################################
'''wap to add even and odd numbers seperately in two lists fromm 1-50'''
# even_list = []
# odd_list = []
# count = 1
# while count <= 50:
#     if count % 2 == 0:
#         even_list.append(count)
#     else:
#         odd_list.append(count)
#     count += 1
#
# print(even_list)
# print(odd_list)

#########################################################################################
'''wap to calculate the first n number sum'''
# user_input = int(input('enter the number: '))
# count = 1
# sum = 0
# while count <= 5:
#     sum += count
#     count += 1
# print(sum)

###########################################################################################
'''wap to count the number of digits, alphabets and special characters in the given string'''
# string = 'J@nuAry 12 !$ 14 awe$0m# 7890'
# count = 0
# alpha_count = 0
# num_count = 0
# spe_count = 0
# while count < len(string):
#     if string[count].isalpha():
#         alpha_count += 1
#     elif string[count].isnumeric():
#         num_count += 1
#     else:
#         spe_count += 1
#     count += 1
#
# print(f'The total number of alphabets are {alpha_count}, numbers are {num_count} and {spe_count} special characters')

###############################################
# string = 'J@nuAry 12 !$ 14 awe$0m# 7890'
# count = 0
# alpha_count = 0
# num_count = 0
# spe_count = 0
# while count < len(string):
#     if 'a'<=string[count]<='z' or 'A'<=string[count]<='Z':
#         alpha_count += 1
#     elif '0'<=string[count]<='9':
#         num_count += 1
#     else:
#         spe_count += 1
#     count += 1
#
# print(f'The total number of alphabets are {alpha_count}, numbers are {num_count} and {spe_count} special characters')

#####################################################################################
'''wap to get the count of all the vowels and consonants in the string'''
# string = 'Hey there! I am using Whatsapp'
# count = 0
# vowels = 0
# consonants = 0
# while count < len(string):
#     if string[count].isalpha():
#         if string[count] in 'aeiouAEIOU':
#             vowels += 1
#         else:
#             consonants += 1
#     count += 1
# print(f'The totals number of vowels are {vowels} and {consonants} consonants')

##########################################################################################
'''wap to print even length elements in the list'''
# l = ['apple', 'google', 'gmail', 'yahoo', 'microsoft', 'facebook', 'ajio', 'myntra']
# a = 0
# while a < len(l):
#     if len(l[a]) % 2 == 0:
#         print(l[a])
#     a += 1

##################################################################################################
'''wap to print the average of numbers in a list'''
# l = [10, 21, 56, 98, 67, 67, 54, 24, 34, 91]
# count = 0
# sum = 0
# while count<len(l):
#     sum += l[count]
#     count += 1
# avarage = sum/len(l)
#
# print(f'The sum of list elements is {sum} and the average of numbers in a list is {avarage}')

########################################################################################
'''wap to  find the factorial of a user input number'''
# number = int(input('Enter the number: '))           #5
# count = 1       #2, 3, 4, 5, 6
# fact = 1        #1, 2, 6, 24, 120
# while count <=5:
#     fact *= count       #fact = fact * count
#     count += 1
#
# print(f'The factorial of {number} is {fact}')
##########################################################################################
'''30 July 2022'''
'''wap to reverse the user input string'''
# user_input = input('Enter the string: ')
# count = 0
# rev_str = ''
# while count < len(user_input):
#     rev_str = user_input[count] + rev_str
#     count += 1
# print(rev_str)

##############################################################################################
'''wap to reverse the user input number'''
# a = int(input('Enter the number: '))
# user_input = str(a)
# count = 0
# rev_num = ''
# while count < len(user_input):
#     rev_num = user_input[count] + rev_num
#     count += 1
# print(int(rev_num))
###############################################################################################
'''wap to find the sum of all the numbers in the list'''
# num_list = [10, 23, 45, 42, 76, 89, 97, 76, 49]
# count = 0
# sum = 0
# while count < len(num_list):
#     sum += num_list[count]
#     count += 1
# print(sum)
##############################################################################################
'''wap to reverse the list element if it's length is odd, else keep it as it is'''
# list_ele = ['smita', 'praveen', 'archana', 'nandhini', 'mukesh', 'ramya']
# l = []
# count = 0
# while count < len(list_ele):
#     if len(list_ele[count]) % 2 == 0:
#         l.append(list_ele[count])
#     else:
#         l.append(list_ele[count][::-1])
#     count += 1
# print(l)

#############################################################################################
'''calculate the sum of user input numbers'''
# user_input = int(input('Enter the num: '))         #918273
# num = str(user_input)       #'918273'
# sum = 0
# count = 0
# while count < len(num):
#     sum += int(num[count])
#     count += 1
# print(sum)
#################################################################################################
'''create a dictionary with the list elements as keys and it's length as a value'''
# list_ele = ['smita', 'praveen', 'archana', 'nandhini', 'mukesh', 'ramya']
# d = {}
# count = 0
# while count < len(list_ele):
#     d[list_ele[count]] = len(list_ele[count])
#     count += 1
# print(d)

################################################################################################
'''wap to print the filenames ending with pdf'''
# file_names = ['youtube.txt', 'google.pdf', 'gmail.com', 'yahoo.pdf', 'apple.doc', 'amazon.pdf']
# count = 0
# while count < len(file_names):
#     if file_names[count][-3:] == 'pdf':
#         print(file_names[count])
#     count += 1

# file_names = ['youtube.txt', 'google.pdf', 'gmail.com', 'yahoo.pdf', 'apple.doc', 'amazon.pdf']
# count = 0
# while count < len(file_names):
#     a = file_names[count].split('.')
#     if a[1] == 'pdf':
#         print(a[0])
#     count += 1
#
# file_names = ['youtube.txt', 'google.pdf', 'gmail.com', 'yahoo.pdf', 'apple.doc', 'amazon.pdf']
# count = 0
# while count < len(file_names):
#     a =  file_names[count].partition('.')
#     if a[2] == 'pdf':
#         print(a[0])
#     count += 1

#############################################################################################
'''wap to extract only the extensions'''
# file_names = ['youtube.txt', 'google.pdf', 'gmail.com', 'yahoo.jpeg', 'apple.doc', 'amazon.co.in']
# count = 0
# while count < len(file_names):
#     a = file_names[count].split('.', maxsplit=1)
#     print(a[1])
#     count += 1
#
# count = 0
# while count < len(file_names):
#     a =  file_names[count].partition('.')
#     print(a[2])
#     count += 1
#
# '''filenames'''
# file_names = ['youtube.txt', 'google.pdf', 'gmail.com', 'yahoo.jpeg', 'apple.doc', 'amazon.co.in']
# count = 0
# while count < len(file_names):
#     a =  file_names[count].partition('.')
#     print(a[0])
#     count += 1

'''Assignment questions
1. wap to get the below output using the given list
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    d = {'even':5, 'odd':6}
2. wap to get the below output
    l = ['google.com', 'facebook.in', 'youtube.com', 'python.edu']
    d = {6:[google, python], 7:[youtube], 8:[facebook]}
3. Remove all the string objects from the given set
    s = {'hai', 10, True, 0, 5.8, 'python', 11, 'java', 'selenium'}
4. create a dict such that char is the key and it's count on the string is the value, a= abracadabra
5. wap to print the numbers from m to n
6. calculate the sum of numerical values in the string, s = 'hai123, 89python456'
7. wap to calculate the sum of even numbers and the sum of odd numbers seperately from 1-100
8. accept two numbers from the user, one is positive, another negative, now find the sum of all the even 
    numbers between them
9. Traverse through a string, create a dict with string elements as keys and it's ascii number as a value 
10. wap to check if the number is prime or not
'''

###################################################################################################
'''01 August 2022'''
'''
for is a keyword which will act as looping statement in python
        Syntax: for variable in iterable:
					statement 1
					statement 2     
					...
Note:
Here variable acts as a carrier of one element at a time from the iterable given.[in simple, collection 
data type]
No need to give any conditions to increment or decrement like in while loop. It will traverse through one 
element after other on its own

##################################################################################
range()
* Returns a range object sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
    and ends at a specified number.
* To loop through a set of code a specified number of times, we use the range() class.
* Syntax: range(start, end, step)
    Start index is always included.(by default 0)
    End index is always excluded.(Required Argument)
* To view the elements of range object, either we need to traverse through it, or we can typecast it to 
    list/tuple
'''

#######################################################################################
'''
for item in iterable:
    statements

for item in range(SI, EI, SV):
    statements
'''
##################################################################################################
# a = 'hello python'
# for item in a:
#     print(item)

#############################################################################################3
'''range(start value, end value, stepvalue)'''
# print(range(1, 10))     #range(1, 10)
# print(list(range(1, 10)))       #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# for item in range(1, 10):
#     print(item)
#
# for item in range(10):
#     print(item)

'''for loop with else'''
# for item in range(10):
#     print(item)
# else:
#     print('Iteration completed')

###################################################################################################
'''Traversing through different iterables'''
# a = 'hello python'
# for item in a:
#     print(item)
#
# b = ['red', 'blue', 'green', 'yellow', 'purple', 'pink']
# for item in b:
#     print(item)
#
# c = ('red', 'blue', 'green', 'yellow', 'purple', 'pink')
# for item in c:
#     print(item)
#
# d = {'red', 'blue', 'green', 'yellow', 'purple', 'pink'}
# for item in d:
#     print(item)
#
# e = {'primeminister':'narendramodi', 'president':'draupadimurmu', 'financeminister':'nirmalasitharaman', 'chiefminister':'basavarajbommai'}
# for item in e:
#     print(item)     #keys
#
# for item in e.keys():
#     print(item)     #keys
#
# for item in e.values():
#     print(item)     #values
#
# for item in e.items():
#     print(item)

##################################################################################
'''numbers'''
'''print numbers from 1-10'''
# for i in range(1, 11):
#     print(i)
#
# l = []
# for i in range(1, 11):
#     l.append(i)
# print(l)        #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in range(10, 0, -1):
#     print(i)
#
# for i in range(1, 20, 2):
#     print(i)
#
# for i in range(1, 11):
#     print(i, end=' ')       #1 2 3 4 5 6 7 8 9 10

#################################################################################################
'''create a dict such that char is the key and it's count on the string is the value'''
# a= 'abracadabra'
# d = {}
# index = 0
# while index < len(a):
#     d[a[index]] = a.count(a[index])
#     index += 1
# print(d)        #{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

# a= 'abracadabra'
# d = {}          #d = {a:5, b:2, r:2, c:1, d:1}
# index = 0
# while index < len(a):
#     if a[index] in d:
#         d[a[index]] += 1
#     else:
#         d[a[index]] = 1
#     index += 1
# print(d)
#
# a= 'abracadabra'
# d = {}
# for i in a:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)            #{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
#######################################################################################################
'''wap to  print even numbers'''
# for i in range(1, 50):
#     if i % 2 == 0:
#         print(i)
###########################################################################################
'''wap to  print odd numbers'''
# for i in range(1, 50):
#     if i % 2 != 0:
#         print(i)

#################################################################################33
'''wap to  print even and odd numbers seperately in a list'''
# even_list = []
# odd_list = []
# for i in range(1, 50):
#     if i % 2 == 0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print(even_list)        #[2, 4 ,6,...48]
# print(odd_list)         #[1, 3, 5,...49]

###################################################################################################
'''sum of n natural numbers'''
# num = int(input('Enter the num: '))
# sum = 0
# for i in range(1, num+1):
#     sum += i
# print(sum)

##################################################################################################
'''sum of all the digits present in a number'''
# user_input = int(input('Enter the number:'))        #345112787654356
# num = str(user_input)
# sum = 0
# for i in num:
#     sum += int(i)
# print(sum)

################################################################################################
'''create a list where even length elements should be as it is, odd length elements should be reversed'''
# l = ['bangalore', 'mysore', 'pune', 'delhi', 'mumbai', 'chennai', 'hubli', 'shimoga']
# list_1 = []
# for i in l:
#     if len(i)%2==0:
#         list_1.append(i)
#     else:
#         list_1.append(i[::-1])
#
# print(list_1)

###############################################################################################3
'''converting uppercase to lowercase and viceversa'''
# a = 'J@mEs BoNd 007'
# b = ''
# for i in a:
#     if 'a'<=i<='z':
#         b += chr(ord(i)-32)
#     elif 'A'<=i<='Z':
#         b += chr(ord(i)+32)
#     else:
#         b += i
# print(b)

################################################################################################################
'''02 Aug 2022'''
'''wap to count the number of uppercase, lowercase, numbers and special characters in a string'''
# a = 'MOnEy 123@ !#5 HiESt &* iS AVeRagE!'
# upper = 0
# lower = 0
# num = 0
# spe_char = 0
# for item in a:
#     if 'a'<=item<='z':
#         lower += 1
#     elif 'A'<=item<='Z':
#         upper += 1
#     elif '0'<=item<='9':
#         num += 1
#     else:
#         spe_char += 1
# print(f'Theere are {upper} uppercase letters, {lower} lowercase letters, {num} numbers and {spe_char} spe characters')

##############################################################################################
'''calculate the sum of numerical characters present in the string'''
# string = 'Hello 123@234, 78965 python 4567 '
# sum = 0
# for i in string:
#     if '0'<=i<='9':
#         sum += int(i)
#
# print(sum)

###############################################################################################3
'''wap to reverse the string'''
# a = 'avengers:age of ultron'
# rev_str = ''
# for i in a:
#     rev_str = i + rev_str
# print(rev_str)
#
# a = 'avengers:age of ultron'
# rev_str = ''
# for i in range(len(a)-1, -1, -1):
#     rev_str += a[i]
# print(rev_str)
#
# a = 'avengers:age of ultron'
# rev_str = ''
# for i in range(len(a)):
#     rev_str = a[i] + rev_str
# print(rev_str)
#######################################################################################################
'''wap to get the max number in the list'''
# l = [10, 1, -1, 33, 65, 45, 43, 0, 98, 78]
# max_num = 0
# for i in l:
#     if i > max_num:
#         max_num = i
# print(max_num)
# print(max(l))
##################################################################################################
'''minimum number'''
# l = [10, 1, 33, 65, 45, 43, 98, 0, 78]
# min_num = l[0]
# for i in l:
#     if i < min_num:
#         min_num = i
# print(min_num)
# print(min(l))

'''NOTE: max() function will give the maximum number in the list, whereas min() func will give minimum
number in the list'''
#######################################################################################################
'''create a list with even length elements only'''
# l = ['lenskart', 10, True, 'ajio', 'gmail', 'microsoft', False, 8.7, ['a', 'b', 'c'], [1, 2, 3, 4]]
# list_1 = []
# for i in l:
#     if not isinstance(i, (int, float, complex, bool)):
#         if len(i)%2 == 0:
#             list_1.append(i)
# print(list_1)       #['lenskart', 'ajio', [1, 2, 3, 4]]
######################################################################################
# l = ['apple', 'google', 'facebook', 'microsoft', 'ajio', 'myntraa', 'ola']
# print(max(l))       #ola. considers highest ASCII value
# print(max(l, key=len))      #microsoft
# l.sort(key=len)
# print(l)    #['ola', 'ajio', 'apple', 'google', 'myntraa', 'facebook', 'microsoft']
# print(min(l))       #ajio
# print(min(l, key=len))      #ola

###################################################################################################
'''wap to check if the num is prime or not'''
# num = int(input('Enter the num: '))     #7
# for item in range(2, num):
#     if num % item == 0:
#         print(f'{num} is not prime')
#         break
# else:
#     print(f'{num} is prime')

##########################################################################################
'''first n prime numbers'''
# num = int(input('Enter the num: '))
# for i in range(2, num):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)
'''
ASSIGNMENT
1. create a dict with elements as keys and its length as value
    l = ['apple', 'google', 'gmail', 'microsoft', 'ajio', 'myntra']
2. find the sum of all numerical data present in a list
    l = [10, True, 0, 45, 'hey', [8, 9, 7], False, 6.4, 'python']
3. wap to fetch the extensions
    files = ['youtube.com', 'gmail.pdf', 'apple.doc', 'google.jpeg', 'amazon.co.in']
4. wap to fetch the filenames
    files = ['youtube.com', 'gmail.pdf', 'apple.doc', 'google.jpeg', 'amazon.co.in']    
5. create a dict with the words as key, and it's occurances as value
    a = 'python is awesome python is fun'
6. create a dict with first element as key and entire word as value
7. remove a random element from the set and create a dict with the deleted element as a key and it's len as value
8. wap to find the factorial of a number
9. calculate the product of numerical characters present in a string, 
    string = 'hello12344, 786, 98, 45 python'
10. wap to check if the elements of a tuple are palindrome or not
11. wap to check if the elements of a tuple are palindrome or not, If it is a not a palindrome, then create
    a dictionary  with the non-palindrome element as key and its reverse as a value
'''
################################################################################################
'''04 August 2022'''
'''wap to find the sum of all numerical data present in the list'''
# list1 = [10, 8.5, 'hai', 7+9j, True, ['a', 'b', 'c'], 49]
# sum = 0     #10, 18.5,
# for i in list1:
#     if not isinstance(i, (str, list)):
#         sum += i        #sum = sum + i
# print(sum)

#################################################################################################
'''create a dict, elements as keys and it's position as value in the list'''
# a = 'harry potter'
# d = {}
# for i in a:
#     d[i] = a.index(i)
#
# print(d)    #{'h': 0, 'a': 1, 'r': 2, 'y': 4, ' ': 5, 'p': 6, 'o': 7, 't': 8, 'e': 10}

#############################################################################################
'''enumerate() :
* enumerate(iterable)
* Returns an enumetare object.
* Iterable must be a sequence, an iterator or some other object which supports iteration
* Returns a tuple containing a count(from start, default value is 0) and the values obtained from
    iterating over iterable'''
# a = 'harry potter'
# print(enumerate(a))     #<enumerate object at 0x000001B4C6BF4900>
# print(list(enumerate(a)))

# a = 'harry potter'
# for i in enumerate(a):
#     print(i)
#
# a = 'harry potter'
# d = {}
# for index, item in enumerate(a):
#     d[item] = index
# print(d)        #{'h': 0, 'a': 1, 'r': 11, 'y': 4, ' ': 5, 'p': 6, 'o': 7, 't': 9, 'e': 10}
#
# a = 'harry potter'
# d = {}
# for index, item in enumerate(a):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item] += [index]
#
# print(d)    #{'h': [0], 'a': [1], 'r': [2, 3, 11], 'y': [4], ' ': [5], 'p': [6], 'o': [7], 't': [8, 9], 'e': [10]}

#############################################################################################
# list1 = ['rose', 'lotus', 'lily', 'jasmine', 'marigold', 'tulips', 'sunflower']
# for index, item in enumerate(list1):
#     print(index, item)
#
# tuple_1 = ('book', 'pen', 'pencil', 'scale', 'eraser', 'protractor', 'sharpener')
# for index, item in enumerate(tuple_1):
#     print(index, item)

# set_1 = {'book', 'pen', 'pencil', 'scale', 'eraser', 'protractor', 'sharpener'}
# for index, item in enumerate(set_1):
#     print(index, item)
#
# dict_1 = {'India':'Delhi', 'Pakistan':'Karachi', 'USA':'Newyork', 'Canada':'Ottawa', 'Germany':'Srugart'}
# for i in enumerate(dict_1):
#     print(i)        #(index, keys)
#
# dict_1 = {'India':'Delhi', 'Pakistan':'Karachi', 'USA':'Newyork', 'Canada':'Ottawa', 'Germany':'Srugart'}
# for i in enumerate(dict_1.keys()):
#     print(i)
#
# dict_1 = {'India':'Delhi', 'Pakistan':'Karachi', 'USA':'Newyork', 'Canada':'Ottawa', 'Germany':'Srugart'}
# for i in enumerate(dict_1.values()):
#     print(i)
#
# dict_1 = {'India':'Delhi', 'Pakistan':'Karachi', 'USA':'Newyork', 'Canada':'Ottawa', 'Germany':'Srugart'}
# for i in enumerate(dict_1.items()):
#     print(i)
###################################################################
'''zip() : 
* The zip() function takes iterables(can be zero or more), arranges them in a tuple and return it.
* The zip() function returns a zip object which has a list of tuples.
* If the passed iterators have different lengths, the iterator with least items decides the length of the new iterator.
    SYNTAX : zip(iterator1, iterator2,…)'''
# a = 'hello'
# b = 'world'
# print(zip(a, b))        #<zip object at 0x0000026AC2D74980>
# print(list(zip(a, b)))      #[('h', 'w'), ('e', 'o'), ('l', 'r'), ('l', 'l'), ('o', 'd')]

# for i in zip(a, b):
#     print(i)
##################
# a = 'friends'
# b = 'the vampire diaries'
# for i in zip(a, b):
#     print(i)
#
# a = [1, 2, 3, 4]
# b = 'javascript'
# for i in zip(a, b):
#     print(i)
#
# a = [1, 2, 3, 4, 5, 6, 7]
# b = 'javascript'
# c = 'python'
# for i in zip(a, b, c):
#     print(i)
#
# a = 'hai'
# b = {1:10, 2:20, 3:30, 4:40, 5:50}
# for i in zip(a, b):
#     print(i)        #keys
#
# a = 'hai'
# b = {1:10, 2:20, 3:30, 4:40, 5:50}
# for i in zip(a, b.values()):
#     print(i)
#
# a = 'hai'
# b = {1:10, 2:20, 3:30, 4:40, 5:50}
# for i in zip(a, b.items()):
#     print(i)

##############################################################################################
'''zip_longest : 
* To include all the elements of iterables of different length, we can use zip_longest of itertools module.
* It will map to the extra element with None by default.
* SYNTAX: zip_longest(iterator1, iterator2,……….., [fillvalue = None])'''
# from itertools import zip_longest
# a = 'java'
# b = 'selenium'
# for i in zip_longest(a, b):
#     print(i)
#
# from itertools import zip_longest
# a = 'java'
# b = 'selenium'
# for i in zip_longest(a, b, fillvalue='hai'):
#     print(i)

##################################################################################
# a = 'python is a programming language programs are fun'
# #d = {p:[python, programming, programs], i:[is], a:[a, are], l:[language], f:[fun]}
# d = {}
# for i in a.split():
#     if i[0] not in d:
#         d[i[0]] = [i]
#     else:
#         d[i[0]] += [i]
# print(d)

##################################################################################
'''default dictionary 
In Normal dictionaries a key cannot be updated without initialization that is updation can only be done 
after initialization.
In default dict, updation as well as initialization can be done simultaneously
'''
# a = 'python is a programming language programs are fun'
# from collections import defaultdict
# dd = defaultdict(list)
# for i in a.split():
#     dd[i[0]] += [i]
#
# print(dd)
# defaultdict(<class 'list'>, {'p': ['python', 'programming', 'programs'], 'i': ['is'], 'a': ['a', 'are'],
# 'l': ['language'], 'f': ['fun']})

###############################################################################################
# a = 'abracadabra'       # {a:5, b:2, r:2, c:1, d:1}
# from collections import defaultdict
# dd = defaultdict(int)
# for i in a:
#     dd[i] += 1
# print(dd)       #defaultdict(<class 'int'>, {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
###############################################################################################
'''reversed() : Returns iterator object. Will reverse the given sequence'''
# a = 'python'
# print(reversed(a))      #<reversed object at 0x0000023F5DE33FD0>
# print(list(reversed(a)))        #['n', 'o', 'h', 't', 'y', 'p']
# for i in reversed(a):
#     print(i, end='')

#################################################################################################
'''loop control statements'''
# '''break : break will stop the execution of loop and comes out of it.'''
# for i in range(0, 5):
#     if i == 3:
#         break
#     print(i)        #o/p = 0, 1, 2
#################################################################################################
'''continue :  Will skip the current execution and continues with the next one.'''
# for i in range(0, 5):
#     if i == 3:
#         continue
#     print(i)        #o/p = 0, 1, 2, 4

'''pass : It performs no operation.'''
# for i in range(0, 5):
#     if i == 3:
#         pass
#     print(i)

##################################################################################################
'''05 August 2022'''
'''Pattern Printing'''
'''
*
* *
* * *
* * * *
'''
# for i in range(4):
#     for j in range(i+1):
#         print('*', end=' ')
#     print()
#
# for i in range(1, 5):
#     print('* ' * i)

##############################################################################################
'''
* * * *
* * *
* *
*
'''
# for i in range(4, 0, -1):
#     print('* ' * i)
##################################################################################################
'''
      *
    * *
  * * *
* * * *'''
# for i in range(1, 5):
#     print(f'{"* " * i:>8}')
#################################################################################################
'''
*
* *
* * *
* * * *
* * *
* *
*  '''
# for i in range(1, 5):
#     print('* ' * i)
# for j in range(3, 0, -1):
#     print('* ' * j)

###################################################################################################
'''
   *
  * * 
 * * *
* * * *
'''
# for i in range(1, 5):
#     print(f'{"* " * i:^8}')

#####################################################################################3
'''
* * * *
 * * *
  * *
   *
'''
# for i in range(4, 0, -1):
#     print(f'{"* " * i:^8}')

#########################################################################################
'''08 August 2022'''
'''
1
1 2
1 2 3
1 2 3 4'''
# pattern = ''
# for i in range(1, 5):
#     pattern += str(i) +' '
#     print(pattern)
############################################################################################
'''
      1
    1 2
  1 2 3
1 2 3 4'''
# pattern = ''
# for i in range(1, 5):
#     pattern += str(i) + ' '
#     print(f'{pattern:>8}')
########################################################################################
'''
    1
   1 2
  1 2 3
 1 2 3 4 
1 2 3 4 5'''
# pattern = ''
# for i in range(1, 6):
#     pattern += str(i) + ' '
#     print(f'{pattern:^10}')

##################################################################################################
'''
a  
a b
a b c
a b c d
a b c d e
'''
# pat = ''
# for i in range(ord('a'), ord('f')):
#     pat += chr(i) + ' '
#     print(pat)

############################################################################################
'''
        a
      a b
    a b c
  a b c d
a b c d e
'''
# pat = ''
# for i in range(ord('a'), ord('f')):
#     pat += chr(i) + ' '
#     print(f'{pat:>10}')

########################################################################################
'''
a b c d e
a b c d
a b c
a b
a
'''
# for i in range(4, -1, -1):
#     for j in range(i + 1):
#         x = ord('a') + j
#         print(chr(x), end=' ')
#     print()
#################################################################################################
'''
*
*
* *
*
* * *
*
* * * *
*
'''
# for i in range(1, 5):
#     print('* ' * i)
#     print('*')

##########################################################################################################
##########################################################################################################
'''COMPREHENSIONS 
* List comprehension is an elegant way to define and create lists based on existing iterables[collection DT].
* Syntax : var = [expression for var in iterable [if condition to filter]]
* Here var acts as a carrier to carry one element after another from the mentioned iterable.
* It can identify when it receives a string or a tuple and work on it like a list.
* List comprehensions can utilize conditional statement to modify(filter).

Set Comprehension: 
It’s exactly same as list comprehension but the boundary will be set, so it will have all the 
characteristics of sets(i.e no duplicates, contains only immutable etc.

Dictionary Comprehension
* It’s a easy way of constructing a dictionary in a single line based on comprehensions.
* Syntax: {key:value for var in iterable [if condition to filter]}
* Here the expression should be in key: value pair, so key should follow all its characteristics.
'''

'''
SYNTAX:
no condition: [expression for item in iterable] / {expression for item in iterable}
only if condition : [expression for item in iterable if <condition>]
both if-else : [Trueblock if <condition> else Falseblock for item in iterable]
'''
#########################################################################################
'''write a list comprehension which will print the squares of numbers in the list'''
'''using normal for loop'''
# num = [1, 2, 3, 4, 5]       #[1, 4, 9, 16, 25]
# square_list = []
# for i in num:
#     square_list.append(i**2)
# print(square_list)
#
# '''using list comprehension'''
# l = [i**2 for i in num]
# print(l)

'''using set comprehension'''
# l = {i**2 for i in num}
# print(l)
######################################################################################
'''create a list comprehension to print the even numbers in the range(1, 50)'''
# even_list = []
# for i in range(1, 50):
#     if i % 2 == 0:
#         even_list.append(i)
# print(even_list)
'''even'''
# even = [i for i in range(1, 50) if i%2==0]
# print(even)
'''odd'''
# odd = [i for i in range(1, 50) if i%2!=0]
# print(odd)

##################################################################################
'''create a list with elements which has the length less than 8 characters'''
# l = ['thor', 'superman', 'spiderman', 'ironman', 'hawkeye', 'blackwidow', 'hulk']
# length = [i for i in l if len(i)<8]
# print(length)

##################################################################################
'''create a list such that if the length of element is even, retain as it is, else reverse it'''
# l = ['thor', 'superman', 'spiderman', 'ironman', 'hawkeye', 'blackwidow', 'hulk']
# l1 = []
# for i in l:
#     if len(i)%2==0:
#         l1.append(i)
#     else:
#         l1.append(i[::-1])
# print(l1)
#
# l2 = [i if len(i)%2==0 else i[::-1] for i in l]
# print(l2)

###################################################################################################
'''
1. wap to get the list of elements starting with vowels
2. wap to get the list of elements ending with vowels
3. create a list of tuples of the element and its length pair
4. build a list with even length elements only
5. create a list with elements whose last digit is divisible by 3
    l = [123, 321, 456, 789, 875, 986]
6. create a list of elements starting with p
    l = ['python', 'php', 'java', 'selenium', 'perl', 'ruby']
7. fetch the string elements only
    l = [10, '10', 'python', 6.9, True, "False", 'hello']
8. write a list comprehension for the element and its index pair
    string = 'harry potter'
9. Write a list comprehension to multiple the corresponding index elements of both lists
    a = [1, 2, 3, 34]
    b = [6, 3, 23, 8]
10. write a list comprehension to reverse the string elements in the list, retain the other elements as it is
    l = [10, '10', 'python', 6.9, True, "False", 'hello']    
'''

###########################################################################################################
'''9 August 2022'''
'''create a list with elements starting with vowels and if the length is odd reverse it, else retain as it is'''
# l = ['apple', 'google', 'oracle', 'ola', 'ajio', 'myntra', 'urbanic']
# l1 = []
# for i in l:
#     if i[0] in 'aeiouAEIOU':
#         if len(i) % 2 == 0:
#             l1.append(i)
#         else:
#             l1.append(i[::-1])
# print(l1)

'''comprehensions'''
# res = [i if len(i)%2==0 else i[::-1] for i in l if i[0] in 'aeiouAEIOU']
# print(res)
#####################################################################################
'''create a dictionary of char and it's ASCII value pair'''
# a = 'python'
# d = {}
# for i in a:
#     d[i] = ord(i)
# print(d)        #{'p': 112, 'y': 121, 't': 116, 'h': 104, 'o': 111, 'n': 110}

'''comprehensions'''
# d1 = {i:ord(i) for i in a}
# print(d1)

############################################################################################
'''create a dict with list element as key, if len of key is even, retain the same for value, else
reverse it for the value'''
# l = ['apple', 'google', 'oracle', 'ola', 'ajio', 'myntra', 'urbanic']
# d = {}
# for i in l:
#     if len(i) % 2 == 0:
#         d[i] = i
#     else:
#         d[i] = i[::-1]
# print(d)

'''comprehensions'''
# d1 = {i:i if len(i)%2==0 else i[::-1] for i in l}
# print(d1)

#############################################################################################
'''flip the key value pair'''
# d = {'ITC':270, 'IRCTC':3000, 'MRF':80000, 'Dmart':3500, 'Bhartiairtel':600, 'idea':7, 'adani':500}
# d1 = {}
# for key,value in d.items():
#     d1[value] = key
# print(d1)

'''comprehensions'''
# d2 = {value:key for key,value in d.items()}
# print(d2)

#################################################################################################
'''create a dictionary of words as keys in the given sentence and its length as value'''
# a = 'sketch your imagination'
# d = {}
# for i in a.split():
#     d[i] = len(i)
# print(d)
#
# d1 = {i:len(i) for i in a.split()}
# print(d1)

##################################################################################################
# a = [1, 2, 3, 34]
# b = [6, 3, 23, 8]
# res = []
# for i, j in zip(a, b):
#     res.append(i * j)
# print(res)
#
# res1 = [i*j for i, j in zip(a, b)]
# print(res1)

##########################################################################################
'''
in
not in 
'''

# print('p' in 'python')
# print('P' in 'python')
# print('pyt' in 'python')
# print('phn' in 'python')

# print('P' not in 'python')
# print('p' not in 'python')

##########################################################################################
'''
no condition = [expression for item in iterable]
only if condition = [expression for item in iterable if <condition>]
both if-else = [TrueBlock if <condition> else FalseBlock for item in iterable]
'''
# l1 = []
# for i in range(1, 15):
#     l1.append(i ** 2)
# print(l1)
#
# l2 = [i ** 2 for i in range(1, 15)]
# print(l2)

# l1 = []
# for i in range(1, 50):
#     if i % 2 == 0:
#         l1.append(i)
#
# print(l1)
#
# l2 = [i for i in range(1, 50) if i%2==0]
# print(l2)

# l = ['archana', 'smita', 'nandhini', 'vijay', 'mukesh', 'praveen', 'radhika', 'anurag']
# l1 = []
# for i in l:
#     if len(i)%2==0:
#         l1.append(i)
#     else:
#         l1.append(i[::-1])
# print(l1)
#
# l2 = [i if len(i)%2==0 else i[::-1] for i in l]
# print(l2)
# l2 = {i if len(i)%2==0 else i[::-1] for i in l}
# print(l2)

################################################################################################################
'''10 August 2022'''
'''Functions
* A function is a block of code which only runs when it is called.
* Functions help break our program into smaller chunks
* As a program grows larger and larger, functions make it more organized and manageable.
* Function avoids repetition and makes the code reusable.

Types of Functions:
* Built- in Functions : Eg : len(), id(), input(),...
* User Defined Functions

#############
1. Built-in Functions: The functions which are pre-defined in the software to perform some specified task.
   eg:  print() - used to print anything in the output terminal
        input() - used to take the user input at the time of execution
        len() - used to calculate the length of an iterable.

2. User Defined Functions: The functions which are defined by the user to perform a specific task.
    Syntax: 	def func_name(parameters):
					Statement 1
					….
					return <data>

                func_name() - Name of the function which helps to reuse.

parameters - variables declared during function definition.
Arguments - values or data passed during function call
return - the value(data) to be return to the caller.

'''
# a = 'hello world'
# def length(n):
#     count = 0
#     for i in n:
#         count += 1
#     print(count)
#
# length(a)
#########################################################################################
'''return: 
* Statement used to get or return the values from a function to the caller.
* The return statement is used to exit a function and go back to the place from where it was called.
* The statements after the return statements will not be executed once return statement is executed.
* It can return single or multiple data.
* Syntax:
    return data
    return data1,data2.. ⇒ 	returns tuple'''
# a = 'hello world'
# b = 'hai'
# c = 'python'
# def length(n):
#     count = 0
#     for i in n:
#         count += 1
#     return count
# res = length(b)
# print(res)
# print(length(a))

########################
'''can return any number of values, the values will be packed in the form of tuple'''
# def spam():
#     return 10, 20, 2.5, 'python', [1, 2, 3], True
#
# print(spam())       #(10, 20, 2.5, 'python', [1, 2, 3], True)

'''can have multiple return statements, it'll not give any error. But only one return statement will be
executed and operations after the return keyword will never be considered'''
# def spam():
#     return 10
#     return 20
#     print('ha')
#
# print(spam())

##############################################################################################
'''TYPES OF ARGUMENTS
i. Positional arguments
ii. Keyword arguments
iii. Combinatiion of both positional and keyword arguments
iv. Positional only arguments
v. Keyword only arguments
vi. Positional and keyword only arguments
vii. Variable positional arguments
viii. Variable keyword arguments
'''
#########################################################################
'''Positional Arguments'''
# def greet(name, age):
#     print(f'My name is {name} and I am {age} years old')
#
# greet('Ram', 20)        #My name is Ram and I am 20 years old
# greet(20, 'Ram')        #My name is 20 and I am Ram years old

############################################################################
'''keyword arguments'''
# def greet(name, age):
#     print(f'My name is {name} and I am {age} years old')
#
# greet(name='Ram', age=20)       #My name is Ram and I am 20 years old
# greet(age=20, name='Ram')       #My name is Ram and I am 20 years old

############################################################################
'''combination of positional and keyword arguments'''
# def add(a, b, c, d, e):
#     print(a + b + c + d + e)
#
# add(1, 2, 3, 4, 5)                  #15
# add(a=1, b=2, c=3, d=4, e=5)        #15
# add(1, 2, 3, d=4, e=5)              #15
# add(a=1, b=2, 3, 4, 5)        #SyntaxError: positional argument follows keyword argument
# add(1, 2, c=3, 4, e=5)          #SyntaxError: positional argument follows keyword argument

####################################################################################
'''Positional only arguments = Indicated by / . We've to give it in the function definition.
The arguments present before the / should be positional arguments only'''
# def add(a, b, c, /, d, e):
#     print(a + b + c + d + e)
#
# add(1, 2, 3, 4, 5)          #15
# add(1, 2, 3, d=4, e=5)      #15
# add(a=1, b=2, c=3, d=4, e=5)        #TypeError
# add(1, 2, c=3, d=4, e=5)        #TypeError
######################################################################################################
'''keyword only arguments = Indicated by * . We've to give it in the function definition.
The arguments present after the * should be keyword arguments only'''
# def add(a, b, c, *, d, e):
#     print(a + b + c + d + e)
#
# add(a=1, b=2, c=3, d=4, e=5)        #15
# add(1, 2, 3, d=4, e=5)              #15
# add(1, 2, c=3, d=4, e=5)            #15
# add(1, 2, 3, 4, e=5)                #TypeError
###############################################################################################
'''combination of positional and keyword only arguments'''
# def add(a, b, /,c, *, d, e, f):
#     print(a + b + c + d + e + f)
#
# add(1, 2, 3, d=4, e=5, f=6)
# add(1, 2, c=3, d=4, e=5, f=6)
# add(1, b=2, c=3, d=4, e=5, f=6)     #TypeError

######################################################
# def add(a, b, c, *, /, d, e, f):
#     print(a + b + c + d + e + f)
#
# add(1, 2, 3, 4, 5, 6)       #SyntaxError: invalid syntax


###############################################################################################
'''11 Aug 2022'''
'''variable positional arguments : Packs in the form of a tuple. 
    *args will only take the positional arguments'''
# def func(*args):
#     print(args)     #(10, 20.8, (3-9j), True, 'hai', [1, 2], (6, 7, 8), {3, 5, 7}, {1: 1, 2: 2, 3: 3})
#
# func(10, 20.8, 3-9j, True, 'hai', [1, 2], (6, 7, 8), {3, 5, 7}, {1:1, 2:2, 3:3})
######################################################################################################
'''variable keyword arguments : Packs in the form of a Dictionary. 
    **kwargs will only take the keyword arguments'''
# def func(**kwargs):
#     print(kwargs)
#
# func(a=1, b='2', c=9.8, d=[1, 2, 3])
################################################################################################
'''combination of variable number of positional and keyword arguments'''
# def func(*args, **kwargs):
#     print(args, kwargs)
#
# func(1, 2, 3, c=4, d=5, e=6)        #(1, 2, 3) {'c': 4, 'd': 5, 'e': 6}

##################################################################################################
'''To unpack the data'''
# l = ['hai', 'hello']
# def func(a, b):
#     print(a, b)
#
# func(*l)

##################################################################################################
# l = ['hai', 'hello', 1, 2, 3, 4, 5, 6, 'end']
# def func(*args):
#     print(args)
#
# func(*l)        #('hai', 'hello', 1, 2, 3, 4, 5, 6, 'end')

##########################################################################
# l = ['hai', 'hello', 1, 2, 3, 4, 5, 6, 'end']
# def func(a, *args):
#     return a, args
#
# print(func(*l))     #('hai', ('hello', 1, 2, 3, 4, 5, 6, 'end'))

#############################################################################
# l = ['hai', 'hello', 1, 2, 3, 4, 5, 6, 'end']
# def func(a, *args, b):
#     return a, args, b
#
# print(func(*l))     #TypeError

##################################################################################
'''To get first and last element'''
# l = ['hai', 'hello', 1, 2, 3, 4, 5, 6, 'end']
# def func(a, *args):
#     return a, args[-1]
#
# print(func(*l))     #('hai', 'end')

#################################################################################
'''Default arguments/parameters'''
# def add(a, b, c=0):
#     print(a + b + c)
# add(1, 2)       #3
# add(1, 2, 3)    #6
#####################################################################################
'''Function annotaion'''
# def add(a:int, b:int):
#     print(a + b)
# add(1, 2)
# add('hai', 'hello')
#########################################################################################
'''waf to count the number of alphabets, special characters and numbers'''
# a = 'hai @ 123 HeLLO 789 %^&HOw arE You67890'
# b = 'PyTHON @123 $%^& is Fun&*9877'
# def count(n):
#     alpha = 0
#     num = 0
#     spe_char = 0
#     for i in n:
#         if 'a'<=i<='z' or 'A'<=i<='Z':
#             alpha += 1
#         elif '0'<=i<='9':
#             num += 1
#         else:
#             spe_char += 1
#     return f"The total number of alphabets are {alpha}, numbers are {num} and {spe_char} special characters"
# print(count(a))
# print(count(b))

############################################################################################
'''waf to print "HI EVERYONE" if the user input is not given'''
# def func(user_input="HI EVERYONE"):
#     print(user_input)
#
# func('hello world')     #hello world
# func()      #HI EVERYONE

###########################################################################################
'''Create a list with elements whole last digit is divisible by 3 '''
# l = [123, 321, 'hello', 456, 789, 875, 986, 'hai']
# def digit(n):
#     l1 = []
#     for i in n:
#         if isinstance(i, int):
#             b = str(i)
#             if int(b[-1]) % 3 == 0:
#                 l1.append(int(b))
#     return l1
#
# print(digit(l))

####################################################################################
# l = [123, 321, 'hello', 456, 789, 875, 986, 'hai']
# l2 = [i for i in l if isinstance(i, int) if int(str(i)[-1])%3==0]
# print(l2)

####################################################################################

'''
1. waf to create a dictionary of a word and its count pair
2. waf to return the words starting with vowels. l = [apple, 'oracle, walmart, ajio, myntra]
3. waf which takes the variable number of arguments and return how many arguments were passed
4. waf to add the numbers present in the list
    l = [10, 'hai', 20, 'hello', 7.8, 9.6, 'python']
5. waf to find the factorial of a number
6. waf to check if the length of the argument is greater than 5 or not
'''

# l = ['apple', 'oracle', 'walmart', 'ajio', 'myntra']
# def vowel(n):
#     l1 = []
#     for i in n:
#         if i[0] in "aeiouAEIOU":
#             l1.append(i)
#     return l1
#
# print(vowel(l))

#########################################################################################
'''waf to create a dictionary of a word and its count pair'''
# a = 'python is a programming language and programming in python is fun'
# def count(n):
#     d = {}
#     for i in n.split():
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     return d
#
# print(count(a))


# a = 'python is a programming language and programming in python is fun'
# def count(n):
#     d = {}
#     b = n.split()
#     for i in b:
#         d[i] = b.count(i)
#     return d
#
# print(count(a))

##############################################################################
'''waf which takes the variable number of arguments and return how many arguments were passed'''
# def func(*args, **kwargs):
#     print(len(args) + len(kwargs))
#
# func(1, 9, 'hai', 7, 8.6, b=5, m=0, j=8, l=6)
#
#
# def func(*args, **kwargs):
#     count = 0
#     for i in args:
#         count  += 1
#     for i in kwargs:
#         count += 1
#     print(count)                            #9
#
# print(func(1, 9, 'hai', 7, 8.6, b=5, m=0, j=8, l=6))    #None
###################################################################################
'''waf to add the numbers present in the list'''
# l = [10, 'hai', 20, 'hello', 7.8, 9.6, 'python']
# def sum_1(n):
#     sum = 0
#     for i in n:
#         if isinstance(i, (int, float)):
#             sum += i
#     return sum
#
# print(sum_1(l))
###################################################################################
'''waf to find the factorial of a number'''
# def factorail(n):
#     fact = 1
#     for i in range(n, 0, -1):
#         fact *= i
#     return fact
# print(factorail(5))
####################################################################################
'''waf to check if the length of the argument is greater than 5 or not'''
# def length(n):
#     if len(n) > 5:
#         print('length of argument is greater than 5')
#     else:
#         print('length of argument is not greater than 5')
#
# length('python')
# length('java')
#####################################################################################
'''Prime number'''
# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return f'{n} is not a prime number'
#     else:
#         return f'{n} is a prime number'
# print(prime(11))
# print(prime(12))

####################################################################################
'''waf to print the maximum number and minimum in the list'''
# l = [10, 1, 23, 42, 14, 98, 0, 56, 164, 70]
# def num(n):
#     max_num=0
#     for i in n:
#         if i> max_num:
#             max_num=i
#     return max_num
#
# print(num(l))


# a = [10 , -1 , 1 , 33,65,345,67,87]
# def minimum(n):
#     min_num = n[0]
#     for i in n:
#         if i < min_num:
#             min_num = 1
#     print(min(a))
#
# minimum(a)

'''waf to check to return the list of palindromes from the given list'''
# l1 = ['mom', 'dad', 'hai', 'malayalam', 'english']
# def palindrome (n):
#     l = []
#     for i in n:
#         if i == i[::-1]:
#             l.append(i)
#     return l
# print(palindrome(l1))


'''waf to swap the cases'''
# a =  'Hai@34 HeLLo PYtHOn &*63'
# def swap(n):
#     b = ''
#     for i in n:
#         if 'a'<=i<='z':
#             b += chr(ord(i)-32)
#         elif 'A'<=i<='Z':
#             b += chr(ord(i)+32)
#         else: b += i
#     return b
#
# print(swap(a))


# def min_num(*args):
#     # print(args)
#     min_n = 0
#     for i in args:
#         if min_n > i:
#             min_n = i
#     return min_n
#
# print(min_num(10, 15, 4, 5, 8, -20, 0))

########################################################################################################
'''13 August 2022'''
'''Anonymous functions
* An anonymous function is a function that is defined without a name.
* While normal functions are defined using the def keyword in Python, anonymous functions are defined 
    using the lambda keyword.
* Syntax: lambda [arg1 [,arg2,...argn]]:expression
'''
'''waf to find the square of a number'''
# def square(n):
#     print(n ** 2)
# square(9)
#
# res = lambda n : n ** 2
# print(res(9))

#######################################################################################
'''waf to add three numbers'''
# add = lambda a, b, c : a + b + c
# print(add(1, 2, 3))
###########################################################################
'''write a lambda function to get last element of iterable'''
# a =  'python'
# def las_ele(n):
#     return n[-1]
# print(las_ele(a))
#
# res = lambda n : n[-1]
# print(res(a))

###########################################################################
'''write a lambda func to get the output of the expression a^2 + b^2 + 2ab'''
# res = lambda a, b : a**2 + b**2 + 2*a*b
# print(res(6, 4))
# print(res(9, 7))
# print(res(8, 9))

###########################################################################
'''write a lambda func to check whether the given num is even or odd'''
# even = lambda n : n%2==0
# print(even(9))      #False
# print(even(8))      #True
#
# even_odd = lambda n: 'even' if n%2==0 else 'odd'
# print(even_odd(2))      #even
# print(even_odd(9))      #odd

#############################################################################

'''write a lambda func to check if the string is palindrome or not'''
# palindrome = lambda n : n==n[::-1]
# print(palindrome('malayalam'))        #True
#
# palindrome = lambda n : 'palindrome' if n==n[::-1] else 'not a palindrome'
# print(palindrome('malayalam'))          #palindrome
#
# palindrome = lambda n : 'palindrome' if n.lower()==n[::-1].lower() else 'not a palindrome'
# print(palindrome('MaLayalaM'))      #palindrome
################################################################################

'''map = map(func, iterable)
* map() applies a function to all the items in an input_list(iterable).
* Syntax: map(function_to_apply, list_of_inputs) ⇒ object
* map() can be applied to more than one list but thelists should have the same length.
* map() will apply its lambda function to the elements of the argument lists, i.e. it first applies
    to the elements with the Oth index, then to the elements with the 1st index until the n-th 
    index is reached
* If the length of the iterables are not same , the length of map object is considered as shortest
    length of all iterables.

'''
# l = ['madam', 'dad', 'hai', 'mom', 'hello', 'malayalam']
# palindrome = lambda n : n==n[::-1]
# print(palindrome(l))
#
# l = ['madam', 'dad', 'hai', 'mom', 'hello', 'malayalam']
# res = map(lambda n : n==n[::-1], l)
# print(res)               #<map object at 0x000001D03EBC3F70>
# print(list(res))        #[True, True, False, True, False, True]
#
# l = ['madam', 'dad', 'hai', 'mom', 'hello', 'malayalam']
# res = map(lambda n : 'palindrome' if n==n[::-1] else 'not a palindrome', l)
# print(res)              #<map object at 0x0000024EA2DE3F70>
# print(list(res))
# ['palindrome', 'palindrome', 'not a palindrome', 'palindrome', 'not a palindrome', 'palindrome']


####################################################################################
'''write a lambda func to check the even odd numbers'''
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_odd = map(lambda n : n % 2== 0, l)
# print(even_odd)         #<map object at 0x0000020A3E123F40>
# print(list(even_odd))   #[False, True, False, True, False, True, False, True, False, True]
#
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_odd = map(lambda n :'even' if n % 2== 0 else 'odd', l)
# print(list(even_odd))   #['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

###################################################################################
'''write a program to square and cube every number in the range(1, 15)'''
# res = map(lambda n : n **2 , range(1,15))
# print(list(res))        #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
#
# res1 = map(lambda n : n**3, range(1,15))
# print(list(res1))       #[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]

##################################################################################
'''write a lambda func of return the list of elements raised to the power of indices using map'''
# a = [9, 7, 5, 3, 1]
# res = map(lambda num : num ** a.index(num), a)
# print(list(res))
#
# res1 = map(lambda num : num[-1] ** num[0], enumerate(a))
# print(list(res1))
# print(list(enumerate(a)))

###############################################################################
'''write a lambda func to convert negative numbers into positive numbers in the range(-10, 10)'''
# res = map(lambda n : abs(n), range(-10, 10))
# print(list(res))

####################################################################################
'''write a lambda func to add elements in both the lists'''
# l1 = [1, 2, 3, 4, 5]
# l2 = [5, 4, 3, 2 ,1]
# res = map(lambda num: num[0] + num[1], zip(l1, l2))
# print(list(res))        #[6, 6, 6, 6, 6]

#########################################################################################
'''16 August 2022'''
'''
Filter: 
* The filter() class in Python takes in a function and an iterable as arguments.
* This offers an elegant way to filter out all the elements of a sequence, for which the function 
    returns True.
* Filter creates a object of elements for which a function returned value will be True.
* Syntax: filter(func, iterable) ⇒ object
* Note:
    Unlike map(), only one iterable is required.
    Also, as only one iterable is required, it's implicit that func must only take one argument.
    Filter passes each element in the iterable through func and returns only the ones that evaluate to true
'''
############################################################################################
'''filter() = filter(function, iterable)'''
'''fetch even and odd numbers from the list'''
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = filter(lambda n : n%2==0, l)
# print(even)     #<filter object at 0x000001B6C5713F40>
# print(list(even))       #[2, 4, 6, 8, 10]
#
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = filter(lambda n : n%2!=0, l)
# print(even)     #<filter object at 0x000001DAE1713EB0>
# print(list(even))       #[1, 3, 5, 7, 9]

#############################################################################################
'''fetch only even length elements from the list using filter'''
# list_1 = ['audi', 'volvo', 'creta', 'ertiga', 'ritz', 'duster', 'kiger']
# res = filter(lambda n : len(n)%2==0, list_1)
# print(res)
# print(list(res))        #['audi', 'ertiga', 'ritz', 'duster']
##############################################################################################
'''wap to print prime numbers from 1-50 using filter'''
# def prime(n):
#     if n > 1:
#         for i in range(2, n):
#             if n%i==0:
#                 return 0
#         else:
#             return 1
#     else:
#         return 0
#
# res = list(filter(prime, range(1, 50)))
# print(res)
#################################################################################
'''wap to calculate the sum of odd numbers and even numbers seperately in the range(1, 30)'''
# even = list(filter(lambda n:n%2==0, range(1, 30)))
# print(even)
# print(sum(even))
#
# odd = list(filter(lambda n:n%2!=0, range(1, 30)))
# print(odd)
# print(sum(odd))

################
# def sum_even(n):
#     if n%2==0:
#         return 1
#     else:
#         return 0
#
# def sum_odd(n):
#     if n%2 !=0 :
#         return 1
#     else:
#         return 0
#
# even_sum = list(filter(sum_even, range(1, 30)))
# print(sum(even_sum))
#
# odd_sum = list(filter(sum_odd, range(1, 30)))
# print(sum(odd_sum))
############################################################################################
'''waf to search for a character in the string and return its corresponding index'''
'''without using inbuilt method'''
# s = 'all the stars are closer'
# def search_char(n):
#     for index, item in enumerate(s):
#         if n == item:
#             print(item, index)
#     else:
#         print('Item not found')
# search_char('s')
# search_char('z')

'''using inbuilt method'''
# s = 'all the stars are closer'
# def search_char(n):
#     if s.find(n) != -1:
#         print(s.find(n))
#     else:
#         print('Item not found')
#
# search_char('s')
# search_char('z')

#######################################################################################
'''
RECURSIONS
* It is function which calls itself until the condition is being satisfied.
* Used to avoid loops in some cases.

Note : 
* Python recursion limit can be found out with a function from the sys module called getrecursionlimit():
* By default the recursion limit will be 1000
* This can reset to any value with a function from the sys module called setrecursionlimit( new_limit ).

Recursive functions typically follow this pattern:
* There are one or more base cases that are directly solvable without the need for further recursion.
* Each recursive call moves the solution progressively closer to a base case.
'''
##########################################################################################
# for i in range(5, 0, -1):
#     print(i)

# count = 5
# while count > 0:
#     print(count)
#     count -= 1

# def num(i):
#     print(i)
#
# num(5)
# num(4)
# num(3)
# num(2)
# num(1)

# def numbers(i):
#     print(i)
#
# for i in range(5, 0, -1):
#     numbers(i)

# def numbers(n):
#     for i in range(n, 0, -1):
#         print(i)
# numbers(5)

'''write a recursion to print numbers from 5-1'''
# def num(n):
#     if n > 0:
#         print(n)
#         num(n-1)
#     else:
#         return
#
# num(5)

###################################################################################################
'''write a recursion to print numbers from 1-10'''
# def numbers(n):
#     if n<11:
#         print(n)
#         numbers(n+1)
#     else:
#         return
#
# numbers(1)

####################################################################################################
'''the maximum depth of recursion is 1000'''
# import sys
# print(sys.getrecursionlimit())      #1000
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())      #2000

############################################################################################
'''write a recursion function to find the factorial of a number'''
# def fact(n):
#     if n <= 0:
#         return 'invalid input'
#     elif n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
# print(fact(5))

############################################################
'''recursion to find the sum of first n numbers'''
# def sum_num(n):
#     if n <= 0:
#         return 'invalid input'
#     elif n == 1:
#         return 1
#     else:
#         return n + sum_num(n-1)
#
# print(sum_num(10))

######################################################################################
'''recursion to reverse a string'''
# def reverse(n):
#     if len(n) == 0:
#         return n
#     elif len(n) == 1:
#         return n
#     else:
#         return reverse(n[1::]) + n[0]
#
# print(reverse('java'))

#############################################################################
'''recursion to find the sum of all numbers in the list'''
# l = [11, 9, 67, 54, 23]
# def sum_list(n):
#     if len(n) == 1:
#         return n[0]
#     else:
#         return n[0] + sum_list(n[1::])
#
# print(sum_list(l))

############################################################################################
'''recursion to print the fibonacci'''
# def fib(n):
#     if n==0:
#         return n
#     elif n==1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#
# print(fib(5))

#############################################################################################
'''18 August 2022'''
'''Variable Scopes'''
# a = 10
# def spam():
#     a += 2
#     print(a)
#
# spam()      #UnboundLocalError

##########################################################
'''write'''
# a = 10
# def spam():
#     a = 20
#     print(a)        #20
#
# spam()
# print(a)        #10
############################################################
'''write'''
# a = 10
# def spam():
#     a = 20
#     a += 2
#     print(a)            #22
#
# spam()
# print(a)                #10

#################################################################
'''global :
* A variable created in global namespace i.e., outside a function.
* It can only be accessed inside a function but cannot be modified.
* In order to modify a global variable inside a function then we need to use global keyword.'''
# a = 10
# def spam():
#     global a
#     a += 2
#     print(a)        #12
#
# print(a)                #10
# spam()
# print(a)            #12
##############################################################
'''local variable : 
A variable which is created inside a function is called a local variable and it cannot be accessed 
outside the function.
Eg: 	def function():
			a = 10 			# local variable
		print(a) 			#Error'''
# a = 10
# def spam():
#     a = 20
#     a += 2
#     print(a)            #22
# print(a)            #10
# spam()
# print(a)                #10

####################################################################
'''non-local :
* Non local scopes are those which are neither local nor global.
* If a nested function has to access and modify the variable of outer function, nonlocal keyword 
    should be used.'''
# a = 10
# def spam():
#     b = 20
#     def inner():
#         print(b)        #20
#         print(a)        #10
#     inner()
# spam()
#
#
# a = 10
# def spam():
#     b = 20
#     def inner():
#         global a
#         a += 15
#         print(b)        #20
#         print(a)        #25
#     inner()
# spam()

# a = 10
# def spam():
#     b = 20
#     def inner():
#         nonlocal b
#         b += 15
#         print(b)        #35
#         print(a)        #10
#     inner()
# spam()
#
# a = 10
# def spam():
#     b = 20
#     def inner():
#         nonlocal b
#         global a
#         a += 15
#         b += 15
#         print(b)        #35
#         print(a)        #25
#     inner()
# spam()

##################################################################################
'''sorted() = sorted(iterable, [key=None], [reverse=False])
* Syntax : sorted(iterable, *, key=None, reverse=False) ⇒ list
* Returns a new sorted list from the items in iterable.
* Has two optional arguments which must be specified as keyword arguments.
* key: It specifies a function of one argument that is used to extract a comparison key,
    from each element in iterable (for example, key=len). 
    The default value is None (compare the elements directly).
* Reverse: It is a boolean value. If set to True(descending , then the list elements are sorted as 
    if each comparison were reversed. 
'''
# a = [9, 3, 1, 5, 2, 6, 8]
# a.sort()
# print(a)
#
# a = 'python'
# l = sorted(a)      #['h', 'n', 'o', 'p', 't', 'y']
# print(''.join(l))   #hnopty
#
# a = 'hello python'
# print(sorted(a))        #[' ', 'e', 'h', 'h', 'l', 'l', 'n', 'o', 'o', 'p', 't', 'y']
#
# l1 = ['i', 'l', 'e', 'z', 'a', 'j', 'w', 'q', 'r']
# print(sorted(l1))       #['a', 'e', 'i', 'j', 'l', 'q', 'r', 'w', 'z']
# print(l1)               #['i', 'l', 'e', 'z', 'a', 'j', 'w', 'q', 'r']
#
# l2 = ['i', 'l', 'e', 'z', 'a', 'j', 'w', 'q', 'r']
# l2.sort()
# print(l2)               #['a', 'e', 'i', 'j', 'l', 'q', 'r', 'w', 'z']

'''NOTE : Sort method will modify the original list only, but the sorted function will give you a new list'''

# tup = ('i', 'l', 'e', 'z', 'a', 'j', 'w', 'q', 'r')
# print(sorted(tup))          #['a', 'e', 'i', 'j', 'l', 'q', 'r', 'w', 'z']
#
# set1 = {'i', 'l', 'e', 'z', 'a', 'j', 'w', 'q', 'r'}
# print(sorted(set1))     #['a', 'e', 'i', 'j', 'l', 'q', 'r', 'w', 'z']
#
# '''sorting a dictionary'''
# d = {'green':5, 'lavender':8, 'red':3, 'blue':4, 'yellow':6, 'white':5}
# res = sorted(d)
# print(res)          #['blue', 'green', 'lavender', 'red', 'white', 'yellow']
#
# res1 = sorted(d.keys())
# print(res1)         #['blue', 'green', 'lavender', 'red', 'white', 'yellow']
#
# res1 = sorted(d.values())
# print(res1)     #[3, 4, 5, 5, 6, 8]
#
# res1 = sorted(d.items())
# print(res1)     #[('blue', 4), ('green', 5), ('lavender', 8), ('red', 3), ('white', 5), ('yellow', 6)]

###########################################################################################
'''write a program to sort a set of names based of length of each name'''
# l1 = {'anurag', 'archana', 'vijay', 'mukeshram', 'radhikagupta', 'praveen', 'smitamishra', 'nandini'}
# print(sorted(l1))   #['anurag', 'archana', 'mukeshram', 'nandini', 'praveen', 'radhikagupta', 'smitamishra', 'vijay']
# print(sorted(l1, key=len))  #['vijay', 'anurag', 'archana', 'nandini', 'praveen', 'mukeshram', 'smitamishra', 'radhikagupta']
# print(sorted(l1, key=len, reverse=True))    #['radhikagupta', 'smitamishra', 'mukeshram', 'archana', 'nandini', 'praveen', 'anurag', 'vijay']

#######################################################################################
'''write a program to sort a list based on last character of eaach name'''
# l1 = {'anurag', 'archanakiran', 'vijay', 'mukeshram', 'radhikagupta', 'praveen', 'smitamishra', 'nandini'}
# def last_char(char):
#     return char[-1]
# print(sorted(l1, key=last_char))    #['radhikagupta', 'smitamishra', 'anurag', 'nandini', 'mukeshram', 'archanakiran', 'praveen', 'vijay']
#
# '''using lambda function'''
# print(sorted(l1, key=lambda n:n[-1]))   #['radhikagupta', 'smitamishra', 'anurag', 'nandini', 'mukeshram', 'archanakiran', 'praveen', 'vijay']

################################################################################################
'''19 August 2022'''
'''sort the below list based on temperature'''
# temp = [('bangalore', 25), ('mysore', 27), ('shimoga', 20), ('hubli', 30), ('tumkur', 21)]
# print(sorted(temp))     #[('bangalore', 25), ('hubli', 30), ('mysore', 27), ('shimoga', 20), ('tumkur', 21)]
# print(sorted(temp, key=lambda n:n[-1]))     #[('shimoga', 20), ('tumkur', 21), ('bangalore', 25), ('mysore', 27), ('hubli', 30)]
#
# def temp1(n):
#     return n[-1]
# print(sorted(temp, key=temp1))  #[('shimoga', 20), ('tumkur', 21), ('bangalore', 25), ('mysore', 27), ('hubli', 30)]

#######################################################################################################
'''sort the below dictionary based on their share prices'''
# d = {'zeel':250, 'itc':280, 'idea':9, 'bhartiairtel':750, 'tatamotors':340, 'adanipower':150}
# print(sorted(d.items(), key=lambda n:n[-1]))    #[('idea', 9), ('adanipower', 150), ('zeel', 250), ('itc', 280), ('tatamotors', 340), ('bhartiairtel', 750)]
#
# def share_price(n):
#     return n[-1]
# print(sorted(d.items(), key=share_price))   #[('idea', 9), ('adanipower', 150), ('zeel', 250), ('itc', 280), ('tatamotors', 340), ('bhartiairtel', 750)]

#################################################################################################
'''write a program to get the most repeated letter in the word'''
# a = 'she sells seashells on the seashore'
# d = {}
# for i in a:
#     d[i] = a.count(i)
# *res, most_repeated = sorted(d.items(), key=lambda n:n[-1])
# print(res)      #[('n', 1), ('t', 1), ('r', 1), ('a', 2), ('o', 2), ('h', 4), ('l', 4), (' ', 5), ('e', 7)]
# print(most_repeated)        #('s', 8)

# a = 'she sells seashells on the seashore'
# d = {}
# for i in a:
#     d[i] = a.count(i)
# res= sorted(d.items(), key=lambda n:n[-1], reverse=True)
# print(res[0])     #('s', 8)
#
# a = 'she sells seashells on the seashore'
# d = {}
# for i in a:
#     d[i] = a.count(i)
# res= sorted(d.items(), key=lambda n:n[-1])
# print(res[-1])      #('s', 8)

###############################################################################
'''wap to find the longest word along with it's length'''
# s = 'as you can see I am still sleeeeeeepy'
# d = {}
# for i in s.split():
#     d[i] = len(i)
# res = sorted(d.items(), key=lambda n:n[-1])
# print(res[-1])      #('sleeeeeeepy', 11)

###############################################################################
'''sorting a list based on names'''
# students = [{'name':'Sita', 'grade':'B', 'age':10}, {'name':'Ravan', 'grade':'A', 'age':15},
#             {'name':'Ram', 'grade':'C', 'age':13}, {'name':'Lakshman', 'grade':'D', 'age':9}]
# print(sorted(students, key=lambda item : item['name']))
# #[{'name': 'Lakshman', 'grade': 'D', 'age': 9}, {'name': 'Ram', 'grade': 'C', 'age': 13}, {'name': 'Ravan', 'grade': 'A', 'age': 15}, {'name': 'Sita', 'grade': 'B', 'age': 10}]
#
# print(sorted(students, key=lambda item : item['age']))
# #[{'name': 'Lakshman', 'grade': 'D', 'age': 9}, {'name': 'Sita', 'grade': 'B', 'age': 10}, {'name': 'Ram', 'grade': 'C', 'age': 13}, {'name': 'Ravan', 'grade': 'A', 'age': 15}]
#
# print(sorted(students, key=lambda item : item['grade']))
# #[{'name': 'Ravan', 'grade': 'A', 'age': 15}, {'name': 'Sita', 'grade': 'B', 'age': 10}, {'name': 'Ram', 'grade': 'C', 'age': 13}, {'name': 'Lakshman', 'grade': 'D', 'age': 9}]

####################################################################################
'''package architecture'''
'''
MODULES
* A module is a file consisting of Python code.
* It can have functions, classes, and variables.
* Any Python file can be referenced as a module.
* Types of Modules:
    Built-in modules:
    Predefined modules
    Ex: re(regular expression), itertools, collections, copy 

User defined modules:
* Created by user.
* Can be accessed using import statement.
* Syntax: import module_name

import keyword
* Used to import modules in any programs.
* It can be written anywhere in the module.
* Any number of modules can be imported in a module.
* Syntax: import module_name

from keyword
* It is used when we need to import some module from different package.
* Syntax:
    from module_name import function
    from package_name import module_name
    from package_name.module_name import function

as keyword
* Used to give an alias name for the module as well as function.
* Syntax:
    from module_name import function as alias_name
    from package _name import module name as alias_name
    from package_name.module_name import function as alias _name
'''
####################################################################################
'''22 August 2022'''
'''File handeling : 
* Files are named locations on disk to store related information.
* When we want to read from or write to a file, we need to open it first.
* When we are done, it needs to be closed so that the resources that are tied with the file are freed.
* Hence, in Python, a file operation takes place in the following order:
    Open a file
    Read or write (perform operation)
    Close the file

##############################
Opening a file
In python, files can be opened in two ways,:
Without context manager:
	file_obj = open(filename, mode)
With context manager
	with open(filename, mode) as file_ob:
			pass

Note: when we open file without context manager, then we need to close the file explicitly.
 But with context manager, we can just exit out of the block to close the file.
'''
##############################################################################
'''without context manager = open(filename, mode)'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\fastrack_2\example_.py'
# file = open(f_path)
# print(file)
# print(file.closed)      #False
# file.close()
# print(file.closed)      #True

'''with context manager'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\example_pack\example_.py'
# with open(f_path) as file_name:
#     # print(file_name)
#     print(file_name.closed)         #False
# print(file_name.closed)     #True

'''
MODES: 
There are four different methods (modes) for opening a file:
    "r”- Read (Default value). Opens a file for reading, error if the file does not exist.
    "a" - Append. Opens a file for appending, creates the file if it does not exist. In this mode the data
        present in previously is preserved.
    "w"- Write Opens a file for writing, creates the file if it does not exist(overrides the content of 
        file if already exists)
    "x" Create - Creates the specified file, returns an error if the file exist
'''

'''read mode = r'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\example_pack\ex10.py'
# file = open(f_path, 'r')
# print(file)
#
# file1= open('f_path123', 'r')
# print(file1)

'''If the file is not present and we try to read it, it will give us FileNotFoundError'''

###############################################################
'''write mode = w'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\example_pack\ex10.py'
# file = open(f_path, 'w')
# print(file)
#
# f1 = open('file1234.py', 'w')
# print(f1)

#####################################################################
'''append mode = a'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\example_pack\ex10.py'
# file = open(f_path, 'a')
# print(file)
#
# file = open('file1234.py', 'a')
# print(file)
'''If the file is not present, write mode and append mode will not give us error,
instead it will create a new file'''

##########################################################################
'''create mode = x'''
# file = open('filename1234.py', 'x')
# print(file)
#
# file1 = open('myfile1.py', 'x')
# print(file1)        #FileExistsError
'''If the file is already pesent, it'll throw FileExistsError'''

#############################################################################
'''file attributes
file.closed : Returns true if file is closed, false otherwise.
file.mode : Returns access mode with which file was opened.
file.name : Returns name of the file
file.readable(): Return true if file is opened in read mode.
file.writable(): Return true if file is opened in write mode.
file.close(): closes the file.
file.open() : opens the file
'''

# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\example_pack\ex10.py'
# with open(f_path) as file:
#     print(file.mode)            #r
#     print(file.name)            #filepath
#     print(file.readable())      #True
#     print(file.writable())      #False

##################################################################################
'''23 August 2022'''
'''Reading from a file
* By default files will be opened in "r" mode.
* Syntax :
    file = open("demo.txt", "r")
    with open("demo.txt") as file:
		pass

* Methods to perform read operation:
    read()
    readline()
    readlines()'''
'''read() : Reads the data from starting to end of the file:'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path, 'r') as file:
#     print(file.read())
###################################################################
'''readline() : reads a single line from the file.'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path, 'r') as file:
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
####################################################################
'''readlines() : returns entire text_1 in the form of list separating each line as an element'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path, 'r') as file:
#     print(file.readlines())
#     print(file.readlines())


# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path, 'r') as file:
#     print(file.read(10))
#     print(file.read(10))
#
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path, 'r') as file:
#     print(file.readline(10))
#     print(file.readline(10))
#     print(file.readline(10))
#
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path, 'r') as file:
#     print(file.readlines(4))
#     print(file.readlines(40))

############################################################################################
'''wap to count the number of lines in a file'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     count = 0
#     for i in file:
#         count += 1
#     print(count)
#
#######################################################################################
'''wap to print lines along with their line number'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         print(count, line)
#
#
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     for line_no, line in enumerate(file, start=1):
#         print(line_no, line)

############################################################################################
'''wap to read a file in reversed order'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     for line in reversed(list(file)):
#         print(line)

#############################################################
'''wap to read a file in reversed order'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     for line in reversed(list(file)):
#         for i in reversed(line):
#             print(i, end='')

# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     for line in reversed(list(file)):
#         for i in reversed(line.split()):
#             print(i, end='')
#         print()
#############################################################################
'''August 24 2022'''
'''wap to read 10 characters at a time'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     print(file.read(10))
#
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     for line in file:
#         print(file.read(10))
################################################################################################
'''wap to find the number of characters in each line'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     for line in file:
#         count = 0
#         for i in line:
#             count += 1
#         print(count)
#################################################################################
'''wap to find the number of words present in each line'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     for i in file:
#         count = 0
#         for j in i.split():
#             count += 1
#         print(count)


# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     for i in file:
#         print(len(i.split()))
#####################################################################################
'''wap to extract IP addresses from access-log.txt file'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\access-log.txt'
# with open(f_path) as file:
#     for line in file:
#         if line.strip():
#             a = line.split()
#             print(a[0])
#
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\access-log.txt'
# with open(f_path) as file:
#     for line in file:
#         if len(line.split()) != 0:
#             print(line.split()[0])
###################################################################################
'''create a dict of IP addresses and its count pair'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\access-log.txt'
# with open(f_path) as file:
#     d = {}
#     l = []
#     for line in file:
#         if line.strip():
#             a = line.split()
#             l.append(a[0])
#             d[a[0]] = l.count(a[0])
#     print(d)

# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\access-log.txt'
# with open(f_path) as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             a = line.split()
#             if a[0] in d:
#                 d[a[0]] += 1
#             else:
#                 d[a[0]] = 1
#     print(d)


# from collections import defaultdict
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\access-log.txt'
# with open(f_path) as file:
#     def_dict = defaultdict(int)
#     for line in file:
#         if line.strip():
#             a = line.split()
#             def_dict[a[0]] += 1
#     print(def_dict)

#########################################################################################
'''wap to extract the msgs from sample.log file'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample.log'
# with open(f_path) as file:
#     for line in file:
#         if line.strip():
#             a = line.split()
#             print(a[2])

'''dict of msg and its count pair'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample.log'
# with open(f_path) as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             a = line.split()
#             if a[2] in d:
#                 d[a[2]] += 1
#             else:
#                 d[a[2]] = 1
#     print(d)
#
# from collections import defaultdict
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample.log'
# with open(f_path) as file:
#     def_dict = defaultdict(int)
#     for line in file:
#         if line.strip():
#             a = line.split()
#             def_dict[a[2]] += 1
#     print(def_dict)


####################################################################################
'''wap to get the country names from football.txt file'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\football.txt'
# with open(f_path, encoding='UTF-8') as file:
#     for line in file:
#         if line.strip():
#             a = line.split()
#             print(a[1])

###################################################################################
'''wap to print the most occuring country name along with count'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\football.txt'
# with open(f_path, encoding='UTF-8') as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             a = line.split()
#             if a[1] in d:
#                 d[a[1]] += 1
#             else:
#                 d[a[1]] = 1
#     res = sorted(d.items(), key=lambda n:n[-1])
#     print(res[-1])

##############
# from collections import Counter
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\football.txt'
# with open(f_path, encoding='UTF-8') as file:
#     l = []
#     for line in file:
#         if line.strip():
#             a = line.split()
#             l.append(a[1])
#             count = Counter(l)
#     res = count.most_common()
#     print(res[0])

#############################################################################
'''25 August 2022'''
'''wap to find the line number of a particular word in a file'''
# string = input('Enter the word: ')
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     for line_no, line in enumerate(file, start=1):
#         if string in line:
#             print(f'{line_no} - {line}')

###########################################################################
'''create a dict, group as a key and the list of countries belonging to that group as value'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\football.txt'
# with open(f_path, encoding='UTF-8') as file:
#     d = {}
#     for line_no, line in enumerate(file, start=1):
#         if line_no == 1:
#             continue
#         else:
#             a = line.split()
#             group = a[0]
#             country = a[1]
#
#         if group not in d:
#             d[group] = [country]
#         elif country not in d[group]:
#             d[group] += [country]
#
#     print(d)

###############################################################
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     print(file.read(10))
#
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     print(file.read(25))

'''seek(position) : It takes the cursor to the position specified'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     print(file.read(25))
#     file.seek(0)
#     print(file.read(25))

'''tell() 
* It has no arguments
* It returns the current position of the cursor in the file'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     print(file.read(25))
#     print(file.read(4))
#     print(file.read(16))
#     print(file.tell())
###########################################################################
'''Methods to write into a file
1. write()
2. writelines()

* To write we need to use "w" mode or “a” mode.
    Syntax: 
        file = open("demo.txt", "w")
        with open("demo.txt" "w") as file:

Functions to perform write operation:
* write():  Writes the data into the file.
            Data must be a string.
            Returns the number of characters written in the files

* writelines(): write an iterable data into file.(list,tuple or dictionary)
            Data must has string as its elements.
            Returns None.

'''
'''write()'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\WPYM14\myfile1.py'
# with open(f_path, 'w') as file:
#     print(file.write('Tomorrow is just an another day\n'))
#     print(file.write('Monday blues'))
#
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\WPYM14\myfile1.py'
# with open(f_path, 'w') as file:
#     print(file.write('Monday blues', 'Tuesday hues'))   #TypeError, Can't pass multiple arguments

'''writelines()'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\WPYM14\myfile1.py'
# with open(f_path, 'w') as file:
#     file.writelines(['Croatia\n', 'Chile\n', 'Mexico\n', 'Spain\n'])

################################################################################
'''CSV file handeling = Comma Seperated Value
OVERVIEW
* CSV (Comma Separated Values) is a simple file format used to store tabular data such as a spreadsheet 
    or database.
* A CSV file stores tabular data (numbers and text_1) in plain text_1.
* Each line of the file is a data record.
* Each record consists of one or more fields, separated by commas.

* For working CSV files in python, there is an inbuilt module named csv.
	i.e  import csv
################################################################
There are 2 methods:
csv.reader(csv_file)
csv.DictReader(csv_file)'''
#########################################################################
'''reader() : Using reader():	
        with open(csv_file, “r”) as file:
		    rows = csv.reader(file)'''
# import csv
# f_path = r"C:\Users\Ramya\OneDrive\Desktop\example1.csv"
# with open(f_path) as file:
#     result = csv.reader(file)
#     print(result)       #<_csv.reader object at 0x000001F155B5C400>
#     for i in result:
#         print(i)

'''NOTE : reader is an iterator object which holds each data record in the form of python list'''

################################################################################
'''dictreader : 
        with open(filename, “r”) as csv_ file:
		    rows = csv.DictReader(csv file)
'''
# import csv
# f_path = r"C:\Users\Ramya\OneDrive\Desktop\example1.csv"
# with open(f_path) as file:
#     result = csv.DictReader(file)
#     print(result)       #<csv.DictReader object at 0x0000024CC87C3F10>
#     for i in result:
#         print(i)

'''NOTE : DictReader is an iterator object which holds each data record in the form of python dictionary'''

#################################################################################################
'''26 August 2022'''
'''wap to extract total vaccination of all countries'''
# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\vaccination_data.csv'
# with open(f_path) as file:
#     for i in file:
#         a = i.split(',')
#         print(a[5])
#
# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\vaccination_data.csv'
# with open(f_path) as file:
#     fileobj = csv.reader(file)
#     print(fileobj)      #<_csv.reader object at 0x00000244B6F7C1C0>
#     for line in fileobj:
#         print(line[5])
#
# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\vaccination_data.csv'
# with open(f_path) as file:
#     fileobj = csv.DictReader(file)
#     print(fileobj)      #<csv.DictReader object at 0x0000026717753F10>
#     for line in fileobj:
#         print(line['TOTAL_VACCINATIONS'])

#########################################################################################
'''Total vaccinations given'''
# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\vaccination_data.csv'
# with open(f_path) as file:
#     total_vaccination = 0
#     fileobj = csv.reader(file)
#     for line in fileobj:
#         if line[5].isnumeric():
#             total_vaccination += int(line[5])
#     print(total_vaccination)
#
# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\vaccination_data.csv'
# with open(f_path) as file:
#     total_vaccination = 0
#     fileobj = csv.DictReader(file)
#     print(fileobj)
# for line in fileobj:
#     if line['TOTAL_VACCINATIONS'].strip():
#         total_vaccination += int(line['TOTAL_VACCINATIONS'])
# print(total_vaccination)
##########################################################################################
'''wap to extract country and who region from the vaccination data'''
# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\vaccination_data.csv'
# with open(f_path) as file:
#     reader_obj = csv.reader(file)
#     for i in reader_obj:
#         print(f'{i[0]} - {i[2]}')

# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\vaccination_data.csv'
# with open(f_path) as file:
#     reader_obj = csv.DictReader(file)
#     for i in reader_obj:
#         print(i['COUNTRY'], '-', i['WHO_REGION'])

###########################################################################
'''wap to extract countries with less than 10000 vaccinated people'''
# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\vaccination_data.csv'
# with open(f_path) as file:
#     reader_obj = csv.reader(file)
#     for i in reader_obj:
#         if i[5].isnumeric():
#             if int(i[5]) < 10000:
#                 print(i[0])

# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\vaccination_data.csv'
# with open(f_path) as file:
#     reader_obj = csv.DictReader(file)
#     for i in reader_obj:
#         if i['TOTAL_VACCINATIONS'].strip():
#             if int(i['TOTAL_VACCINATIONS']) < 10000:
#                 print(i['COUNTRY'])

############################################################################################
'''Writing into CSV files
There are 2 methods:
    * csv.writer(csv_file)
    * csv.DictWriter(csv_file, fieldnames)

Note: Below are some supporting methods to write data into csv file,
* writer_obj.writerow(): writes a single data into csv file. Data can be a list or dictionary
* writer_obj.writerows(): writes multiple data into csv file. Data should be list of iterables.
* writer_obj.writeheader(): writes header in the file using the field names specified.
'''

'''writerow()'''
# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\WPYM14\myfile1.py'
# with open(f_path, 'w') as csv_write_file:
#     csv_obj = csv.writer(csv_write_file)
#     csv_obj.writerow(['python', 'java', 'selenium'])
#
################################################################
'''writerows()'''
# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\WPYM14\myfile1.py'
# with open(f_path, 'w') as csv_write_file:
#     csv_obj = csv.writer(csv_write_file)
#     csv_obj.writerows([['python', 'java', 'selenium'], [10, 20, 30], [1, 2, 3]])

###################################################################
# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\WPYM14\myfile1.py'
# with open(f_path, 'w') as csv_write_file:
#     csv_obj = csv.DictWriter(csv_write_file, ['a', 'b', 'c'])
#     csv_obj.writerow({'a':10, 'b':20, 'c':30})

#######################################################
# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\WPYM14\myfile1.py'
# with open(f_path, 'w') as csv_write_file:
#     csv_obj = csv.DictWriter(csv_write_file, ['a', 'b', 'c'])
#     csv_obj.writeheader()
#     csv_obj.writerow({'a':10, 'b':20, 'c':30})

########################################################
# import csv
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\WPYM14\myfile1.py'
# with open(f_path, 'w') as csv_write_file:
#     csv_obj = csv.DictWriter(csv_write_file, ['a', 'b', 'c'])
#     csv_obj.writeheader()
#     csv_obj.writerows([{'a':10, 'b':20, 'c':30}, {'a':100, 'b':200, 'c':300}])

############################################################################################
'''27 August 2022'''
'''Generators : 
* Python generator is used to create python iterators.
* This is done by defining a function but instead of the return statement returning from the function, 
    use the "yield" keyword. 
* A generator is similar to a function returning an array. 


FEATURES OF GENERATORS
* A Generator is a function that returns an iterator. It generates values using the 'yield' keyword.
* They don't take memory of a list. They are LAZY Iterables. Generators are used for saving memory.
* When called on next() function, it raises StopIteration exception when there are no more values to generate.
* 'yield' keyword suspends or pauses the execution of the function. But 'return' statement ends the function.


DIFFERENCE BETWEEN YIELD AND RETURN
    RETURN                                                      YIELD
* Stops the execution                                   * Pauses the execution
* Cannot return to the function block                   * Can return to the function block
* Multiple return statements cannot be                  * Multiple yield keywords can be written in a function
    written in a function
* Can return multiple elements                          * Can return multiple elements
'''

# def greeting():
#     return 'hello world'
#     return 'good moring'
#     return 'good evening'
#
# print(greeting())

# def greeting():
#     return 'hello world', 'good morning', 'good evening'
#
# print(greeting())

# def greeting():
#     yield 'good morning'
#     yield 'good evening'
#     yield 'hello world'
#     yield 'hey python'
#
#
# res = greeting()       #<generator object greeting at 0x000001BC05F8F8B0>
# for i in res:
#     print(i)
#
# res1 = greeting()
# print(list(res1))       #['good morning', 'good evening', 'hello world', 'hey python']
#
# res2 = greeting()
# print(res2)
# print(next(res2))       #good morning
# print(next(res2))       #good evening
# print(next(res2))       #hello world
# print(next(res2))       #hey python
# print(next(res2))       #StopIteration


# def spam():
#     return 'hey python', 'hey India', 'world'
#
# s = spam()
# print(dir(s))       #, __iter__, __len__
# print(next(s))      #TypeError: 'tuple' object is not an iterator

# def func():
#     yield 'hello world'
#
# res = func()
# print(dir(res))     #'__iter__', __next__

######################################################################################
'''write a generator func which yields names starting with vowels'''
'''generator function'''
# names = ['amazon', 'flipkart', 'ajio', 'uber', 'myntra', 'ola', 'urbanic']
# def starting_with_vowels(n):
#     for name in n:
#         if name[0] in 'aeiouAEIOU':
#             yield name
#
# res = starting_with_vowels(names)
# print(res)      #<generator object starting_with_vowels at 0x000002232243F990>
# for i in res:
#     print(i)


'''generator expression'''
# vowels = (name for name in names if name[0] in 'aeiouAEIOU')
# print(vowels)       #<generator object <genexpr> at 0x0000022C9301F990>
# print(next(vowels))     #amazon
# print(next(vowels))     #ajio
# print()
# for i in vowels:
#     print(i)

#####################################################################################
'''write a generator func to print numbers from 10 - 1'''
# def numbers(n):
#     for i in range(n, 0, -1):
#         yield i
#
# res = numbers(10)
# print(res)
# print(next(res))
#
#
# res1 = (i for i in range(10, 0, -1))
# for i in res1:
#     print(i)
############################################################################################
'''write a generator func and expression to extract all the names which are of even length
    names = ['amazon', 'flipkart', 'ajio', 'uber', 'myntra', 'ola', 'urbanic']'''
'''write a generator func and expression to extract the names ending with vowels'''
'''write a generator func and expression to create a list of tuples of word and its length pair
    names = ['amazon', 'flipkart', 'ajio', 'uber', 'myntra', 'ola', 'urbanic']'''
'''write a generator func and expression to reverse item of list if its of odd length, else retain as it is
    names = ['amazon', 'flipkart', 'ajio', 'uber', 'myntra', 'ola', 'urbanic']'''

# names = ['amazon','flipkart','ajio','uber','myntra','ola','urbanic']
# def even_length_names(listOfNames):
#     for i in listOfNames:
#         if len(i) % 2 == 0:
#             yield i
#
# res = even_length_names(names)
# for i in res:
#     print(i)

###############################################################################
'''29 August 2022'''
'''write a generator func to yield one line at a time from the file'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     print(file.readline())

'''generator function'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# def one_line(file_path):
#     with open(file_path) as file:
#         for line in file:
#             yield line
#
# result = one_line(f_path)
# print(result)       #<generator object one_line at 0x000001B05724FB50>
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

'''generator expression'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample1.txt'
# with open(f_path) as file:
#     result = (line for line in file)
#     print(result)
#     print(next(result))

#######################################################################################
'''write a generator function ,expression to print the lines which has TRACE in it in sample.log file'''
'''generator function'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample.log'
# def gen_func(file_path):
#     with open(file_path) as file:
#         for line in file:
#             if 'TRACE' in line:
#                 yield line
#
# result = gen_func(f_path)
# for i in result:
#     print(i)

'''generator expression'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample.log'
# with open(f_path) as file:
#     result = (line for line in file if 'TRACE' in line)
#     for i in result:
#         print(i)

#####################################################################################
'''wap to count the TRACE in sample.log file'''
'''generator function'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample.log'
# def count_trace(file_path):
#     with open(file_path) as file:
#         count = 0
#         for line in file:
#             if line.strip():
#                 if 'TRACE' in line:
#                     count += 1
#         yield count
#
# res = count_trace(f_path)
# print(next(res))

# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample.log'
# def count_trace(file_path):
#     with open(file_path) as file:
#         count = 0
#         for line in file:
#             if line.strip():
#                 line_split = line.split()
#                 if line_split[2] == 'TRACE':
#                     count += 1
#         yield count
#
# res = count_trace(f_path)
# print(next(res))

'''generator expression'''
# f_path = r'C:\Users\Ramya\PycharmProjects\pythonProject\myfiles\sample.log'
# res = (1 for line in open(f_path) if line.strip() if line.split()[2]=='TRACE')
# print(sum(res))

##############################################################################################
'''
DECORATORS
First class objects
* First Class objects are the one which is treated as any other object in Python like strings, 
    lists dicts etc.
* You can pass a function to another function, you can return a function from another function, just
    like any other functions.
* A Decorator is a function, which takes another function as an argument, adds some extra functionality,
    and returns another function without altering the source code of original function.

DECORATORS
* A decorator takes in a function, adds some functionality and returns it.
* This is also called metaprogramming because a part of the program tries to modify another part of 
    the program at compile time.
* A single decorator can decorate any number of functions.

Types:
Built in decorators : @classmethod, @staticmethod, @property,
					@abstractmethod
User defined decorator : created by users.

'''
#####################################################################################
'''
Given an integer n, perform the following conditional actions.
    o If n is odd , print Bangalore
    o If n is even and in the inclusive range of 2 to 9, print Pune.
    o If n is even and in the inclusive range of 10 to 20, print Bangalore.
    o If n is even and greater than 20, print Pune.
    o Note: choose n between 1 to 100.

WAP to read month number from the user and print how many days in that month.(print invalid if user 
gives other than 1-12).

Wap to accept the cost price of a bike and display the road tax
to be paid according to the following criteria :
Cost price (in Rs)                  Tax
 > 100000                           15%
 > 50000 and <= 100000              10%
 <= 50000                           5%

A company decided to give hike to employee according to following criteria:
    * Time period of Service hike
    * More than 10 years 10%
    * >=6 and <=10 8%
    * Less than 6 years 5%
    * Less than year No hike
Ask user for their salary and years of service and print the net bonus amount and also total salary

Accept the kilo meters covered and calculate the bill accordingto the following criteria:
 * First 10 Km Rs11/km
 * Next 90Km Rs10/km
 * After that Rs9/km 
'''

#####################################################################################################
'''September 1 2022'''
'''Decorators'''

# def spam():
#     print('In spam')
#
#
# def rev_str(n):
#     print(n[::-1])
#
# spam()
# rev_str('python')
#
# def add(a, b):
#     print(a + b)
#
# spam()
# add(2, 3)
# spam()
# add(8, 7)

####################################################
# def spam(func):
#     print('In spam')
#     func('python')
#
# def rev_str(n):
#     print(n[::-1])
#
# def add(a, b):
#     print(a + b)
#
#
# spam(rev_str)

############################################################
# def spam(func, *args, **kwargs):
#     print('In spam')
#     func(*args, **kwargs)
#
# def rev_str(n):
#     print(n[::-1])
#
# def add(a, b):
#     print(a + b)
#
# spam(rev_str, 'python')
# spam(add, a=14, b=6)

###################################################
# def spam(func):
#     def wrapper(*args, **kwargs):
#         print('In spam')
#         func(*args, **kwargs)
#     return wrapper
#
# def rev_str(n):
#     print(n[::-1])
#
# def add(a, b):
#     print(a + b)
#
# rev_str = spam(rev_str)
# rev_str('python')
# add = spam(add)
# add(2, 3)

########################################################################
# def outer(func):
#     def wrapper(*args, **kwargs):
#         print('In spam')
#         func(*args, **kwargs)
#         print('decorator executed')
#     return wrapper
#
# @outer      #rev_str = outer(rev_str)
# def rev_str(n):
#     print(n[::-1])
#
# @outer      #add = outer(add)
# def add(a, b):
#     print(a + b)
#
# rev_str('python')
# add(2, 3)

###########################################################################################
'''02 September 2022'''

# def outer(func):
#     def wrapper(*args, **kwargs):
#         print('The addition of two numbers is : ')
#         func(*args, **kwargs)
#     return wrapper
#
# @outer      #add = outer(add)
# def add(a, b):
#     print(a + b)
#
# add(2, 3)
# add(9, 8)
# add(a=8, b=5)

'''NOTE: 
Whenever the interpreter exceutes @outer statement, two major changes will happen.
    i. outer functions argument will take the address of the decorated function(function ---> add)
    ii. The decorated function will take the address of wrapper function(add ---> wrapper func address)
'''

##############################################################################
'''wap to create a log decorator'''
# def outer(func):
#     def wrapper(*args, **kwargs):
#         print('Good morning')
#         func(*args, **kwargs)
#         print('****************************')
#     return wrapper
#
# @outer          #greeting = outer(greeting)
# def greeting(name, age):
#     print(f"hello my name is {name}, I'm {age} years old")
#
# greeting('Ram', 40)
# greeting('Raavan', 60)
# greeting('Sita', 45)
#################################################################################
'''write a decorator function to reverse a string'''
# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res[::-1]
#     return wrapper
#
# @outer      #rev_str = outer(rev_str)
# def rev_str(n):
#     return n
#
# print(rev_str('python'))
# print(rev_str('selenium'))

###############################################################################
'''write a decorator func that counts the number of arguments given to the main function'''
# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = len(args) + len(kwargs)
#         function = func(*args, **kwargs)
#         print(f'The total number of arguments is {res}')
#         return function
#     return wrapper
#
# @outer      #add = outer(add)
# def add(a, b, c, d):
#     return a + b + c + d
#
# print(add(1, 2, 3, d=4))


# def outer(func):
#     def wrapper(*args, **kwargs):
#         count = 0
#         for i in args:
#             count += 1
#         for j in kwargs:
#             count += 1
#         res = func(*args, **kwargs)
#         print(f'The total number of arguments is {count}')
#         return res
#     return wrapper
#
# @outer      #add = outer(add)
# def add(a, b, c, d, e):
#     return a + b + c + d + e
#
# print(add(1, 2, 3, d=4, e=5))

################################################################################################
'''write a decorator function to print the function name before decorating'''
# def outer(func):
#     def wrapper(*args, **kwargs):
#         print(f'The name of the main function is {func.__name__}')
#         func(*args, **kwargs)
#     return wrapper
#
# @outer      #september = outer(september)
# def september():
#     print('September has 30 days')
#
# september()

'''__name__ =  special methods/ magic methods/ dunder methods'''

#######################################################################################
'''write a decorator to count the total number of decorated functions'''
# count = 0
# def outer(func):
#     def wrapper(*args, **kwargs):
#         global count
#         count += 1
#         func(*args, **kwargs)
#     return wrapper
#
# @outer      #add = outer(add)
# def add(a, b):
#     return a + b
# @outer      #sub = outer(sub)
# def sub(a, b):
#     return a - b
# @outer      #mul = outer(mul)
# def mul(a, b):
#     return a * b
# @outer      #div = outer(div)
# def div(a, b):
#     return a / b
#
# add(1, 2)
# sub(2, 3)
# mul(3, 4)
# div(4, 5)
# print(f'The value of count is {count}')

############################################################################
'''3 September 2022'''
'''write a decorator function to execute the function for 3 times'''
# def exe_three_times(func):
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             func(*args, **kwargs)
#     return wrapper
#
# @exe_three_times            #display = exe_three_times(display)
# def display():
#     print('Function block executing')
#
# display()

#####################################################################
'''PARAMETERIZED DECORATORS'''
# def n_times(n):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return outer
#
# @n_times(3)
# def name(f_name, l_name):
#     print(f'My name is {f_name} {l_name}')
#
# name('Smita', 'Mishra')
#
# @n_times(5)
# def age(num):
#     print(f'My age is {num}')
#
# age(20)

##################################################################################
'''Delay the execution'''
# import time
# def greeting(name, age):
#     time.sleep(3)
#     print(f'My name is {name} and I am {age} years old')
#
# greeting('John', 50)
#
# '''Delay the execution using decorators'''
# import time
# def delay_execution(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(2.5)
#         func(*args, **kwargs)
#     return wrapper
#
# @delay_execution
# def greeting(name, age):
#     print(f'My name is {name} and I am {age} years old')
#
# greeting('John', 50)

###########################################################################
# import time
# def delay_execution(n):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             func(*args, **kwargs)
#         return wrapper
#     return outer
#
# @delay_execution(3)
# def greeting(name, age):
#     print(f'My name is {name} and I am {age} years old')
#
# greeting('John', 50)
#
# @delay_execution(5)
# def greeet():
#     print('Hello everyone good morning')
#
# greeet()

#############################################################################
'''Calculate the execution time'''
# import time
# def greeting(name, age):
#     start = time.time()
#     print(f'My name is {name} and I am {age} years old')
#     end = time.time()
#     res = end - start
#     print(f'Total execution time is {res} seconds')
#
# greeting('Ram', 20)
#
# import time
# def greeting(name, age):
#     start = time.time()
#     time.sleep(4)
#     print(f'My name is {name} and I am {age} years old')
#     end = time.time()
#     res = end - start
#     print(f'Total execution time is {res} seconds')
#
# greeting('Ram', 20)

##################################
'''Using decorators'''
# import time
# def calculate_execuution_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         time.sleep(2)
#         func(*args, **kwargs)
#         end = time.time()
#         res = end - start
#         print(f'Total execution time is {res} seconds')
#     return wrapper
#
# @calculate_execuution_time
# def greeting(name, age):
#     print(f'My name is {name} and I am {age} years old')
#
# greeting('Ram', 20)

#######################################################################
'''September 6 2022'''
'''OOPs'''
'''Classes and objects 
* A Class is like an object constructor, or a "blueprint" for creating objects.
* Can be called as a design / plan / model
* It contains states and behaviours.
* Behaviour - action performed on the class(methods).
* State - properties of the class(variables).

#################################################
INSTANCES OR OBJECTS
* Represents the physical entity of class.
* We can create any number of objects using a class.
* Each and every object are independent to each other. i.e., changes done in one object will not
 affect the other objects.

################################################
CONSTRUCTORS
* Constructor is a special method used to create and initialize an object of a class
* Key points : 
    How to create a constructor to initialize an object in Python
    Different types of constructors
    Constructor overloading and chaining 

################################################

SYNTAX:
Creating a class:
					class ClassName:
						pass

Creating an instance:
				obj = ClassName()

Class names should be created using CamelCase according to PEP-8 

METHODS
The functions which are written inside a class are called methods.
They are called class attributes and should have the first parameter as “self” 
    (python naming convention).
Self - holds the address of the instance which is invoking the method.

NOTE:
* In case of classes, when you look up for an attribute, Python tries to look for that attribute
 in the instance.
* If the attribute exists in the instance, then it will return the value of the instance attribute.
* If the attribute does not exist in the instance, it will lookup for the attribute at class level.
* If the attribute exists in the class level, it will return the value of the class attribute.
* If the attribute does not exist in instance and at class level,then AttributeError is raised.
'''
#################################################################################

# class MyCalculator:
#     def add(self, a, b):
#         print(a + b)
#
#     def sub(self, a, b):
#         print(a - b)
#
#     def mul(self, a, b):
#         print(a * b)
#
#     def div(self, a, b):
#         print(a / b)
#
# cal1 = MyCalculator()
# cal2 = MyCalculator()
# cal1.add(2, 3)
# cal2.add(1, 3)
# cal1.sub(3, 2)

#######################################################################################
# class MyCalculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self, x, y):
#         print(self.a + self.b)
#         print(x + y)
#
#     def sub(self):
#         print(self.a - self.b)
#
#     def mul(self):
#         print(self.a * self.b)
#
#     def div(self):
#         print(self.a / self.b)
#
# cal1 = MyCalculator(8, 2)
# cal2 = MyCalculator(6, 3)
# cal1.add(2, 4)
# cal1.sub()
# cal1.mul()
# cal1.div()


###############################################################################
'''September 7 2022'''

# list_ = [1, 2]
#
# #adding 0.5 to the integers
# list_[0] = list_[0] + 0.5
# list_[1] = list_[1] + 0.5
# print(list_)
#
# #swap
# temp  = list_[0]
# list_[0] = list_[1]
# list_[1] = temp
# print(list_)
#
# #reset
# list_[0] = 0
# list_[1] = 0
# print(list_)
#
# # print(dir(list))
# print(type(list_))


########################
# class Integers:
#     def add(self, a, b, extra_value):
#         print(f'Before Adding: {a} and {b}')
#         a = a + extra_value
#         b = b + extra_value
#         print(f'After Adding: {a} and {b}')
#
#     def swap(self, a, b):
#         print(f'Before swapping: {a} and {b}')
#         temp = a
#         a = b
#         b = temp
#         print(f'After swapping: {a} and {b}')
#
#     def reset(self, a, b):
#         print(f'Before resetting: {a} and {b}')
#         a = 0
#         b = 0
#         print(f'After resetting: {a} and {b}')
#
# i1 = Integers()
# # print(i1)   #<__main__.Integers object at 0x000001F019E63FD0>
# Integers.add(i1, 1, 2, 0.5)
# Integers.swap(i1, 1, 2)
# Integers.reset(i1, 1, 2)

#############################################################################
# class Integers:
#
#     #init will store the values inside the class
#     def __init__(self, a, b, extra_value):
#         self.a = a
#         self.b = b
#         self.extra_value = extra_value
#
#     def add(self):
#         print(f'Before Adding: {self.a} and {self.b}')
#         self.a = self.a + self.extra_value
#         self.b = self.b + self.extra_value
#         print(f'After Adding: {self.a} and {self.b}')

#     def swap(self):
#         print(f'Before swapping: {self.a} and {self.b}')
#         temp = self.a
#         self.a = self.b
#         self.b = temp
#         print(f'After swapping: {self.a} and {self.b}')
#
#     def reset(self):
#         print(f'Before resetting: {self.a} and {self.b}')
#         self.a = 0
#         self.b = 0
#         print(f'After resetting: {self.a} and {self.b}')
# #
# i1 = Integers(1, 2, 0.5)
# i2 = Integers(3, 4, 1.5)
# print(i1.__dict__)    #init will internally store the values in the form of a dictionary,
#                         #This is call as instance dictionary
# print(i2.__dict__)
# Integers.add(i1)
# Integers.add(i2)
# Integers.swap(i1)
# i1.reset()
# i1.add()

##########################################################################################
# class Employee:
#     f_name = 'Steve'
#     l_name = 'Jobs'
#
# e1 = Employee()
# print(e1.f_name)
# print(e1.l_name)

#########################################################################################
# class Bonus:
#     bonus_amount = 5000
#
#     def __init__(self, name, empid):
#         self.name = name
#         self.empid = empid
#
#     def gift(self):
#         print(f'Congratulations {self.name} on recieving the Deepavali bonus amount of Rs.{self.bonus_amount}')
#
# b1 = Bonus('Ajay', 1234)
# b2 = Bonus('Krish', 2345)
# b1.gift()       #Congratulations Ajay on recieving the Deepavali bonus amount of Rs.5000
# print(b1.bonus_amount)      #5000
# print(Bonus.bonus_amount)   #5000
# b2.gift()       #Congratulations Krish on recieving the Deepavali bonus amount of Rs.5000
# b2.bonus_amount = 3500
# b2.gift()       #Congratulations Ajay on recieving the Deepavali bonus amount of Rs.3500
# print(b2.bonus_amount)      #3500
# print(b1.bonus_amount)      #5000
# Bonus.bonus_amount = 10000
# print(Bonus.bonus_amount)       #10000
# print(b1.bonus_amount)          #10000
# print(b2.bonus_amount)          #3500

'''The changes made in one object will never affect the other objects'''

########################################################################################

# class Employee:
#     company_name = 'tcs'
#
#     def __init__(self, f_name, l_name, empid):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.empid = empid
#
#     def display(self):
#         print(f'Hello {self.f_name} {self.l_name}, Welcome to {self.company_name}')
#
#     def email(self):
#         print('This is your Email-id')
#         print(f'{self.f_name}_{self.empid}@{self.company_name}.com')
#
# emp1 = Employee('Elon', 'Musk', 12334)
# emp1.display()
# emp1.email()

##################################################################################################
'''September 8 2022'''
'''
METHODS
* The functions which are written inside a class are called methods.
* They are called class attributes and should have the first parameter as “self” 
    (python naming convention).
* Self - holds the address of the instance which is invoking the method.

NOTE:

* In case of classes, when you look up for an attribute, Python tries to look for that attribute
    in the instance.
* If the attribute exists in the instance, then it will return the value of the instance attribute.
* If the attribute does not exist in the instance, it will lookup for the attribute at class level.
* If the attribute exists in the class level, it will return the value of the class attribute.
* If the attribute does not exist in instance and at class level,then AttributeError is raised.

'''
#############################################################
'''object method / Instance method
* Method that can change the state of the object is known as object method
* Object  method receives the object address (self) as an implicit first argument 
* An Object method is a method that is bound to the object and not the class.
* They have the access to the state of the object as it takes a self parameter that points to 
    the object instance.

CLASS METHOD
* class method receives the class as an implicit first argument, just like an instance method 
    receives the instance 
* A class method is a method that is bound to the class and not the object of the class.
* They have the access to the state of the class as it takes a class parameter that points to the
    class and not the object instance.
'''
###################################################################
'''without class method'''
# class PrimeMinister:
#     current_prime_minister = 'Narendra Modi'
#
#     def display(self):
#         print(f'The Current PrimeMinister is {self.current_prime_minister}')
#
#     def replacement(self, votes):
#         if votes > 100:
#             self.current_prime_minister = 'Yogi Adithyanath'
#
# bjp = PrimeMinister()
# opposition = PrimeMinister()
# common_people = PrimeMinister()
# bjp.display()                   #The Current PrimeMinister is Narendra Modi
# opposition.display()            #The Current PrimeMinister is Narendra Modi
# common_people.display()         #The Current PrimeMinister is Narendra Modi
# bjp.replacement(110)
# bjp.display()                   #The Current PrimeMinister is Yogi Adithyanath
# opposition.display()            #The Current PrimeMinister is Narendra Modi
# common_people.display()         #The Current PrimeMinister is Narendra Modi
# print(PrimeMinister.current_prime_minister)     #Narendra Modi


'''with class  method'''
# class PrimeMinister:
#     current_prime_minister = 'Narendra Modi'
#
#     def display(self):
#         print(f'The Current PrimeMinister is {self.current_prime_minister}')
#
#     @classmethod
#     def replacement(self, votes):
#         if votes > 100:
#             self.current_prime_minister = 'Yogi Adithyanath'
#
# bjp = PrimeMinister()
# opposition = PrimeMinister()
# common_people = PrimeMinister()
# bjp.display()                       #The Current PrimeMinister is Narendra Modi
# opposition.display()                #The Current PrimeMinister is Narendra Modi
# common_people.display()             #The Current PrimeMinister is Narendra Modi
# bjp.replacement(110)
# bjp.display()                       #The Current PrimeMinister is Yogi Adithyanath
# opposition.display()                #The Current PrimeMinister is Yogi Adithyanath
# common_people.display()             #The Current PrimeMinister is Yogi Adithyanath
# print(PrimeMinister.current_prime_minister)         #Yogi Adithyanath


##################################################################
'''can have multiple class methods'''
# class PrimeMinister:
#     current_prime_minister = 'Narendra Modi'
#     current_president = 'Draupadi Murmu'
#
#     def display(self):
#         print(f'The Current PrimeMinister is {self.current_prime_minister}')
#
#     @classmethod
#     def replacement(self, votes):
#         if votes > 100:
#             self.current_prime_minister = 'Yogi Adithyanath'
#
#     def display1(self):
#         print(f'The current president is {self.current_president}')
#
#     @classmethod
#     def president(self, vote):
#         if vote > 50:
#             self.current_president = 'Sudha Murthy'

# bjp = PrimeMinister()
# opposition = PrimeMinister()
# common_people = PrimeMinister()
# bjp.display()                       #The Current PrimeMinister is Narendra Modi
# opposition.display()                #The Current PrimeMinister is Narendra Modi
# common_people.display()             #The Current PrimeMinister is Narendra Modi
# bjp.replacement(110)
# bjp.display()                       #The Current PrimeMinister is Yogi Adithyanath
# opposition.display()                #The Current PrimeMinister is Yogi Adithyanath
# common_people.display()             #The Current PrimeMinister is Yogi Adithyanath
# print(PrimeMinister.current_prime_minister)         #Yogi Adithyanath
# bjp.display1()
# bjp.president(52)
# bjp.display1()
# opposition.display1()

#############################################################################
'''Static method :
* A static method is independent of both class as well as instances. 
* Hence it does not receive implicit first argument i.e, self/cls
* Therefore a static method can neither modify object state nor class state. 
'''

# class Sample:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(f'My name is {self.name}, and I am {self.age} years old')
#
#     @staticmethod
#     def add(a, b):
#         print(a + b)
#
#
# s = Sample('Ram', 45)
# s.display()
# s.add(1, 2)

###########################################################################################
'''September 9 2022'''
'''Making objects callable
OVERVIEW :
* Among class and objects, only class is callable.
* In order to make an object callable, there must be __call__() present in the respective class 
    of that object. 
* callable(obj) - It is a function used to check if any object is callable or not.


NOTE : Generally classes are callable  because they will be having magic/special/dunder method
    __call__ . But, this is not the case for user defined objects. 
    Objects can never be called since they'll not have __call__ implicitly.

    * When an  object is called without defining __call__ method, it'll raise TypeError 
'''

# class Sample:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(f'My name is {self.name} and I am {self.age} years old')
#
# print(dir(Sample))
# s = Sample('ram', 25)
# Sample.display(s)
# s.display()
# print(callable(Sample))     #True
# print(callable(s))          #False
#####################################################################
# class Sample:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __call__(self, *args, **kwargs):
#         print('In call method')
#
# s = Sample('Ram', 35)
# s()                         #In call method
# print(callable(s))          #True

#######################################################################
'''create a class that prints the msg 'hello world' when an object is called '''
# class Message:
#
#     def __call__(self, *args, **kwargs):
#         print('Hello world')
#
# m = Message()
# m()         #Hello world

########################################################################
'''create a class which will add the user given numbers when an object is called'''
# class Addition:
#
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def __call__(self, *args, **kwargs):
#         print(self.num1 + self.num2)
#
# a = Addition(2, 3)
# a()

##########
# class Addition:
#
#     def __call__(self, num1, num2):
#         print(num1 + num2)
#
# a = Addition()
# a(7, 3)

###########################################################################################
'''create a class which returns a list of squares when the object is called'''
# class Squares:
#
#     def __call__(self, *args, **kwargs):
#         l = []
#         for i in args:
#             l.append(i**2)
#         for i in kwargs:
#             l.append(kwargs[i]**2)
#         return l
#
# s = Squares()
# print(s(2, 4, p=9, y=6, t=3))


# class Squares:
#     def __call__(self, a):
#         l = []
#         for i in a:
#             l.append(i**2)
#         return l
#
# s = Squares()
# print(s([1, 2, 3, 4, 5, 6]))
#################################################################################
'''create a class that checks whether the number is even or not whenever the obj is called'''
# class EvenOdd:
#     def __init__(self, num):
#         self.num = num
#
#     def __call__(self, *args, **kwargs):
#         if isinstance(self.num, (int, float)):
#             if self.num % 2 == 0:
#                 return 'Even'
#             else:
#                 return 'Odd'
#         else:
#             return 'Wrong argument'
#
# even_odd = EvenOdd('1234')
# print(even_odd())

################################################################################
'''Class Decorators'''
'''NOTE : Whenever @Greet is executed, the interpreter will interpret it as display=Greet(display). 
There will be two major changes happening now
    i. func will be taking display function address
    ii. Greet(display), it is nothing but the syntax of object creation, it'll create an object
     and the address will be given to the display. display will now be the object of greet class'''

# class Greet:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print('In __call__ executing')
#         return self.func()
#
# @Greet          #display = Greet(display)
# def display():
#     return 'Display function executing'
#
# print(display())

##########################################################################################
'''September 12 2022'''
'''write a class decorator which delays the execution by 5 seconds'''
# import time
# class Delay:
#     def __init__(self, func):
#         self.func =  func
#
#     def __call__(self, *args, **kwargs):
#         time.sleep(5)
#         return self.func()
#
# @Delay      #display = Delay(display)
# def display():
#     print('In display')
#
# display()

################################################
'''write a class decorator that prints the function name'''
# class FunctionName:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print(f'The function name is {self.func.__name__}')
#         return self.func()
#
# @FunctionName       #display = FunctionName(display)
# def display():
#     print('In display')
#
# display()

########################################################################
'''write a class decorator which delays the execution by 5 seconds'''
# import time
# class Delay:
#     def __init__(self, n):
#         self.n =  n
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             time.sleep(self.n)
#             return func(*args, **kwargs)
#         return wrapper
#
# @Delay(3)      #display = Delay(3)
# def display():
#     print('In display')
#
# display()

#########################################################################
'''write a class decorator to print 'good morning' msg if the user has not given any msg '''
# class Message:
#     def __init__(self, msg='Good Morning'):
#         self.msg = msg
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print(f'The message is {self.msg}')
#             return func(*args, **kwargs)
#         return wrapper
#
# @Message('hai')
# def display():
#     print('In display')
#
# display()
#
#
# @Message()
# def spam():
#     print('In spam')
#
# spam()
#
# #####################################################################################
'''write a class decorator to count the number of function calls'''
# count = 0
# class Greet:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         global count
#         count += 1
#         return self.func()
#
# @Greet
# def display():
#     print('In display')
#
# display()
# display()
# display()
# print(f'The total number of function calls is {count}')


# count = 0
# class Greet:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             global count
#             count +=1
#             func(*args, **kwargs)
#         return wrapper
#
# @Greet()
# def display():
#     print('In display')
#
# display()
# display()
# display()
# print(f'The total number of function calls is {count}')

################################################################################
'''write a class decorator to calculate the execution time'''
# def fib(n):
#     if n == 0:
#         return n
#     elif n==1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
#
# for i in range(1, 11):
#     print(fib(i))

#################################################################################
'''September 13 2022'''
'''Exception handeling
* An event which causes the termination of the program.
* To handle unexpected termination of the program, exception handling is done.
* To handle the exception, try and except block is used.'''
# num1 = int(input('Enter the number 1: '))
# num2 = int(input('Enter the number 2: '))
# try:
#     print(num1 / num2)
# except:
#     print('hello world')
'''
4 Types
1. Default Exception block
2. Specific Exception block
3. Multiple Exception block
4. Generic Exception block
'''

'''Default exception block
This Block will handle all the exceptions that are raised in try block
Syntax :
            try:
			    statements
			except:
			    Statements
			    '''
# a = 'hello world'
# try:
#     a.append('hai')
# except:
#     print('Except block executing')
# ##################
# try:
#     d[10] = 10
# except:
#     print('Except block executing')

###################################################################
'''Specific exception block
We can create an exception block specific to an error.
Syntax :	
        try:
		    statements
		except <exception_name>:
		    Statements'''
# a = 'hello world'
# try:
#     a.append('hai')
# except AttributeError:
#     print('Except block executing')     #'Except block executing'

# a = 'hello world'
# try:
#     a.append('hai')
# except ZeroDivisionError:
#     print('Except block executing')     #AttributeError
#####################################################################
'''Multiple Exception block
A single try block can have multiple except blocks.
Syntax :	
        try:
		    statements
		except exception 1:
		    statements
		except exception 2 : 
		    Statements'''
# a = 'hello world'
# try:
#     a.append('hai')         #AttributeError
# except ZeroDivisionError:
#     print('Except block executing')
# except NameError:
#     print('Except block2 executing')
# except IndexError:
#     print('Except block3 executing')
# except AttributeError:
#     print('Except block4 executing')

########################################################################
'''Generic Except block
Handles all types of exceptions in a single except block.
Syntax :	
        try: 
			statements
		except Exception/BaseException as alias: 
			Statements'''
# a = 'hello world'
# try:
#     print(a.index('z'))
# except BaseException as msg:
#     print('Except block executing')
#     print(msg)
#
# try:
#     print(10/0)
# except BaseException as message:
#     print(message)      #division by zero

########################################################
'''as keyword
Used to give alias name for the exception names written in the except block.
Syntax :  except <exception name> as alias_name:
'''
###############################################################
'''else
It is a block which will get executed when the exception is not raised in the try block.
Syntax :	
        try:
			statements
		except:
			statements
		else:
			Statements'''
# a = ['hello world']
# try:
#     a.append('hai')
# except:
#     print('Except block executing')
# else:
#     print('Else block executing')
#     print(a)

# a = {}
# try:
#     print('Try block executing')
#     a['key'] = 'value'
# except BaseException as message:
#     print('Except block executing')
#     print(message)
# else:
#     print('Else block executing')
#     print(a)

#####################################################
'''finally
It is a block which will get executed even when the exception is raised or not.
We can add try and except block inside finally.
Syntax :	
        try:
			statements
		except:
			statements
		finally :
			Statements'''

# try:
#     print('Try block executing')
#     a['key'] = 'value'
# except BaseException as message:
#     print('Except block executing')
#     print(message)
# else:
#     print('Else block executing')
#     print(a)
# finally:
#     print('FINALLY EXECUTING')

######################################################################
'''raise keyword
* Used to raise a specific exception whenever the condition is matched.
* Once an exception is raised, it searches for the specific except block and handles the exception.
* Syntax :	raise error_name(“message”)
'''
# a = int(input('Enter the number: '))
# if a > 0:
#     print(a)
# else:
#     raise AttributeError('the value of a is not greater than 0')

###########################################################################
'''wap to handle KeyError while creating a dictionary of word and its count'''
# l = ['hello', 'world', 'hello', 'hai']
'''normal program'''
# d = {}
# for i in l:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

'''handling key error'''
# d = {}
# l = ['hello', 'world', 'hello', 'hai']
# for item in l:
#     try:
#         d[item] += 1
#     except:
#         d[item] = 1
# print(d)

###################################################################
'''wap to handle ZeroDivisionError in the list of data. Print the result of division if there
is no exception and print the numbers for all iterations'''
# num = [(1, 0), (3, 4), (4, 5), (7, 0), (9, 6), (8, 0)]
# for item in num:
#     x, y = item
#     try:
#         res = x/y
#     except:
#         print('invalid inputs')
#     else:
#         print(res)
#     finally:
#         print(f'The values are {x} and {y}')
##############################################################
# num = [(1, 0), (3, 4), (4, 5), (7, 0), (9, 6), (8, 0)]
# for item in num:
#     x, y = item
#     try:
#         if y == 0:
#             raise ZeroDivisionError
#     except ZeroDivisionError:
#         print('Invalid inputs')
#     else:
#         print(x/y)
#     finally:
#         print(f'The values are {x} and {y}')

####################################################################################
# def validate_user_name(user_name):
#     if user_name != 'John':
#         print('Invalid UserName')
#
# def validate_password(password):
#     if password != 'John123':
#         print('Invalid Password')
#
# try:
#     validate_user_name('Ram')
#     validate_password('Ram123')
# except:
#     print('Invalid credentials')

# def validate_user_name(user_name):
#     if user_name != 'John':
#         raise NameError('Invalid UserName')
#
# def validate_password(password):
#     if password != 'John123':
#         raise NameError('Invalid Password')
#
# try:
#     validate_user_name('Ram')
#     validate_password('Ram123')
# except:
#     print('Invalid credentials')

#
# def validate_user_name(user_name):
#     if user_name != 'John':
#         raise NameError('Invalid UserName')
#
# def validate_password(password):
#     if password != 'John123':
#         raise NameError('Invalid Password')
#
# try:
#     validate_user_name('John')
#     validate_password('Ram123')
#
# except BaseException as msg:
#     print('Invalid credentials')
#     print(msg)

#######################################################################
# def validate_user_name(user_name):
#     if user_name != 'John':
#         raise NameError('Invalid UserName')
#
#
# def validate_password(password):
#     if password != 'John123':
#         raise NameError('Invalid Password')
#
# try:
#     validate_user_name('John')  #/validate_user_name('Ram')
#     validate_password('John123') #/validate_password('Ram123')
#
# except BaseException as msg:
#     print('Invalid credentials')
#     print(msg)
#
# else:
#     print('Else block is executing')
#
# finally:
#     print('Finally block executing')

##############################################################################
'''Factorial'''
# import math
# def factorial_1(num):
#     if not isinstance(num, int):
#         raise TypeError("Input value is not number")
#     elif isinstance(num, int):
#         if num <= 0:
#             raise ValueError("Number is less than 0")
#         else:
#             print(math.factorial(num))
#
# factorial_1(-9)
#
# ####
# import math
# def fact(n):
#     try:
#         result = math.factorial(n)
#     except BaseException as msg:
#         print(msg)
#     else:
#         print(result)
#
# fact(6)
# fact('9')

##########################################
'''custom exception
* User defined exceptions or custom exception
* Custom exceptions can be created by inheriting Exception class.
Syntax :	
        class user_exception_name(Exception):
	        pass'''

# number = int(input('Enter the number: '))
# class MyOwnError(Exception):
#     pass
#
# if number < 0:
#     raise MyOwnError('Number less than 0')

#################################################################################
'''Custom Iterators'''
# l = [1, 2 ,3, 4]
# # print(dir(l))       #__iter__, __len__
#
# print(dir(list))        #__iter__, __len__
# print(dir(enumerate))   #__iter__, __next__

'''Can find the length of an iterable, but cannot find the length of an iterator
Iterator will be having __next__ method, whereas iterable will not be having that
'''

###################################################################################
'''CUSTOM ITERATORS
OVERVIEW
* Iterators are containers for objects so that you can loop over the objects.
* Iterators are objects that allow you to traverse through all the elements of a collection.
* There are many iterators in the Python standard library. For example, enumerate object is an iterator
 and you can run a for loop over a list.
* Anything that can be iterated or looped over is called iterable in Python.
* All iterables have a special method called  __iter__
* Strings, Lists, Tuples, Sets, Dictionary are iterables.
* All iterables can be passed to the built-in iter() function to get an iterator from them.
* An iterator is an object that implements __next__, which is expected to return the next element of the
 iterable object that returned it, and raise a StopIteration exception when no more elements are available.
* Any iterator can be passed to next() function to get the next item.
* Iterators does not have length. They do not know how long they are.
* Iterators do not have length, and can not be indexed. You can only call next() method to  get 
    the next item.
* Generators are iterators, enumerate objects are iterators, zip function is an iterator file objects
    are iterators,
   Generators.
   Generator Expressions.
   enumerate
   map
   filter
   zip
   reversed
   csv.reader()  functions returns an iterator object
* Iterators are Lazy Iterables. i.e. they don’t determine what their next item is until you ask for it

#######################################################################################
__iter__ and __next__
* To create a Python iterator object, you will need to implement two methods in your iterator class.
* __iter__ : This returns the iterator object itself and is used while using the "for" and "in" keywords.
* __next__ : This returns the next value. This would return the StopIteration error once all the 
    objects have been looped through.

Note : Once an iterator object is traversed completely we can not traverse through it again from the
    beginning until the iterator object is initiated.
###########################################################################################
ITERATOR PROTOCOl:
for item in obj:
Statements
What happens under the Covers?
     _iter = obj.__iter__()  # Get iterator object
     while True:
     		try:
          		x = _iter.__next__()  # Get next item
         	except StopIteration:  # No more items
            	break
            statements ...
###########################################################################################
NOTE : In order to create custom iterator, class must contain __iter__ and __next__ methods.
* __iter__ : makes a class as an iterable.'''

# l = [1, 2, 3 ,4]
#
# print(dir(list))            #__iter__, __len__
# print(dir(enumerate))       #__iter__, __next__


# a = {'hello', 'hai'}
# count = 0
# while count < len(a):
#     print(a[count])
#     count += 1

# for i in a:
#     print(i)

# list_1 = [1, 2, 3, 4]
# print(len(list_1))      #4
# print(type(list_1))     #<class 'list'>
# iter_obj = iter(list_1)       #or list_1.__iter__()
# print(iter_obj)     #<list_iterator object at 0x000001E13A697FD0>
# print(type(iter_obj))   #<class 'list_iterator'>
# print(len(iter_obj))        #Error


# list_1 = [1, 2, 3, 4]
# for item in list_1:
#     print(item)

# list_1 = [1, 2, 3, 4]
# iter_object = iter(list_1)
# while True:
#     item = next(iter_object)
#     print(item)


# list_1 = [1, 2, 3, 4]
# iter_object = iter(list_1)
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object))
# print(next(iter_object))

'''take this'''
# list_1 = [1, 2, 3, 4]
# iter_object = iter(list_1)
# while True:
#     try:
#         item = next(iter_object)        #1, 2, 3, 4
#     except StopIteration:
#         break
#     else:
#         print(item)
#
# for item in list_1:
#     print(item)

############################################
# list_1 = [1, 2, 3, 4]
# iter_object = iter(list_1)
# for item in iter_object:
#     print(item, end=' ')        #1 2 3 4
#
# for item in iter_object:
#     print(item) #nothing is printed because we've already traversed through it once.

#########################################################################
# class Sample:
#
#     def __init__(self, ele, i):
#         self.ele = ele
#         self.i = i
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i < len(self.ele):
#             x = self.i
#             self.i += 1
#             return self.ele[x]
#         else:
#             raise StopIteration
#
# s = Sample([1, 2, 3, 4], 0)
# for item in s:
#     print(item)

###########################################################################
'''create a custom iterator class to print the numbers from 1-5'''
# class Numbers:
#     def __init__(self, i):
#         self.i = i
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i <= 5:
#             x = self.i
#             self.i += 1
#             return x
#         else:
#             raise StopIteration
#
# num = Numbers(1)
# for i in num:
#     print(i)

#####################################################################
'''create a custom iterator class to print the numbers from 10-1'''
# class Numbers:
#     def __init__(self, i):
#         self.i = i
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i > 0:
#             x = self.i
#             self.i -= 1
#             return x
#         else:
#             raise StopIteration
#
# num = Numbers(10)
# for item in num:
#     print(item)

##########################################################################
'''17 September 2022'''
'''write a custom iterator class to pprint squares of numbers'''
# class SqNum:
#     def __init__(self, ele, i):
#         self.i = i
#         self.ele = ele
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i < len(self.ele):
#             x = self.i
#             self.i += 1
#             return self.ele[x]**2
#         else:
#             raise StopIteration
#
# s = SqNum([1, 2, 5, 10], 0)
# l1 = (i for i in s)
# print(f'the sq. numbers of {s.ele} is {list(l1)} respectively')

###########################################################################
'''create a custom iterator class to print the range of numbers'''
# class Range:
#     def __init__(self, start_index, end_index, step_value):
#         self.start_index = start_index
#         self.end_index = end_index
#         self.step_value = step_value
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start_index > self.end_index:
#             raise StopIteration
#         else:
#             number = self.start_index
#             self.start_index += self.step_value
#             return number
#
# range_obj = Range(10, 20, 2)
# for item in range_obj:
#     print(item)

###############################################################################
'''create a custom iterator class to return the elements of the list in reversed order'''
# class Reversed:
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if len(self.iterable) == 0:
#             raise StopIteration
#         else:
#             popped_element = self.iterable.pop()
#             return popped_element
#
# rev_obj = Reversed(['vijay', 'smita', 'archana', 'nandhini'])
# for item in rev_obj:
#     print(item)


###############################################################
'''prime number'''
# class Prime:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start == self.end:
#             raise StopIteration
#
#         if self.start > 1:
#             for i in range(2, self.start):
#                 if self.start % i == 0:
#                     break
#             else:
#                 result = self.start
#                 self.start += 1
#                 return result
#             self.start += 1
#
# p = Prime(2, 10)
# for i in p:
#     if i != None:
#         print(i)

#######################################################################################
'''
random()
* Python defines a set of functions that are used to generate or manipulate random numbers. 
* Python offers random module that can generate random numbers.
* This particular type of functions are used in a lot of games, lotteries or any application requiring
    random number generation.

randrange()
* The randrange() method returns a randomly selected element from the specified range.
* Syntax : random.randrange(start, stop, step)
* Start → Optional. An integer specifying at which position to start. Default 0
* Stop → Required. An integer specifying at which position to end.
* Step → Optional. An integer specifying the incrementation. Default 1
Note : Here the stop value will not be included.

randint()
* The randint() method returns a randomly selected element from the specified range.
* Syntax : random.randint(start, stop)
* Start → Required,  An integer specifying at which position to start. 
* Stop →  Required. An integer specifying at which position to end.
* Note: Here both start and stop value will  be included.

choice()
* The choice() method returns a randomly selected element from the specified sequence.
* The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
* Syntax : random.choice(sequence)

shuffle()
* The shuffle() method takes a sequence (list) and reorganize the order of the items.
* Syntax : random.shuffle(sequence)
* Note: This method changes the original list it does not return a new list.

sample()
* The sample() method returns a list with a random selection of a specified number of items from a sequence.
    Syntax : random.sample(sequence, k)
        Sequence →  Required. A sequence. Can be any sequence: list, set, range etc.
        K →  Required. The size of the returned list
Note: This method does not change the original sequence.

random()
The random() method returns a random floating number between 0 and 1.
Syntax : random.random()

uniform()
The uniform() method returns a random floating number between the two specified numbers (both included).
    Syntax : random.uniform(a, b)
        a : Required. A number specifying the lowest possible outcome
        b : Required. A number specifying the highest possible outcome
'''
##########################################################################
'''September 19 2022'''
'''
UML Diagrams
* The standard method of creating class is called UML (Unified Modeling Language).
* UML is used to show class hierarchies in software projects.
* In other words, it describes the relationships between different classes and it supports
    inheritance and composition.

##############################################################################
Inheritance
* Inheritance is the capability of one class to derive or inherit the properties from another class. 
* Inheritance enables us to define a class that takes all the functionality from a parent class
    and allows us to add more.
* Parent class is the class being inherited from, also called base class.
* Child class is the class that inherits from another class, also called derived class.

##############################################################################
'''
# class A:
#     def feature1(self):
#         print('feature1 is executing')
#
#     def feature2(self):
#         print('feature2 is executing')
#
# a = A()
# a.feature1()
# a.feature2()
# print()
#
# class B(A):
#     def feature3(self):
#         print('feature3 is executing')
#
#     def feature4(self):
#         print('feature4 is executing')
#
# b = B()
# b.feature3()
# b.feature4()
# b.feature1()
# b.feature2()


# class B:
#     def feature3(self):
#         print('feature3 is executing')
#
#     def feature4(self):
#         print('feature4 is executing')
#
# class A(B):
#     def feature1(self):
#         print('feature1 is executing')
#
#     def feature2(self):
#         print('feature2 is executing')
#
# a = A()
# a.feature1()
# a.feature2()
# a.feature3()
# a.feature4()

#############################################################################
'''
TYPES OF INHERITANCE
1. Single level Inheritance
2. Multi-level Inheritance
3. Multiple Inheritance
4. Hierarchial Inheritance
'''

'''Single level Inheritance : When a child class inherits from only one parent class, it is called
    single level inheritance. '''
# class Parent:
#     car = 'Creta'
#
#     def display(self):
#         print(f'Parent car is {self.car}')
#
# class Child(Parent):
#     bike = 'Continental GT'
#
#     def display1(self):
#         print(f'Child Bike is {self.bike} and car is {self.car}')
#
#
# child1 = Child()
# child1.display()
# child1.display1()

############################################
# class Parent:
#     car = 'Creta'
#
#     def display(self):
#         print(f'Parent car is {self.car}')
#     def spam(self):
#         print('Parent class Spam execurting')
#
# class Child(Parent):
#     car = 'Audi'
#     bike = 'Continental GT'
#
#     def display1(self):
#         print(f'Child Bike is {self.bike} and car is {self.car}')
#     def spam(self):
#         print('Child class Spam executing')
#
#
# child1 = Child()
# child1.display()    #Parent car is Audi
# child1.display1()   #Child Bike is Continental GT and car is Audi
# child1.spam()       #Child class Spam executing
# print()
# parent1 = Parent()
# parent1.display()       #Parent car is Creta
# parent1.spam()          #Parent class Spam execurting
######################################################################
'''Multi-level Inheritance 
* Multi-level inheritance is achieved when a derived class inherits another derived class. 
* There is no limit on the number of levels.'''
# class GrandParent:
#     villa = 'Happy Home'
#
#     def grand_parent_attribute(self):
#         print(f"Grandparent's asset is {self.villa}")

# class Parent(GrandParent):
#     car = 'Volvo'
#
#     def parent_attribute(self):
#         print(f"Parent's asset is {self.car} and {self.villa}")
#
# class Child(Parent):
#     bike = 'Himalayan'
#
#     def child_attribute(self):
#         print(f"Child's asset is {self.bike}, {self.car} and {self.villa}")
#
# c = Child()
# c.grand_parent_attribute()
# c.parent_attribute()
# c.child_attribute()

#########################################################################
'''Multiple Inheritance
* Multiple inheritance is achieved when a derived class inherits from more than one Base class.

Order of inheritance: 
* In multiple inheritance, the inheritance will take place from right to left. I.e., the 
    rightmost class will be inherited first and the leftmost will be inherited last.

MRO(Method Resolution Order): 
* MRO is the order followed to look up for an attribute in classes. In multiple inheritance the 
    MRO will takes place from left to right.'''
# class Maruti:
#     def display(self):
#         print('Inheriting Maruti parts')
#
# class Suzuki:
#     def display1(self):
#         print('Inheriting Suzuki parts')
#
# class Vitara(Maruti, Suzuki):
#     def spam(self):
#         print('Vitara class executing')
#
# v = Vitara()
# v.display()     #Inheriting Maruti parts
# v.display1()    #Inheriting Suzuki parts


# class Child1:
#     a = 10
#     b = 20
#
# class Child2:
#     c = 30
#     b = 45
#
# class Child3(Child1, Child2):
#     a = 55
#     d = 100
#
# c = Child3()
# print(c.a)      #55
# print(c.b)      #20
# print(c.c)      #30
# print(c.d)      #100

#########################################################
'''Hierarchial Inheritance : Properties of single base class will be inherited by many child classes
'''
# class Parent:
#     car = 'Volvo'
#
#     def display(self):
#         print('Parent class executing')
#
# class Child1(Parent):
#     def spam1(self):
#         print(f"parent's car is {self.car}")
#
# class Child2(Parent):
#
#     def spam2(self):
#         print(f"parent's car is {self.car}")
#
# c1 = Child1()
# c2 = Child2()
# c1.spam1()
# c2.spam2()

#############################################################################################
'''20 September 2022'''
'''
* The process of calling parent class method after overriding it in the child class is called 
    chaining.
* In order to achieve chaining, super() is used.

NOTE: MRO(Method Resolution Order) is a concept that is used to search the attributes in a class 
    especially in inheritance hierarchy. Here MRO will be from left to right.
	Eg: class A(B, C):	----->	 A → B → C'''
##############################################3
'''Method chaining'''
# class Parent:
#     a = 10
#     def display(self):
#         print('Parent class display method executing')
#
# class Child(Parent):
#     a = 100
#     def display(self):      #overridden method
#         print('Child class display method executing')
#         Parent.display(self)    #/super().display()
#     def spam(self):         #Independent method
#         print('Child class spam method executing')
# c = Child()
# c.display()
# print(c.a)

#######################################################################
'''Constructor chaining'''
# class Sample:
#     def __init__(self, value1, value2):
#         self.value1 = value1
#         self.value2 = value2
#
#     def add(self):
#         print(f"The addition of two values is {self.value1 + self.value2}")
#
# class Spam(Sample):
#     def sub(self):
#         print(f"The subtraction of two values is {self.value1 - self.value2}")
#
# s = Spam(10, 5)
# s.add()
# s.sub()

##########################################
'''Constructor chaining'''
# class Sample:
#     def __init__(self, value1, value2):
#         self.value1 = value1
#         self.value2 = value2
#
#     def add(self):
#         print(f"The addition of two values is {self.value1 + self.value2}")
#
# class Spam(Sample):
#     def __init__(self, v1, v2):
#         self.v1 = v1
#         self.v2 = v2
#         super().__init__(self.v1, self.v2)
#
#     def sub(self):
#         print(f"The subtraction of two values is {self.v1 - self.v2}")
#
# s = Spam(10, 5)
# s.add()
# s.sub()

########################################################################
'''create a classname Addition which has two variables and write a method to add those two 
   variables   
|---------------------------|
|       Addition            |
|---------------------------|
|           a               |
|           b               |
|---------------------------|
|           add()           |
|---------------------------|
'''
# class Addition:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         print(f'The addition of two numbers is {self.a + self.b}')
#
# a = Addition(3, 4)
# a.add()

##################################################################################
'''create a classname student and get the stu name, id, dob as a user input and check whether the
student is over 18 years
----------------------
|       Student      |
----------------------
        stu_name     |
        stu_id       |
        stu_dob      |
----------------------
        age()        |
----------------------

'''
# class Student:
#     def __init__(self, stu_name, stu_id, stu_dob):
#         self.stu_name = stu_name
#         self.stu_id = stu_id
#         self.stu_dob = stu_dob
#
#     def age(self):
#         date, month, year = self.stu_dob.split('/')     #['12', '3', '1998']
#
#         if 2022-int(year) > 18:
#             print(f"{self.stu_name} is above 18 years")
#         else:
#             print(f"{self.stu_name} is below 18 years")
#
# stu_obj = Student('Ram', 1234, '12/3/1998')
# s1 = Student('Lakshman', 2345, '11/11/2010')
# stu_obj.age()
# s1.age()

#############################################################################
'''
|-----------------------------|
|       BankAccount           |
|-----------------------------|
|       owner : string        |
|       balance : float       |
|-----------------------------|
|          deposit            |
|         withdrawal          |
|           balance           |
-------------------------------       
'''
# class BankAccount:
#
#     def __init__(self, acc_holder_name, acc_balance):
#         self.acc_holder_name = acc_holder_name
#         self.acc_balance = acc_balance
#
#     def deposit(self, amount):
#         self.acc_balance += amount
#         print(f'Successfully deposited Rs.{amount}')
#
#     def withdraw(self, amount):
#         if isinstance(amount, (int, float)):
#             if amount < self.acc_balance:
#                 self.acc_balance -= amount
#                 print(f'Successfully withdrawn Rs.{amount}')
#             else:
#                 print('Insufficient balance')
#         else:
#             print('Please enter the valid number')
#
#     def balance(self):
#         print(f'The current balance is {self.acc_balance}')
#
# b1 = BankAccount('Ajay', 20000)
# b1.balance()
# b1.deposit(5000)
# b1.balance()
# b1.withdraw(40000)
# b1.balance()

######################################################################################
'''
-------------------------
        Circle          
-------------------------
        x_co : float
        y_co : float
        radius : float
-------------------------
     find_area
     find_circumference
--------------------------        
'''

###########################################################################################
'''
------------------------
    ListData        
------------------------
    list_1: list
-----------------------
    add_data(element)
    delete_data(element)
    find_length()
    find_element
------------------------'''
# class ListData:
#     list_1 = [1, 2, 3, 4, 5, 6]
#
#     def add_element(self, element):
#         self.list_1.append(element)
#         print(self.list_1)
#
#     def delete_element(self, element):
#         if element in self.list_1:
#             self.list_1.remove(element)
#         else:
#             print('No such element found to remove')
#         print(self.list_1)
#
#     def length(self):
#         print(len(self.list_1))
#
#     def find_element(self, element):
#         if element in self.list_1:
#             print(f"Element found and it's index is {self.list_1.index(element)}")
#         else:
#             print('Element not found')
#         print(self.list_1)
#
#
# list_obj = ListData()
# list_obj.length()
# list_obj.add_element(100)
# list_obj.length()
# list_obj.delete_element(5)
# list_obj.delete_element(2)
# list_obj.length()
# list_obj.find_element(1)

#################################################################################
'''21 September 2022'''
'''
-------------------------
        Books   
-------------------------
    Book_data : dict
    book_id : int
    book_name : str
    author : str
    year_of_publish : str
    price : float
-------------------------
    add_new_book
    delete_book
    display_book
    inquire_book
--------------------------
'''
# class Books:
#
#     book_data = {'It ends with us' : {'book_id':123, 'author':'Collen Hoover', 'year':2020, 'price':200},
#                  'The Alchemist' : {'book_id':345, 'author':'Paulo Coelho', 'year':1990, 'price':250},
#                  'Harry Potter' : {'book_id':456, 'author':'JK Rowling', 'year':2000, 'price':500}}
#
#     def add_book(self):
#         while True:
#             choice = int(input('Enter the choice. 1 or 2: '))
#             if choice == 1:
#                 book_name = input('Enter the bookname: ')
#                 if book_name not in self.book_data:
#                     book_id = int(input('Enter the book-id: '))
#                     author = input('Enter the author name: ')
#                     year = input('Enter the year of publish: ')
#                     price = float(input('Enter the price of the book: '))
#                     details = dict([('book_id', book_id), ('author', author), ('year', year), ('price', price)])
#                     self.book_data[book_name] = details
#                 print(self.book_data)
#
#             elif choice == 2:
#                 print('Thank You ! Visit Again')
#                 break

#         else:
#             print('Invalid Request')
#
# def delete_book(self, book):
#     if book in self.book_data:
#         removed_book = self.book_data.pop(book)
#         print(f'{book} is successfully removed')
#     else:
#         print(f'{book} is not present in your cart')
#
# def display_book(self):
#     print(self.book_data)
#
# def inquire_books(self, book):
#     if book in self.book_data:
#         print(f'{book} is present')
#         print(self.book_data[book])
#     else:
#         print(f'{book} is not present in your cart')

# b = Books()
# b.display_book()
# b.add_book()
# b.delete_book('5 point someone')
# b.delete_book('The Alchemist')
# b.display_book()
# b.inquire_books('It ends with us')

###########################################################################################
'''Encapsulation'''
'''
OVERVIEW:
* It describes the idea of wrapping data and the methods that work on data within one unit.
* This puts restrictions on accessing variables and methods directly and can prevent the accidental
    modification of data. 

############################################################
Access Specifiers
1. Public members : It can be accessed anywhere in the class.

2. Protected members : 
* Protected members are those which should not be accessed outside the class according to python coding 
    convention.
* These are for internal use/ implementation only
* To accomplish this in Python, just follow the convention by prefixing the name of the member by a 
    single underscore “_”.

3. Private members : 
* They cannot be accessed either in child classes or outside the classes.
* They are limited to the respective class space.
* To create private members, Add “__” (double underscore ) in front of the variable and method name

############################################################
Property
* Python property() class creates the object of the property class and it is used to create property 
    of a class. 
* Syntax: 
    property(fget=None, fset=None, fdel=None, doc=None)
    fget (optional) - Function for getting the attribute value. Defaults to None.
    fset (optional) - Function for setting the attribute value. Defaults to None.
    fdel (optional) - Function for deleting the attribute value. Defaults to None.
    doc (optional) - A string that contains the documentation (docstring) for the attribute. 
        Defaults to None

#############################################################
Property Decorators
* @property decorator is a built-in decorator in python which is helpful in defining the properties 
    effortlessly without manually calling the inbuilt function property(). 
* Which is used to return the property attributes of a class from the stated getter, setter and deleter 
    as parameters.
* Use @property decorator on any method in the class to use the method as a property.

SYNTAX :

* @property: Declares the method as a property.
* @<property-name>.setter: Specifies the setter method for a property that sets the value to a property.
* @<property-name>.deleter: Specifies the delete method as a property that deletes a property.


'''
# class BankAccount:
#     bank_name = 'SBI'
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
# b = BankAccount('Ram', 10000)
# print(b.name)
# print(b.balance)

'''Access Specifiers
1. Public access specifiers
2. Protected access specifiers
3. Private access specifiers
'''
'''Public'''
# class BankAccount:
#     bank_name = 'SBI'
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
# b = BankAccount('Ram', 10000)
# print(b.name)
# print(b.balance)

'''Protected'''
# class BankAccount:
#     bank_name = 'SBI'
#
#     def __init__(self, name, balance):
#         self.name = name
#         self._balance = balance
#
# b = BankAccount('Ram', 10000)
# print(b.name)
# print(b._balance)
# print(b.__dict__)       #{'name': 'Ram', '_balance': 10000}

'''Private'''
# class BankAccount:
#     bank_name = 'SBI'
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
# class SBI(BankAccount):
#     pass
#
# s = SBI('ram', 10000)
# print(s.__dict__)       #{'name': 'ram', '_BankAccount__balance': 10000}

##########################################################################################
'''22 September 2022'''
# class Account:
#     roi = 4.5
#     _interest = 10
#     __emi = 5
#
#     def rate_of_interest(self):
#         print(f'ROI is {self.roi}')
#
#     def interest_1(self):
#         print(f'Interest is {self._interest}')
#
#     def emi_1(self):
#         print(f'EMI is {self.__emi}')
#
#
# a = Account()
# print(a.roi)        #4.5
# print(a._interest)  #10
# print(a.__emi)      #AttributeError
# a.rate_of_interest()
# a.interest_1()
# a.emi_1()

##############################################################################
# class Account:
#     roi = 4.5
#     _interest = 10
#     __emi = 5
#
#     def rate_of_interest(self):
#         print(f'ROI is {self.roi}')
#
#     def interest_1(self):
#         print(f'Interest is {self._interest}')
#
#     def emi_1(self):
#         print(f'EMI is {self.__emi}')
#
# class Savings(Account):
#     roi = 14.5
#     _interest = 20
#     __emi = 15
#
#     def rate_of_interest(self):
#         print(f'ROI is {self.roi}')
#
#     def interest_1(self):
#         print(f'Interest is {self._interest}')
#
#     def emi_1(self):
#         print(f'EMI is {self.__emi}')
#
# s = Savings()
# # print(s.roi)
# # print(s._interest)
# s.rate_of_interest()
# s.interest_1()
# s.emi_1()

#########################################################################
'''UML Diagrams :      -    -----> Public 
                    +    -----> Private
                    #    -----> Protected'''
################################################################################
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     def get_balance(self):          #getter
#         print(f'Current balance is {self.__balance}')
#
#     def set_balance(self,  amount):     #setter
#         self.__balance += amount
#         print(f'Successfully deposited {amount}')
#
#     def delete_balance(self):       #deleter
#         print('Cant delete balance')
#
# b = BankAccount('Ram', 10000)
# b.get_balance()     #Current balance is 10000
# b.set_balance(2000)
# b.get_balance()
# b.delete_balance()

########################################
# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     def get_balance(self):          #getter
#         print(f'Current balance is {self.__balance}')
#
#     def set_balance(self,  amount):     #setter
#         self.__balance += amount
#         print(f'Successfully deposited {amount}')
#
#     def delete_balance(self):       #deleter
#         print('Cant delete balance')
#
#     my_balance = property(get_balance, set_balance, delete_balance)
#
# b = BankAccount('Ram', 10000)
# b.my_balance
# b.my_balance = 5000
# del b.my_balance

############################################
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     @property
#     def get_balance(self):          #getter
#         return f'Current balance is {self.__balance}'
#
#     @get_balance.setter
#     def get_balance(self,  amount):     #setter
#         self.__balance += amount
#         print(f'Successfully deposited {amount}')
#
#     @get_balance.deleter
#     def get_balance(self):       #deleter
#         print('Cant delete balance')
#
# b = BankAccount('Ram', 10000)
# print(b.get_balance)
# b.get_balance = 5000
# del b.get_balance

#####################################################################################
'''23 September 2022'''
'''create a class SimCard where it has two attributes number and network provider where the
network provider can be changed but number cannot be changed'''
# class SimCard:
#     def __init__(self, number, network):
#         self.__number = number
#         self.__network = network
#
#     @property
#     def get_network(self):      #getter
#         return f'The current network is {self.__network}'
#
#     @get_network.setter
#     def get_network(self, new_network):     #setter
#         self.__network = new_network
#
#     @get_network.deleter
#     def get_network(self):          #deleter
#         print(f'Cant delete network {self.__network}')
#
#     @property
#     def get_number(self):
#         return f'The number is {self.__number}'
#
# sim = SimCard(9876543210, 'BSNL')
# print(sim.get_network)
# sim.get_network = 'Airtel'
# print(sim.get_network)
# del sim.get_network

##############################################################################
'''
-------------------------
        Student
-------------------------
        - schoolname
        - stu_name
        - stu_id
        + marks
------------------------
    display_marks()
------------------------
'''
# class Student:
#     school_name = 'VidyaMandir'
#
#     def __init__(self, stu_name, stu_id, phy, che, math):
#         self.stu_name = stu_name
#         self.stu_id = stu_id
#         self.__phy = phy
#         self.__che = che
#         self.__math = math
#
#     def student_details(self):
#         print(f'The student name is {self.stu_name} and ID is  {self.stu_id}')
#
#     @property
#     def phy_marks(self):
#         return f'Physics marks is {self.__phy}'
#
#     @phy_marks.setter
#     def phy_marks(self, new_phy_marks):
#         self.__phy = new_phy_marks
#
#     @property
#     def che_marks(self):
#         return f'Chemistry  marks is {self.__che}'
#
#     @che_marks.setter
#     def che_marks(self, new_che_marks):
#         self.__che = new_che_marks
#
#     @property
#     def math_marks(self):
#         return f'Math marks is {self.__math}'
#
#     @math_marks.setter
#     def math_marks(self, new_math_marks):
#         self.__math = new_math_marks
#
#     def total_marks(self):
#         total = self.__phy + self.__che + self.__math
#         print(f'TOTAL MARKS = {total}')
#         if total > 105:
#             return 'PASS'
#         else:
#             return 'FAIL'
#
# s = Student('Krish', 1234, 20, 21, 22)
# print(s.phy_marks)
# print(s.che_marks)
# print(s.math_marks)
# print(s.total_marks())
# s.phy_marks = 90
# s.che_marks = 95
# s.math_marks = 98
# print()
# print(s.phy_marks)
# print(s.che_marks)
# print(s.math_marks)
# print(s.total_marks())

##############################################################################
'''Abstraction 
* Abstraction is a process of hiding the implementation of an application.
* An abstract class can be considered as a blueprint for other classes.
* Abstract classes are classes that contain one or more abstract methods. 
* An abstract method is a method that is declared in the abstract class, but contains no 
    implementation.
* Abstract classes cannot be instantiated, and require subclasses to provide implementations 
    for the abstract methods.

CONVENTIONS TO CREATE ABSTRACT CLASS
    Import abstract base class
        from abc import ABC , abstractmethod
    Inherit ABC in the base class.
        class ClassName(ABC)
    Create an abstract method.
        @abstractmethod
    Give implementation to all abstract method in all the child classes.

NOTE:
* The abstract base class may have more than one abstract methods and also normal methods.
* The child class must implement all of the abstract methods from abstract class failing which
    TypeError will be raised.
* We cannot create an instance or object for the abstract class  → TypeError
* A class that is derived from an abstract class cannot be instantiated unless all of its 
    abstract methods are overridden.
* An abstract method can have an implementation in the abstract class! Even if they are 
    implemented, the subclasses will be forced to override the implementation.
'''
# from abc import ABC, abstractmethod
# class ATM(ABC):
#     @abstractmethod
#     def withdraw(self):
#         pass
#
#     @abstractmethod
#     def deposit(self):
#         pass
#
#     @abstractmethod
#     def balance(self):
#         pass
#
# class SBI(ATM):
#     def withdraw(self):
#         print('In SBI Class, withdraw method')
#
#     def deposit(self):
#         print('In SBI Class, deposit method')
#
#     def balance(self):
#         print('In SBI Class, balance method')
# #
# s = SBI()
# s.deposit()

#########################################################################################
'''Polymorphism
OVERVIEW
* Poly - Many, Morphs - forms
* Polymorphism refers to the ability of the object with the same name to carry out different 
    functionality altogether.

##########################
TYPES
* Polymorphism w.r.t inbuilt function
* Polymorphism in operators
* Polymorphism in class methods
* Polymorphism w.r.t inheritance → overriding

######################################################
Overriding v/s Overloading
* Overriding is a concept in which if objects are with same name then the latest one will be retained.
* Overloading is a concept in which if the functions/ methods with same name have different arguments,
    each can be called with respect to their arguments.
'''
##########################################################
'''wrt inbuilt func'''
# print(len('python is awesome'))     #number of characters
# print(len([10, False, 0, True, 7.8, 'python'])) #number of words/elements
# print(len((10, False, 0, True, 7.8, 'python'))) #number of words/elements
# print(len({10, False, 0, True, 7.8, 'python'})) #number of keys
# print(len({'karnataka':'kannada', 'Andhra':'Telugu', 'Kerala':'Malayalam', 'TamilNadu':'Tamil'}))   #number of key-value pairs

'''wrt operators'''
# print(4 + 7)        #addition
# print('hai' + 'hello')  #concatenation
# print([1, 2, 3] + [7, 8, 9])        #concatenation
#
# print(9 - 6)        #subtraction
# print({1, 2, 3, 4, 5, 6} - {2, 4, 6})       #difference method
#
# print(8 * 3)        #multiplication
# print('hai' * 3)        #concatenation

##########################
# def add(a, b, c=0):
#     print(a + b + c)
#
# add(1, 2, 3)
# add(2, 3)

#########################
# class Sample:
#     def display(self):
#         print('Sample class display method executing')
#
#
# class Example:
#     def display(self):
#         print('Example class display method executing')
#
#
# s = Sample()
# e = Example()
# s.display()
# e.display()

#####################################################
import random

user_win = 0
comp_win = 0
options = ['rock', 'paper', 'scissors']

while True:
    choice = input('Choose rock/paper/scissors OR Q to quit: ').lower()

    if choice == 'q':
        break

    if choice not in options:
        print('Enter the valid option')
        continue

    number = random.randint(0, 2)
    comp_pick = options[number]
    print(f"Computer's choice is {comp_pick}")

    if choice == comp_pick:
        print('Same choices, Choose again')
        continue

    if choice == 'rock' and comp_pick == 'scissors':
        print('USER WINS...!!')
        user_win += 1

    elif choice == 'paper' and comp_pick == 'rock':
        print('USER WINS...!!')
        user_win += 1

    elif choice == 'scissors' and comp_pick == 'paper':
        print('USER WINS...!!')
        user_win += 1

    else:
        print('COMPUTER WINS')
        comp_win += 1

if user_win == comp_win:
    print('DRAW MATCH')
elif user_win > comp_win:
    print(f'YOU HAVE WON {user_win} TIMES')
    print('CONGRATULATIONS. YOU WON !!')
else:
    print(f'COMPUTER HHAS WON {comp_win} times')
    print('OOPs. YOU LOST. BETTER LUCH NEXT TIME')