
import random

time_signature = "4/4"

notes_per_measure = 16

note_sym = {
  0 : "c16",
  1 : "c16->"
}

def pre_rule(note_array, arr_length):   
  return False

def post_rule(note_text):
  
  # Pick 20 ramdom ones
  new_note_text = []

  for i in range(36):
    new_note_text.append(random.choice(note_text))
  
  return new_note_text
