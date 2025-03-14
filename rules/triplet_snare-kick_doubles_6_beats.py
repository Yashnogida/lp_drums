
time_signature = "2/4"

note_sym = {
  0 : "c8  ",
  1 : "c8->",
  2 : "f,8 ",
}

notes_per_measure = 6

  
def pre_rule(note_array, arr_length):   
  
  for note in range(arr_length):  

    na_n2 = note_array[-2 + note]
    na_n1 = note_array[-1 + note]
    na_0 = note_array[note]

  # Checks that a note occurs a maximum of twice consecutively
    if (na_n1 == na_0 == 0):
        return True
      
  # Checks that a note occurs a maximum of twice consecutively
    if (na_n1 == na_0 == 1):
        return True

  # Checks that a note occurs a maximum of twice consecutively
    if (na_n2 == na_n1 == na_0 == 2):
        return True

  # Checks that a note occurs a maximum of twice consecutively
    if (((na_n2 == 0) or ((na_n2 == 1))) and ((na_n1 == 0) or ((na_n1 == 1))) and (na_0 != 2)):
        return True

  return False


def post_rule(note_text):
  return note_text
