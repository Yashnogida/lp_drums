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
    
    with open("ly/staff.ly", "w") as file:
      
      rulefile_write_title(file, title)
      
      rulefile_write_section_title(file, "Doubles")
      rulefile_write_rhythymic_staff(file, "1/4", doubles)
      
      rulefile_write_section_title(file, "Paradiddles")
      rulefile_write_rhythymic_staff(file, "2/4", paradiddles)
  
def rotate_notes(note_pattern):
    
  note_data = []
  
  for i in range(len(note_pattern)):
    rotated = note_pattern[i:] + note_pattern[:i]
    rotated_notes = [note_sym[x] for x in rotated]
    note_data.append(rotated_notes)

  return note_data


def format_notes(note_data):
  
  note_data_formatted = []
  max_str_len = max(len(value) for value in note_sym.values())
  
  for note_array in note_data:
    note_data_formatted.append([x + " " * (max_str_len - len(x)) for x in note_array])

  note_data_formatted = [(" ".join(x) + '\n') for x in note_data_formatted] 
  
  return note_data_formatted