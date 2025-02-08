note_array = []

def main():

  f = open("temp", "w")
    
  for i in range (pow(2, 8)):
    for j in range (8):
        note_array.append("c-> " if ((1<<j) & i) else "c   ")
        note_array[-1] = f"{note_array[-1]:<3}"
    note_array.reverse()
    f.write(' '.join(note_array))
    f.write('\n')
    note_array.clear()
    
  f.close()

if __name__ == "__main__":
    main()