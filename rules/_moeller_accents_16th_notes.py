# For List of note symbols:
# https://lilypond.org/doc/v2.24/Documentation/notation/percussion-notes

time_signature = "4/4"

notes_per_measure = 16

note_sym = {
  0 : "sn16",
  1 : "sn16->",
}

def generate():
  
  note_array = []
  note_data = []
  
  for i in range (pow(len(note_sym), notes_per_measure)):
  
    note_array = convert_base(i, len(note_sym))
  
    while(len(note_array) < notes_per_measure):
      note_array.insert(0, 0)

    note_array = [note_sym[x] for x in note_array]
    note_data.append(note_array)
  
  return note_data


def format(note_data):
  
  note_data_formatted = []
  max_str_len = max(len(value) for value in note_sym.values())
  

  for note_array in note_data:
  
    non_moeller = False

    for note in range(len(note_array)):
      
      na_n2 = note_array[-2 + note]
      na_n1 = note_array[-1 + note]
      na_0 = note_array[note]
      
      if (("->" in na_n1) and ("->" in na_0)) or \
      ((na_n2 == "sn16") and (na_n1 == "sn16") and (na_0 == "sn16")):
        non_moeller = True
    
    if (not non_moeller):
      note_data_formatted.append([x + " " * (max_str_len - len(x)) for x in note_array])

  note_data_formatted = [(" ".join(x) + '\n') for x in note_data_formatted] 
  
  return note_data_formatted


def convert_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

