"""
Doubles/Singles patterns for snare and kick.
Meant to be played with left hand only 
while the right hand plays hihatt patterns.
"""

import re
import itertools

# For List of note symbols:
# https://lilypond.org/doc/v2.24/Documentation/notation/percussion-notes

time_signature = "1/4"

note_sym = {
  0 : 'sn16^"L"',
  1 : "bd16",
  # 2 : "r16",
}


notes_per_measure = 6

def generate():
  
  note_array = []
  note_data = []
  
  for i in range (pow(len(note_sym), notes_per_measure)):
  
    note_array = convert_base(i, len(note_sym))
  
    while(len(note_array) < notes_per_measure):
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
    if (na_n2 == na_n1 == na_0 == 'sn16^"L"'):
        return False
    
    # No more than two kicks next to eachother 
    if (na_n2 == na_n1 == na_0 == "bd16"):
        return False

    # # No more than two rests next to eachother 
    # if (na_n2 == na_n1 == na_0 == "r16"):
    #     return False

  return True


def format(note_data):
  
  note_data_formatted = []
  max_str_len = max(len(value) for value in note_sym.values())
  
  for note_array in note_data:
    tuple_string = ""
    note_array_formatted = [x + " " * (max_str_len - len(x)) for x in note_array]
    for chunk in chunker(note_array_formatted, 3):
      tuple_string += rf"\tuplet 3/2 {{{' '.join(chunk)}}} "
    note_data_formatted.append(f"{tuple_string}\n")
  
  return note_data_formatted


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def convert_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

