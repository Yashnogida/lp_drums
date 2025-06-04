# For List of note symbols:
# https://lilypond.org/doc/v2.24/Documentation/notation/percussion-notes

import re

time_signature = "2/4"

min_notes_per_measure = 8

note_sym = {
  0 : "sn16",
  1 : "sn32",
}

rhythyms = list(note_sym.values())
rhythyms = [re.sub('[^0-9]','',x) for x in rhythyms]
slowest_rhythym = min([int(x) for x in rhythyms])
fastest_rhythym = max([int(x) for x in rhythyms])
rhythym_scale = int(fastest_rhythym / slowest_rhythym)

def generate():
  
  note_array = []
  note_data = []
  
  for i in range(min_notes_per_measure, rhythym_scale * min_notes_per_measure + 1):
    for j in range(pow(len(note_sym), i)):
      
      note_array = convert_base(j, len(note_sym))
      
      while(len(note_array) < i):
        note_array.insert(0, 0)
      
      # with open("note_arrays.txt", "a") as f:
        # f.write(f"{i:6} {j:6} | {note_array} | {[note_sym[x] for x in note_array]}" + "\n")
      
      note_array = [note_sym[x] for x in note_array]
      
      if (rule(note_array)):
        note_data.append(note_array)
  
  return note_data


def rule(note_array):   


  for note_index in range(len(note_array)):  

    na_n2 = note_array[-2 + note_index]
    na_n1 = note_array[-1 + note_index]
    na_0 = note_array[note_index]
    
    # No more than two next to eachother
    if (("16" in na_n2) and ("16" in na_n1) and ("16" in na_0)): 
      return False
    
    # No more than two next to eachother
    if (("32" in na_n2) and ("32" in na_n1) and ("32" in na_0)): 
        return False
  
  if (rhythm_mismatch(note_array)):
    return False
  
  return True


def format(note_data):
  
  note_data_formatted = []
  max_str_len = max(len(value) for value in note_sym.values())
  
  for note_array in note_data:
    note_data_formatted.append([x + " " * (max_str_len - len(x)) for x in note_array])

  note_data_formatted = [(" ".join(x) + '\n') for x in note_data_formatted] 
  
  return note_data_formatted




#######################################
#         Utility Functions           #
#######################################


def rhythm_mismatch(note_array):

  # Divide the smallest rhythmic subdivision by each note rhythmic value
  # And check to see that they add up to the measure length (notes_per_measure)

  note_length = [re.sub('[^0-9]','',x) for x in note_array]  # Strip non-numeric characters
  note_length = [fastest_rhythym / int(length) for length in note_length]


  if int(sum(note_length)) != int(rhythym_scale * min_notes_per_measure):
    return True
  
  # with open("note_arrays.txt", "a") as f:
    # f.write(f"{note_array}"+ "\n")
  
  return False



def convert_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

