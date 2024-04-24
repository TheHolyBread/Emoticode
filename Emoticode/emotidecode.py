from Emoticode.transpile import convert


def run(file: list):
  """Give the file to run as a tuple with the first element being the file's contents and the second element being the file's path"""
  convert(file[0], file[1])