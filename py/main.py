import sys
import string


note_sym = {
  0 : "c8  ",
  1 : "c8->",
  2 : "f,8 ",
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
    file.write(f'instrument = "{title}"\n')

  note_array = []

  f = open("ly/notes.ly", "w")

  for i in range (pow(len(note_sym), notes_per_measure)):
    
    note_array = convert_base(i, len(note_sym))
    
    while(len(note_array) < notes_per_measure):
        note_array.insert(0, 0)
    
    if (rule(note_array, notes_per_measure)):
        continue

    note_array = [note_sym[x] for x in note_array]

    
    # Deal with Triplets
    if ((notes_per_measure % 3) == 0):
        for chunk in chunker(note_array, 3):
          ly_string = rf"\tuplet 3/2 {{{' '.join(chunk)}}} "
          f.write(ly_string)
    else:
      f.write(' '.join(note_array))
    
    f.write('\n')
    
  f.close()


def rule(note_array, arr_length):

  for note in range(arr_length):

    na_n2 = note_array[-2 + note]
    na_n1 = note_array[-1 + note]
    na_0 = note_array[note]

  # Checks that a note occurs a maximum of twice consecutively
    if (na_n1 == na_0 == 0):
        return True
      
  # Checks that a note occurs a maximum of twice consecutively
    if (na_n1 == na_0 == 1):
        return True

  # Checks that a note occurs a maximum of twice consecutively
    if (na_n2 == na_n1 == na_0 == 2):
        return True

  # Checks that a note occurs a maximum of twice consecutively
    if (((na_n2 == 0) or ((na_n2 == 1))) and ((na_n1 == 0) or ((na_n1 == 1))) and (na_0 != 2)):
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


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

if __name__ == "__main__":
    main()
