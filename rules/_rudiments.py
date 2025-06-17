# For List of note symbols:
# https://lilypond.org/doc/v2.24/Documentation/notation/percussion-notes

from common import *

notes_per_measure = 8

note_sym = {
  0 : 'c16^"R"',
  1 : 'c16^"L"',
}

def create_rulefile(title):

    doubles = rotate_notes([0, 0, 1, 1])  # RLRR LRLL
    doubles = format_notes(doubles)

    paradiddles = rotate_notes([0, 1, 0, 0, 1, 0, 1, 1])  # RLRR LRLL
    paradiddles = format_notes(paradiddles)
    
    other_singles_doubles = generate_notes()
    other_singles_doubles = format_notes(other_singles_doubles)

    
    with open("ly/staff.ly", "w") as file:
      
      rulefile_write_title(file, title)
      
      rulefile_write_section_title(file, "Doubles")
      rulefile_write_rhythymic_staff(file, "1/4", doubles)
      
      rulefile_write_section_title(file, "Paradiddles")
      rulefile_write_rhythymic_staff(file, "2/4", paradiddles)
      
      rulefile_write_section_title(file, "Other Singles/Doubles")
      rulefile_write_rhythymic_staff(file, "2/4", other_singles_doubles)

  
def rotate_notes(note_pattern):
    
  note_data = []
  
  for i in range(len(note_pattern)):
    rotated = note_pattern[i:] + note_pattern[:i]
    rotated_notes = [note_sym[x] for x in rotated]
    note_data.append(rotated_notes)

  return note_data


def generate_notes():
  
  note_array = []
  note_data = []
  
  for i in range (pow(len(note_sym), notes_per_measure)):
  
    note_array = convert_base(i, len(note_sym))

    while(len(note_array) < notes_per_measure):
      note_array.insert(0, 0)

    note_array = [note_sym[x] for x in note_array]
    
    if (apply_rule(note_array)):
      note_data.append(note_array)
  
  return note_data


def apply_rule(note_array):   
  
  for note in range(len(note_array)):  

    na_n2 = note_array[-2 + note]
    na_n1 = note_array[-1 + note]
    na_0 = note_array[note]
    
    # No more than two left-hands next to eachother
    if (("L" in na_n2) and ("L" in na_n1) and ("L" in na_0)):
        return False
    
    if (("R" in na_n2) and ("R" in na_n1) and ("R" in na_0)):
        return False

  return True


def format_notes(note_data):
  
  note_data_formatted = []
  max_str_len = max(len(value) for value in note_sym.values())
  
  for note_array in note_data:
    note_data_formatted.append([x + " " * (max_str_len - len(x)) for x in note_array])

  note_data_formatted = [(" ".join(x) + '\n') for x in note_data_formatted] 
  
  return note_data_formatted