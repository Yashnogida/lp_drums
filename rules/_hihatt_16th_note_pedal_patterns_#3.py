
import re
import itertools

# For List of note symbols:
# https://lilypond.org/doc/v2.24/Documentation/notation/percussion-notes

time_signature = "2/4"

note_sym = {
  0 : "hho8 ",  # Open Hihatt 8
  1 : "hho16",  # Open Hihatt 16
  2 : "hhc16",  # Closed Hihatt
  3 : "hhp16",  # Hihatt Pedal
}


notes_per_measure = 8


def generate():
  
  note_array = []
  note_data = []

  # 4 Because it's the worse case scenario (four 8th notes)
  for i in range(4, notes_per_measure + 1):
    for j in range(pow(len(note_sym), i)):

      note_array = convert_base(j, len(note_sym))

      while(len(note_array) < i):
        note_array.insert(0, 0)
    
      if (pre_rule(note_array)):
        note_array = [note_sym[x] for x in note_array]
        note_data.append(note_array)
  
  return note_data




def pre_rule(note_array):   

  # Divide 16 (the smallest rhythmic subdivision) by each note rhythmic value
  # And check to see that they add up to the measure length (notes_per_measure)
  note_array = [note_sym[x] for x in note_array]
  note_length = [re.sub('[^0-9]','',x) for x in note_array]  # Strip non-numeric characters
  note_length = [16 / int(length) for length in note_length]
  
  if sum(note_length) != 8:
    return False

  for note in range(len(note_array)):  

    na_n2 = note_array[-2 + note]
    na_n1 = note_array[-1 + note]
    na_0 = note_array[note]

    # No more than two Open8/Open16 next to eachother
    if (((na_n2 == "hho8 ") or (na_n2 == "hho16")) and
        ((na_n1 == "hho8 ") or (na_n1 == "hho16")) and
        ((na_n0 == "hho8 ") or (na_n0 == "hho16")))
        return False
     
    # No more than two Closed next to eachother 
    if (na_n2 == na_n1 == na_0 == "hhc16"):
        return False
    
    # No more than two Pedals next to eachother 
    if (na_n2 == na_n1 == na_0 == "hhp16"):
        return False
    
    # Two Closed must be followed by an Open8 or an Open16
    if (((na_n2 == 2) and (na_n1 == 2) and (na_0 != 0)) or ((na_n2 == 2) and (na_n1 == 2) and (na_0 != 1))):  
        return False

    # A Pedal followed by a Closed must be followed by an Open 
    if ((na_n2 == 2) and (na_n1 == 1) and (na_0 != 0)):  
        return False

    # Closed must NOT be followed by a Pedal
    if ((na_n1 == 1) and (na_0 == 2)):  
        return False

    # Open must NOT be followed by a Closed
    if ((na_n1 == 0) and (na_0 == 1)):
        return False

  #   # print(f"{note_array} : {note_length} : {sum(note_length)}")

  return True





def convert_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

