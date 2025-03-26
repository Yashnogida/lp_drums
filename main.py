import sys
import importlib
import subprocess

rule_path = "rules"

#  TODO:
#  - Superscript "th" for titles
#  - implement post rule and post-rule exception
#  - implement prime-number tuplet generalization


def main():

  try:
    rule_file = importlib.import_module(f"{rule_path}.{sys.argv[1]}")

    title = sys.argv[1]
    title = title_create(title)
  
  except IndexError:
    print("\nNeed rule filename\n")
    exit()
     
  except ModuleNotFoundError:
    print(f"\n Can't find rule file: {rule_path}/{sys.argv[1]}.py\n")
    exit()
    
  with open("ly/time.ly", "w") as file:
    file.write(rf'\time {rule_file.time_signature}')

  with open("ly/notes.ly", "w") as file:
    
    note_data = rule_file.generate()
    note_data = rule_file.format(note_data)

    for note_string in note_data:
      file.write(note_string)

    file.close()   

  # Run Lilypond
  subprocess.check_call(f"lilypond -o pdf/{sys.argv[1]} ly/main.ly", shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)



def title_create(title):
  
  title = title.replace('_', ' ')
  title = title_capitalize(title)

  title_string = ""
  last_char = ""
  number = ""
  digit_started = False

  for char in title:
    
    if (digit_started and (last_char == 't') and (char == 'h')):
      title_string = title_string[:-(1+len(number))]
      title_string += f" \concat{{{number} \super th }} "
      digit_started = False
      number = ""

    elif (char.isdigit()):
      digit_started = True
      number += char
      title_string += char
      
    else:
      title_string += char

    last_char = char
    

  with open("ly/title.ly", "w") as file:
    file.write(f'title = \markup {{{title_string}}}\n')
    file.write(f'instrument = \markup {{{title_string}}}\n')

  # title = \markup {Snare-Kick 8\super th -16\super th Note Left Hand Patterns}
  # instrument = \markup {Snare-Kick 8 \super th -16 \super th Note Left Hand Patterns}
  
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
