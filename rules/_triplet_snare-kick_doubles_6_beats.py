
time_signature = "2/4"

note_sym = {
  0 : "sn8  ",
  1 : "sn8->",
  2 : "bd ",
}

notes_per_measure = 6
  
def generate():
  
  note_array = []
  note_data = []
  
  for i in range (pow(len(note_sym), notes_per_measure)):
  
    note_array = convert_base(i, len(note_sym))
  
    while(len(note_array) < notes_per_measure):
      note_array.insert(0, 0)

    if (pre_rule(note_array)):
      note_array = [note_sym[x] for x in note_array]
      note_data.append(note_array)
  
  return note_data



def pre_rule(note_array):   
  print(f"{note_array} : {len(note_array)}")
  for note in range(len(note_array)):  

    na_n2 = note_array[-2 + note]
    na_n1 = note_array[-1 + note]
    na_0 = note_array[note]

  # Checks that a note occurs a maximum of twice consecutively
    if (na_n1 == na_0 == 0):
        return False
      
  # Checks that a note occurs a maximum of twice consecutively
    if (na_n1 == na_0 == 1):
        return False

  # Checks that a note occurs a maximum of twice consecutively
    if (na_n2 == na_n1 == na_0 == 2):
        return False

  # Checks that a note occurs a maximum of twice consecutively
    if (((na_n2 == 0) or ((na_n2 == 1))) and ((na_n1 == 0) or ((na_n1 == 1))) and (na_0 != 2)):
        return False

  return True


def convert_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]