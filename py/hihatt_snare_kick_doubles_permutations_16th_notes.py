note_array = []

note_sym = {
  0 : "r",  # rest
  1 : "d",  # hihatt
  2 : "c",  # snare
  3 : "f"  # kick
}

num_notes = 4

def main():
  
  f = open("temp", "w")
    
  for i in range (pow(4, num_notes)):
    
    note_array = convert_base(i, 4)
    
    while(len(note_array) < num_notes):
        note_array.insert(0, 0)
    
    if (check_rule(note_array, num_notes)):
        continue
    
    note_array = [note_sym[x] for x in note_array]
    
    f.write(' '.join(note_array))
    f.write('\n')
    

  f.close()


def check_rule(note_array, arr_length):
    for note in range(arr_length):
        
        # Checks that a note occurs a maximum of twice consecutively
        if (note_array[-2 + note] == note_array[-1 + note] == note_array[0 + note]):
            return True

        # Checks that there are no consecutive rests 
        if (note_array[-1 + note] == note_array[0 + note] == 0):
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