import sys
import string


note_sym = {
  0 : "c16  ",
  1 : "c16->",
  2 : "f,16 ",
}

notes_per_measure = 12

# note_sym_inv = {val: key for key, val in note_sym.items()} 

def main():
  
  
  if (len(sys.argv) < 2):  # default file name
    title = "main"          
  else:
    title = sys.argv[1]
    title = title.replace('_', ' ').title()
  
  with open("ly/title.ly", "w") as file:
    file.write(fr'title = "{title}"')

  note_array = []

  f = open("ly/notes.ly", "w")

  for i in range (pow(len(note_sym), notes_per_measure)):
    
    note_array = convert_base(i, len(note_sym))
    
    while(len(note_array) < notes_per_measure):
        note_array.insert(0, 0)
    
    if (rule(note_array, notes_per_measure)):
        continue

    note_array = [note_sym[x] for x in note_array]
    
    f.write(' '.join(note_array))
    f.write('\n')
    
  f.close()


def rule(note_array, arr_length):

  # Checks that a note occurs a maximum of twice consecutively
  for note in range(arr_length):
      if (note_array[-2 + note] == note_array[-1 + note] == note_array[0 + note] == 0):
          return True
      
  # Checks that a note occurs a maximum of twice consecutively
  for note in range(arr_length):
      if (note_array[-2 + note] == note_array[-1 + note] == note_array[0 + note] == 1):
          return True

  # Checks that a note occurs a maximum of twice consecutively
  for note in range(arr_length):
      if (note_array[-2 + note] == note_array[-1 + note] == note_array[0 + note] == 2):
          return True


  for note in range(arr_length):

  if 2 not in note_array:
    return True















  return False


def convert_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

if __name__ == "__main__":
    main()