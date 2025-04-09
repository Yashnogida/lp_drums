"""
Doubles/Singles patterns for snare and kick.
Meant to be played with left hand only 
while the right hand plays hihatt patterns.
"""

import re
import itertools

# For List of note symbols:
# https://lilypond.org/doc/v2.24/Documentation/notation/percussion-notes

time_signature = "2/4"

note_sym = {
  0 : 'sn8',
  1 : 'sn16',
  2 : "bd8",
  3 : "bd16",
}

notes_per_measure = 8

def generate():
  
  note_array = []
  note_data = []
  
  # 2 Because it's the worse case scenario (four 8th notes)
  for i in range(2, notes_per_measure + 1):
    for j in range(pow(len(note_sym), i)):

      note_array = convert_base(j, len(note_sym))

      while(len(note_array) < i):
        note_array.insert(0, 0)
    
      note_array = [note_sym[x] for x in note_array]
    
      if (rule(note_array)):
        note_data.append(note_array)
  
  
  return note_data



def rule(note_array):   

  for note in range(len(note_array)):  

    na_n2 = note_array[-2 + note]
    na_n1 = note_array[-1 + note]
    na_0 = note_array[note]
    
    # No more than two snares next to eachother
    if (("sn" in na_n2) and ("sn" in na_n1) and ("sn" in na_0)): 
        return False
    
    # No more than two kicks next to eachother
    if (("bd" in na_n2) and ("bd" in na_n1) and ("bd" in na_0)):
        return False

  return True



def format(note_data):
  
  note_data_formatted = []
  max_str_len = max(len(value) for value in note_sym.values())
  
  for note_array in note_data:
    
    if (not rhythm_mismatch(note_sym, note_array)):
      note_data_formatted.append([x + " " * (max_str_len - len(x)) for x in note_array])

  note_data_formatted = [(" ".join(x) + '\n') for x in note_data_formatted] 
  
  return note_data_formatted



def rhythm_mismatch(note_sym, note_array):

  # Divide the smallest rhythmic subdivision by each note rhythmic value
  # And check to see that they add up to the measure length (notes_per_measure)
  
  fastest_rhythym = list(note_sym.values())
  fastest_rhythym = [re.sub('[^0-9]','',x) for x in fastest_rhythym]
  fastest_rhythym = max([int(x) for x in fastest_rhythym])

  note_length = [re.sub('[^0-9]','',x) for x in note_array]  # Strip non-numeric characters
  note_length = [fastest_rhythym / int(length) for length in note_length]

  if sum(note_length) != notes_per_measure:
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

