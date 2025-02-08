note_array = []

note_sym = {
  0 : "c16  ",  
  1 : "c16->  ",  
}

num_notes = 8

def main():
  
  f = open("ly/notes.ly", "w")
    
  for i in range (pow(len(note_sym), num_notes)):
    
    note_array = convert_base(i, len(note_sym))
    
    while(len(note_array) < num_notes):
        note_array.insert(0, 0)
    
    if (rule(note_array, num_notes)):
        continue

    note_array = [note_sym[x] for x in note_array]
    
    f.write(' '.join(note_array))
    f.write('\n')
    

  f.close()



def rule(note_array, arr_length):

  return False  # Uncomment for No Rules

  for note in range(arr_length):
      
      # Checks that a note occurs a maximum of twice consecutively
      if (note_array[-2 + note] == note_array[-1 + note] == note_array[0 + note] == 1):
          return True


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