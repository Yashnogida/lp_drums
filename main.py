import sys
import importlib
import subprocess
import inspect

rule_path = "rules"

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

    for note_array in note_data:

      # Make the note entries evenly spaced based on the widest note symbol
      max_str_len = max(len(value) for value in rule_file.note_sym.values())
      note_array = [x + " " * (max_str_len - len(x)) for x in note_array]
      
      note_string = rule_file.format(note_array)
      
      # Deal with Triplets. TODO: Generalize it to Prime
      if ((rule_file.notes_per_measure % 3) == 0):
        for chunk in chunker(note_array, 3):
          tuple_string = rf"\tuplet 3/2 {{{' '.join(chunk)}}} "
          file.write(''.join(tuple_string))

      else:
        file.write(note_string)

      file.write("\n")

    file.close()   

  # Run Lilypond
  try:
    subprocess.check_call(f"lilypond -o pdf/{sys.argv[1]} ly/main.ly", shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)
  except subprocess.CalledProcessError:
    print('Calling "lilypond" failed. Is it installed?')
  

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

if __name__ == "__main__":
    main()
