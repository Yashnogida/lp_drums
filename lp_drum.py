note_array = []

def main():
  for i in range (pow(2, 8)):
    for j in range (8):
        note_array.append("f " if ((1<<j) & i) else "c ")
        note_array[-1] = f"{note_array[-1]:<3}"
    note_array.reverse()
    for j in range (8):
        print(note_array[j], end=" ")
    print()
    

if __name__ == "__main__":
    main()