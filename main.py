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
    title = sys.argv[1]
    title = title.replace('_', ' ').title()
    rule_file = importlib.import_module(f"{rule_path}.{sys.argv[1]}")
  
  except IndexError:
    print("\nNeed rule filename\n")
    exit()
     
  except ModuleNotFoundError:
    print(f"\n Can't find rule file: {rule_path}/{sys.argv[1]}.py\n")
    exit()

  with open("ly/title.ly", "w") as file:
    file.write(f'title = "{title}"\n')
    file.write(f'instrument = "{title}"\n')
    
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



if __name__ == "__main__":
    main()
