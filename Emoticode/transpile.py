import os
import re

def error(e):
  raise Exception(f'\nErr: {e}')

def fix(code):
  
  li = code
  
  # fixing basic characters
  li = li.replace('\n', '')
  li = li.replace('😒', '😒🛑')
  li = li.replace('\t', '')
  li = li.replace(r'\n', '')
  li = li.replace(r'\t', '')
  li = li.replace(r'\"', '')
  li = li.replace(r"\'", '')
  li = li.replace(r'\b', '')
  li = li.replace(r'\r', '')
  commentReg = re.compile(r"💬[\s\S]*?💬", re.MULTILINE)
  li = re.sub(commentReg, '', li)

  # finding string prefixes
  def searchReg(x):
    return re.compile(fr"{x}\"[^\n]*?\"|{x}\'[^\n]*?\'", flags=re.UNICODE | re.MULTILINE | re.IGNORECASE)

  #finding fixed string prefixes
  def fixed(c):
    return re.compile(fr"({c})(?=\"[\s\S]*?\")|({c})(?=\'[\s\S]*?\')", flags=re.UNICODE | re.MULTILINE | re.IGNORECASE)
  
  chars = {
    "fr" : '🗿🥩',
    "rf" : '🥩🗿',
    "rb" : '🥩🍽',
    "br" : '🍽🥩',
    "f" : '🗿',
    "r" : '🥩',
    "b" : '🍽',
    "u" : '🍞'
  }
  
  
  for i in chars:
    if re.findall(searchReg(i), code):
      error(f'Unknown string modifier \"{i}\", did you mean \"{chars[i]}\"?')

    li = re.sub(fixed(chars[i]), i, li)
  li = re.sub(r'(?:f|fr|rf)"[^"]*"|(?:f|fr|rf)\'[^\']*\'', lambda x: x.group().replace("{", "{{").replace("}", "}}"), li)

  li = re.sub(r'(?:f|fr|rf)"[^"]*"|(?:f|fr|rf)\'[^\']*\'', lambda x: x.group().replace("🤜", "{").replace("🤛", "}"), li)
  li = li.replace('🤜', '🤜🛑').replace('🤛', '🤛🛑')
  for i in (a := {
    "!": "not",
    "&&": "and",
    "\|\|": "or"
  }):
    li = re.sub(fr'{i}(?=([^\"]*\"[^\"]*\")*[^\"]*$)', a[i], li)
  
  return li






def convert(file, filepath):
  escape = {
    r'\🦘' : '\\t',
    r'\💔' : '\\n',
    r'\⏮️' : '\\r',
    r'\⏪' : '\\b',
    r'\🔠' : r'\"',
    r'\🔡' : r"\'"
  }
  
  code = fix(file)
  
  for i in escape:
    code = code.replace(i, escape[i])
  code = code.split('🛑')
  code = [txt.strip() for txt in code]
  for i in code:
    if(len(i)==0):
        code.remove(i)
  with open('build.py', 'w') as f: f.write('import time\n')
  with open('build.py', 'a') as f:
    indent = 0
    indentBypass = "😒🤷😮‍💨"
    
    for line in code:
      # add indents
      if line[0] not in indentBypass:
        f.write(f'{"  " * indent}')
      else:
        f.write(f'{"  " * (indent - 1)}')
      if indent < 0:
        indent = 0

      # print statements
      if line.startswith('🗣'):
        f.write(f'print({line[2:]})\n')

      # set variables
      elif line.startswith('✏'):
        line = line[2:].split(' 👉 ')
        f.write(f'{line[1]} = {line[0]}\n')

      # string input
      elif line.startswith('🙏'):
        line = line[2:].split(' 👉 ')
        f.write(f'{line[1]} = input({line[0]})\n')

      # integer input
      elif line.startswith('🔢'):
        line = line[2:].split(' 👉 ')
        f.write(f'{line[1]} = int(input({line[0]}))\n')

      # define functions
      elif line.startswith('⚙️'):
        if "," in line:
          line = line[2:].split(',', 1)
          line = [line[0]] + line[1].split(' 🤜', 1)
          indent += 1
          f.write(f'def {line[0]}({line[1]}):\n')
        else:
          line = line[2:].split(' 🤜', 1)
          indent += 1
          f.write(f'def {line[0]}():\n')

      # close bracket
      elif line == '🤛':
        indent -= 1
        f.write('\n')

      # call functions
      elif line.startswith('📢'):
        if " 👉 " in line:
          if "," in line:
            line = line[2:].split(' 👉 ')
            line = line[0].split(',', 1) + [line[1]]
            f.write(f'{line[2]} = {line[0]}({line[1]})\n')
          else:
            line = line[2:].split(' 👉 ')
            f.write(f'{line[1]} = {line[0]}()\n')
        else:
          if "," in line:
            line = line[2:].split(',', 1)
            f.write(f'{line[0]}({line[1]})\n')
          else:
            line = line[2:]
            f.write(f'{line}()\n')

      # if statements
      elif line.startswith('🤔'):
        line = line.split(' ', 1)
        line = [line[0]] + line[1].split(' 🤜', 1)
        indent += 1
        f.write(f'if {line[1]}:\n')

      # else statements
      elif line == '😒':
        f.write('else:\n')

      # elif statements
      elif line.startswith('🤷'):
        line = line.split(' ', 1)
        line = [line[0]] + line[1].split(' 🤜', 1)
        f.write(f'elif {line[1]}:\n')

      # while loop
      elif line.startswith('🌀'):
        line = line.split(' ', 1)
        line = [line[0]] + line[1].split(' 🤜', 1)
        indent += 1
        f.write(f'while {line[1]}:\n')

      elif line == '💀':
        f.write('break\n')

      # increment
      elif line.startswith('👆'):
        line = line.split(' ', 1)
        f.write(f'{line[1]} += 1\n')

      # decrement
      elif line.startswith('👇'):
        line = line.split(' ', 1)
        f.write(f'{line[1]} -= 1\n')

      # return
      elif line.startswith('👍'):
        line = line.split(' ', 1)
        f.write(f'return {line[1]}\n')

      # continue
      elif line == '⏭':
        f.write('continue\n')

      # clear screen
      elif line == '💥':
        f.write('print("\033c", end="")\n')

      # sleep
      elif line.startswith('😴'):
        line = line[2:].split(' ', 1)
        f.write(f'time.sleep(({line[0]})/1000)\n')

      # import
      elif line.startswith('📦'):
        line = line[2:].split(' ', 1)
        f.write(f'import {line[0]}\n')

      # open file
      elif line.startswith('📂'):
        line = line[2:].split(' 👉 ')
        line = line[0].split(',', 1) + [line[1]]
        line[1] = line[1].replace('"', '').replace("'", '').strip()
        line[0] = line[0].replace('"', '').replace("'", '').strip()
        line[1] = ('"r"' if line[1] == 'read' else '"w+"' if line[1] == 'write' else '"a+"' if line[1] == 'add' else '"stupid"')
        line[0] = f'{os.path.dirname(filepath)}/' + line[0]
        f.write(f'{line[2]} = open("{line[0]}", {line[1]})\n')

      # close file
      elif line.startswith('📁'):
        line = line[1:].split(' ', 1)
        f.write(f'{line[1]}.close()\n')

      # comments
      elif line.startswith('💬'):
        pass

      # classes
      elif line.startswith('🏫 '):
        if " 🌮 " in line:
          line = line.split(' ', 1)[1].split(' 🌮 ')
          #line = line[0].split(',', 1) + [line[1]]
          line = [line[0]] + line[1].split(' 🤜', 1)
          indent += 1
          f.write(f'class {line[0]}({line[1]}):\n')
        else:
          line = line.split(' ', 1)
          line = line[1].split(' 🤜', 1)
          indent += 1
          f.write(f'class {line[0]}(object):\n')

      # init garbage
      elif line.startswith('🧑‍🏫'):
        line = line.split(' ', 1)
        line = line[1].split(' 🤜', 1)
        indent += 1
        f.write(f'def __init__(this, {line[0]}):\n')
        
      # declare self vars
      elif line.startswith('🧑‍🎓'):
        line = (line.split(' ', 1)[1]).split(' 👉 ')
        f.write(f'this.{line[1]} = {line[0]}\n')

      # delete classes and their properties
      elif line.startswith('🏫🔫'):
        line = line.split(' ', 1)
        f.write(f'del {line[1]}\n')
      
      # try statement
      elif line == '😤 🤜':
        indent += 1
        f.write('try:\n')
      
      # except statement
      elif line.startswith('😮‍💨'):
        line = (line.split('🤜', 1))[0]
        if " 👉 " in line:
          line = line.split(' ', 1)[1].split(' 👉 ')
          f.write(f'except {line[0]} as {line[1]}:\n')
        else:
          line = line.split(' ', 1)[1].split(',', 1)
          f.write(f'except {line[0]}:\n')

      # classes string statement
      elif line == '🔤 🤜':
        indent += 1
        f.write('def __str__(this):\n')

      # classes repr statement
      elif line == '🗃 🤜':
        indent += 1
        f.write('def __repr__(this):\n')

      # classes del statement
      elif line == '🗑 🤜':
        indent += 1
        f.write('def __del__(this):\n')

      # pass
      elif line == '🫥':
        f.write('pass\n')

      # function decorators
      elif line.startswith('💄'):
        f.write(f'@{line.split(" ", 1)[1]}\n')

      # global var
      elif line.startswith('🌎'):
        f.write(f'global {line.split(" ", 1)[1]}\n')
      
      # unknown command
      else:
        error(f'Unknown command "{line}"')