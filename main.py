import sys
import importlib
import subprocess
import os
from rules import *

sys.dont_write_bytecode = True   # To not generate __pycache__ folder

rule_path = "rules"


def main():

  if (sys.argv[1] == "--all"):
    for rulefile in os.listdir(rule_path):
      make_ly(rulefile[:-3])   # Remove ".py" from end of file
  
  else: 
    make_ly(sys.argv[1])



def make_ly(rule_filename):

  try:
    rule_file = importlib.import_module(f"{rule_path}.{rule_filename}")
    title = create_title_string(rule_filename)
  
  except IndexError:
    print("\nNeed rule filename\n")
    exit()
     
  except ModuleNotFoundError:
    print(f"\n Can't find rule file: {rule_path}/{rule_filename}.py\n")
    exit()
    
  rule_file.create_rulefile(title)

  # Run Lilypond
  subprocess.check_call(f"lilypond -o pdf/{rule_filename} ly/main.ly", shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)



def create_title_string(title):
  
  title = title.replace('_', ' ')
  title = title_capitalize(title)

  title_string = ""
  last_char = ""
  number = ""
  digit_started = False

  for char in title:
    
    if (digit_started and (last_char == 't') and (char == 'h')):
      title_string = title_string[:-(1+len(number))]
      title_string += f"\concat{{{number} \super th}} "
      digit_started = False
      number = ""

    elif (digit_started and (last_char == 'n') and (char == 'd')):
      title_string = title_string[:-(1+len(number))]
      title_string += f"\concat{{{number} \super nd}} "
      digit_started = False
      number = ""

    elif (char.isdigit()):
      digit_started = True
      number += char
      title_string += char
      
    else:
      title_string += char

    last_char = char

  # with open("ly/title.ly", "w") as file:
  #   file.write(f'title = \markup {{{title_string}}}\n')
  #   file.write(f'instrument = \markup {{{title_string}}}\n')
  
  return title_string



def title_capitalize(title):
  
  cap_string = ""
  last_char = " "

  for char in title:

    if ( char.islower() and not last_char.isalnum()):
      char = char.capitalize()

    last_char = char
    cap_string += char

  return cap_string



if __name__ == "__main__":
    main()
