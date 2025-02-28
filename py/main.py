import sys
import importlib

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

    note_array = []
    note_text = []

    for i in range (pow(len(rule_file.note_sym), rule_file.notes_per_measure)):
      
      note_array = convert_base(i, len(rule_file.note_sym))
      
      while(len(note_array) < rule_file.notes_per_measure):
        note_array.insert(0, 0)
      
      if (rule_file.pre_rule(note_array, rule_file.notes_per_measure)):
        continue

      note_array = [rule_file.note_sym[x] for x in note_array]

      # Deal with Triplets
      if ((rule_file.notes_per_measure % 3) == 0):
        for chunk in chunker(note_array, 3):
          ly_string = rf"\tuplet 3/2 {{{' '.join(chunk)}}} "
          note_text.append(ly_string)
      else:
        note_text.append(' '.join(note_array))


    note_text = rule_file.post_rule(note_text)

    for line in note_text:
      file.write(line)
      file.write("\n")

    file.close()   
  
  

def convert_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

if __name__ == "__main__":
    main()
