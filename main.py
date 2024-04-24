###############
#   IMPORTS   #
###############

import Emoticode.emotidecode
from Emoticode.transpile import error
import os
import runpy


def console():
  while True:
    a = input('C:/scripts > ')
    if a == 'help':
      print(
        """dir - list all emoticode files in current directory
build <filename> - transpile emoticode file to python, leave out file extension
cls - clear console""")
      return
    elif a == 'cls':
      os.system('clear')
      return
    if a.startswith('build '):
      filename = a[6:]
      break
    if a == 'run':
      runpy.run_path("build.py")
      return
    if a.startswith('dir'):
      for files in os.walk(r'scripts/'):
        for file in files[2]:
            if file.endswith('.🔥'):
                print(file)
    else: print('unknown command')
  global emoticodefile
  try:
    with open(f'scripts/{filename}.🔥', 'r') as f:
      global emoticodefile
      emoticodefile = [f.read(), os.path.abspath(f.name)]
  except:
    print(f'file ({filename}.🔥) not found')
    return

  try:
    print("Starting build...")
    Emoticode.emotidecode.run(emoticodefile)
    print(f"Build of {filename + '.🔥'} completed successfully")
    runpy.run_path("build.py")
  except Exception as e:
    print(e)


while True:
  console()