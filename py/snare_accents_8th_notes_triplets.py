note_array = []

note_sym = {
  0 : "c  ",  # snare
  1 : "c->",  # snare accents
}

num_notes = 6

def main():
  
  f = open("temp", "w")
    
  for i in range (pow(2, num_notes)):
    
    note_array = convert_base(i, 2)
    
    while(len(note_array) < num_notes):
        note_array.insert(0, 0)
    
    note_array = [note_sym[x] for x in note_array]
    
    f.write(' '.join(note_array))
    f.write('\n')
    

  f.close()


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