# **emoticode**<br>*the gentlemen’s programming language*

### Introduction
This documentation will teach you almost everything you need to know to start programming with Emoticode. There will be plenty of code snippets that will show examples of how the code would look. The code snippets will typically contain two code blocks, first one being the code, and the second one being the result.

<hr>

### Printing and Basic Syntax
Here is the classic "Hello World!" script written in Emoticode:
```py
🗣 "hello world" 🛑
```
```
hello world
```

Lets walk through it:<br>
The `🗣` statement tells the program that you want to print something, then prints what comes after it. Once you finish your line of code, you finish every line in emoticode with a `🛑`. A `🛑` tells the computer that you are finished with that line, and is ready to move on to the next task. `🛑` works like the familiar semi-colon in many languages, so you can actually put multiple expressions together on one line:
```py
🗣 "hello world" 🛑 🗣 "hello universe" 🛑
```
```
hello world
hello universe
```

<hr>

### Comments
Comments are multiline and start and end with a `💬`. You can use them to quickly disable a block of code for debugging, or to add notes and documentation to make your program more understandable:

```py
💬 this is commented out 💬

🗣 "this is NOT commented out" 🛑

💬
🗣 "this block of code" 🛑
🗣 "is commented out and wont run" 🛑
💬
```
```
this is NOT commented out
```

<hr>

### Variables
Variables are created using the `✏️` statement. After the `✏️`, you have the value you want to assign to the variable, then a `👉` which allows you to then specify the variable name.<br>
If the variable does not already exist, a new variable will be created, otherwise the old value will be overwritten:
```py
✏️ "hello world" 👉 my_string 🛑
✏️ 69 👉 my_integer 🛑
✏️ [1,2] 👉 my_list 🛑
```

You can use variables by simply adding them to a print statement, or wherever else you need to use them:
```py
✏️ "hello world" 👉 my_string 🛑
✏️ [1,2] 👉 my_list 🛑
🗣 "my string is " + my_string 🛑
🗣 "my list is " + my_list 🛑
🗣 "my list first element is " + my_list[0] 🛑
```
```
my string is hello world
my list is [1,2]
my list first element is 1
```

<hr>

### User Input
User input can be gathered as either string or integer. To ask the user for a string, use the `🙏` function with the message to send in the console. The input is then assigned to a variable similar to the default variable creation syntax by seperating the message and name with a `👉`. Integer input follows the same syntax but with a `🔢` instead of a `🙏`:
```py
🔢 "Enter a number: " 👉 num1 🛑
🙏 "Enter a string: " 👉 string1 🛑
```
```
Enter a number: <user input>
Enter a string: <user input>
```

> - 🔢 is for integer input
> - 🙏 is for string input

<hr>

### Functions
Functions are defined with a `⚙️` and called with a `📢`.<br>
Arguments for defining functions and calling them are separated by commas (`My_Function, a, b`):
```py
⚙️ add, x,y 🤜
  🗣 x + y 🛑
🤛

📢 add, 69,420 🛑
```
```
489
```

You can use `👍` to return a value and use the `👉` to assign the returned value to a variable:
```py
⚙️ add, x,y 🤜
  👍 x + y 🛑
🤛
📢 add, 69, 420 👉 c 🛑
```
```
489
```
You can also change the "type" or behavior of a function using function decorators, but they are not very important right now.
```py
💄 myDecorator 🛑
⚙️ hello_decorator 🤜
    🗣 "Gfg" 🛑
🤛

💬 Above code is equivalent to - 💬

⚙️ hello_decorator 🤜
    🗣 "Gfg" 🛑
🤛

📢 myDecorator, hello_decorator 👉 hello_decorator 🛑
```
> Code blocks for things like functions, if statements, and while loops are all opened and closed using an opening `🤜` and a closing `🤛`.
> Since these act as curly braces, Emoticode is also not indent sensitive.

<hr>

### If Statements
`If:` statements are created with a `🤔`, `else if/elif:` statements are created with a `🤷`, and `else:` statements with a `😒`:
```py
✏️ 69 👉 n 🛑
🤔 n == 1 🤜
    🗣 'n is 1' 🛑
🤷 n == 2 🤜
    🗣 'n is 2' 🛑
😒
    🗣 'n is not 1 or 2' 🛑
🤛
```
```
n is not 1 or 2
```
> Keep in mind that a `😒` does not use a `🤜` after it.
> However, its code block still must be closed with a `🤛`

<hr>

### Looping
A while loop is created using a `🌀` followed by a condition.<br>
A while loop also still must have an opening and closing `🤜🤛`:
```py
🌀 True 🤜
    🗣 'w infinite loop' 🛑
🤛
```
```
w infinite loop
w infinite loop
w infinite loop
w infinite loop
<will keep repeating infinitely>
```
To break out of a while loop a `💀` statement is used which kills the loop:
```py
🌀 True 🤜
    🗣 'w infinite loop' 🛑
    💀 🛑
🤛
🗣 'aww loop died :(' 🛑
```
```
w infinite loop
aww loop died :(
```

Emoticode does not currently support for-loops so the while loop with an increment variable must be used instead:
```py
✏️ [1,2] 👉 my_list 🛑
✏️ 0 👉 i 🛑

🌀 i <= len(my_list) 🤜
    🗣 my_list[i] 🛑
    ✏️ i + 1 👉 i 🛑
🤛

🗣 'so you want a normal for loop? you can kiss my 🍑' 🛑
```
```
1
2
so you want a normal for loop? you can kiss my 🍑
```

### Increment and Decrement
Emoticode has a method to increment or decrement a variable by one by using a `👆` and `👇` emoji so this makes for loops kinda easier, but you still dont get normal for loops:
```py
✏️ [1,2] 👉 my_list 🛑
✏️ 0 👉 i 🛑


🌀 i <= len(my_list) 🤜
    🗣 my_list[i] 🛑
    👆 i 🛑
🤛
🗣 'so you want a normal for loop? you can kiss my 🍑' 🛑
```
```
1
2
so you want a normal for loop? you can kiss my 🍑
```

> Here you see im lazy so there are default python functions like len() 

To continue to next iteration of a loop use a `⏭` like this:
```py
✏️ 0 👉 i 🛑

🌀 i <= 5 🤜
    🤔 n == 1 🤜 ⏭ 🛑 🤛
    🗣 i 🛑
    👆 i 🛑
🤛
```
```
0
2
3
4
5
```

<hr>

### String Prefixes
Just like other languages with multiple string types, Emoticode uses string prefixes like Python. The most common is `🗿` which is for string comprehension with similar syntax to Python. Insert variables by using a pair of opening and closing `🤜🤛` with a variable name in between:
```py
✏️ "hello world" 👉 my_string 🛑
💬 variable-string 💬
🗣 🗿"my string is 🤜my_string🤛" 🛑
```
```
my string is hello world
```
Every other string prefix follows a similar format but with different Emoticons (escape characters will be shown in a later chapter):
```py
✏️ "hello world" 👉 my_string 🛑
💬 variable-string 💬
🗣 🗿"my string is 🤜my_string🤛" 🛑
💬 raw string 💬
🗣 🥩"escape chars wont be escaped \" 🛑
💬 byte string 💬
🗣 🍽"this string will be formatted as bytes" 🛑
💬 unicode string 💬
🗣 🍞"you shouldnt even use this because its the default" 🛑
```
```
my string is hello world
escape chars wont be escaped \
b'this string will be formatted as bytes'
you shouldnt even use this because its the default
```

> Some string prefixes can also be combined such as a raw variable-string (`🥩🗿`) or even raw byte string (`🍽🥩`).
> The order of the emojis does not matter

<hr>

### Quality-of-Life Quick Commands
To clear the console using the built in clear command, use the `💥` statement<br>
You can also sleep for X milliseconds with the `😴` statement:
```py
🗣 'heres some text' 🛑

💬 sleep one second 💬
😴 1000 🛑
🗣 'it has been one second' 🛑
🙏 "Press enter to continue" 👉 a 🛑

💬 clear the screen 💬
💥 🛑
🗣 'no shot the screen got cleared' 🛑
```
```
heres some text
<execution pauses for 1 second>
it has been one second
Press enter to continue<user input>
<console is cleared>
no shot the screen got cleared
```

<hr>

### Packages
Emoticode, being programmed in python, also supports python packages!<br>
To import a Python/Emoticode package, first make sure you have the package files installed, then use the `📦` statement followed by the module name:
```py
💬 import the math module 💬
📦 math 🛑

⚙️ square_root, num 🤜
  👍 math.sqrt(num) 🛑
🤛
🔢 "Insert a number to square root: " 👉 number 🛑
📢 square_root, number 👉 result 🛑 🗣️ result 🛑
```
```
Insert a number to square root: <user input>
<square root of "number" is printed>
```
You can also call the function like a normal function:
```py
📦 math 🛑

🔢 "Insert a number to square root: " 👉 number 🛑
📢 math.sqrt, number 👉 result 🛑 🗣️ result 🛑
```
```
Insert a number to square root: <user input>
<square root of "number" is printed>
```

<hr>

### File Handling
Emoticode also has built in file handling!<br>
Open a file in the current directory using the `📂` statement and then close the file with `📁`:
```py
💬 open the file "somecode" for reading 💬
📂 "somecode.🔥", "read" 👉 f 🛑

💬 print the contents of the file 💬
🗣️ f.read() 🛑

💬 close the file 💬
📁 f 🛑
```
```
<reads and prints all the text contents of "somecode.🔥">
```

The `📂` function takes two arguments, the file path and the action (read, write, or add) which do the following:
- read  : open the file for reading only
- write : open the file for writing and create a new file if the one specified does not exist. when you write to the file, it replaces all of its contents, so it may be safe to store the contents in a variable (✏️ f.read() 👉 backup 🛑) before overwriting them
- add   : open the file for appending and create one if it does not exist. like the write mode, you can also read the contents of the file which can help to insert text into a specific spot in the file instead of the end of the file
You then assign the file to a variable (such as f) so you can manipulate it. When you are finished with the file, you can close it with 📁 which takes one argument, the file’s variable.

<hr>

### Escape Characters
Just like other languages Emoticode also comes with some build in escape characters except that they use emojis as usual, here is a refrence:

| Symbol | Result          |
|:------:|--------         |
| `\💔`  | Line break      |
| `\🦘`  | Tab indent      |
| `\⏮️`  | Carriage return |
| `\⏪`  | Backspace       |
| `\🔠`  | Double quote    |
| `\🔡`  | Single Quote    |

> ### 🚨 WARNING
> Emoticode does not support classic escape characters such as `\n` or `\t`!
> You must use the unique Emoticode escape characters in place of original escape characters
> Classic escape characters will be deleted during interpretation

<hr>

### Classes
If you decide to create object-oriented code, you will most likely need to use classes.<br>
To create a class, you will need to initiate it with the `🏫` statement.
```py
💬 create a class with its my_value variable set to 5 💬
🏫 My_Class 🤜
  ✏️ 5 👉 my_value 🛑
🤛
```
To access a class and its properties, it is typically good practice to create a new object using the class so you don't modify the class itself, but you can directly modify the class too:
```py
🏫 My_Class 🤜
  ✏️ 5 👉 my_value 🛑
🤛
💬 create a new object variable of My_Class 💬
✏️ My_Class 👉 my_object 🛑
💬 print the value of my_value of the object 💬
🗣 my_object.my_value 🛑

✏️ 6 👉 my_object.my_value 🛑

🗣 my_object.my_value 🛑
🗣 My_Class.my_value 🛑
```
```
5
6
5
```
You can insert the optional argument of what type of class it should be using the `🌮` operator. You can use this to make one class inherit properties from another class:
```py
💬 if I created a class called "object", this class would inherit all the properties 💬
🏫 My_Class 🌮 object 🤜
  ✏️ 5 👉 my_value 🛑
🤛
🗣 My_Class.my_value 🛑
```
```
5
```
To create a class with arguments, you must declare them using the "teacher `🧑‍🏫`", and assign the values to the "students `🧑‍🎓`":
```py
🏫 My_Class 🤜
  💬 create a class with arguments "first_name" and "last_name" 💬
  🧑‍🏫 first_name, last_name 🤜
    🧑‍🎓 🗿"🤜last_name🤛, 🤜first_name🤛" 👉 name 🛑
  🤛
🤛
✏️ My_Class("John", "Doe") 👉 my_object 🛑
🗣 my_object.name 🛑
```
```
Doe, John
```
You can create multiple object values based on specified values as well:
```py
🏫 My_Class 🤜
  🧑‍🏫 grade1, grade2, grade3 🤜
    🧑‍🎓 grade1 👉 first_grade 🛑
    🧑‍🎓 grade2 👉 second_grade 🛑
    🧑‍🎓 grade3 👉 third_grade 🛑
    💬 create the "average" value for the class 💬
    💬 can be done using argument values too but not in other functions 💬
    🧑‍🎓 (this.first_grade + this.second_grade + this.third_grade) // 3 👉 average 🛑
  🤛
🤛
✏️ My_Class(100, 90, 95) 👉 my_object 🛑
🗣 my_object.average 🛑
```
```
95
```
To create a string representation of an object, create a `🔤` function that returns the intended string representation using `👍`:
```py
🏫 My_Class 🤜
  🧑‍🏫 first_name, last_name 🤜
    🧑‍🎓 first_name 👉 firstname 🛑
    🧑‍🎓 last_name 👉 lastname 🛑
  🤛
  
  🔤 🤜
    💬 when this class is converted to a string, this will be its value 💬
    👍 🗿"🤜this.lastname🤛, 🤜this.firstname🤛" 🛑
  🤛
🤛
✏️ My_Class("John", "Doe") 👉 my_object 🛑
🗣 my_object 🛑
```
```
Doe, John
```
To create a printable representation of an object, create a `🗃` function that returns the intended printable representation. `🗃` and `🔤` work very similarily, but `🔤` is intended for human reading while `🗃` is for the program to read:
```
🏫 My_Class 🤜
  🧑‍🏫 first_name, last_name 🤜
    🧑‍🎓 first_name 👉 firstname 🛑
    🧑‍🎓 last_name 👉 lastname 🛑
  🤛

  🗃 🤜
    💬 when this class is being printed or read as a whole, this will be its value 💬
    👍 🗿"🤜this.lastname🤛, 🤜this.firstname🤛" 🛑
  🤛
🤛
✏️ My_Class("John", "Doe") 👉 my_object 🛑
🗣 my_object 🛑
```
```
Doe, John
```

> that is all the current documentation
> I will update it eventually
