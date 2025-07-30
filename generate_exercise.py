# For List of note symbols:
# https://lilypond.org/doc/v2.24/Documentation/notation/percussion-notes

from common import *
import subprocess
import random
import time
import os
import sys

from tkinter import *
from PIL import ImageTk, Image
import os


    
working_folder = "temp"

def main():

  create_png( get_random_rudiment(), "test_0")
  create_png( get_random_rudiment(), "test_1")
  create_png( get_random_rudiment(), "test_2")
  create_png( get_random_rudiment(), "test_3")
  
  root = Tk()
  root.configure(background='White')
  
  control_window = Frame(root, bg="grey", highlightbackground="black", highlightthickness=1) 
  control_window.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

  score_window = Frame(root, bg="ivory3")
  score_window.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

  variable = StringVar(control_window)
  variable.set("Select Rudiment") # default value
  
  rudiment_option = OptionMenu(control_window, variable, "one", "two", "three")
  rudiment_option["highlightthickness"] = 0
  rudiment_option.grid(padx=10, pady=10, row=0, column=0, sticky="nsew")

  my_button = Button(control_window, text="Generate", command=on_button_click)
  my_button.grid(row=1, column=0, padx=10, pady=0, sticky="nsew")


  img_0 = ImageTk.PhotoImage( Image.open(f"{working_folder}/test_0.preview.png"))
  img_1 = ImageTk.PhotoImage( Image.open(f"{working_folder}/test_1.preview.png"))
  img_2 = ImageTk.PhotoImage( Image.open(f"{working_folder}/test_2.preview.png"))
  panel_0 = Label(score_window, image = img_0, bd=0)
  panel_1 = Label(score_window, image = img_1, bd=0)
  panel_2 = Label(score_window, image = img_2, bd=0)
  panel_0.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
  panel_1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
  panel_2.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
  
  root.mainloop()
  
def on_button_click():

   return

def create_png(pattern, png_filename):
  
  with open("ly/staff.ly", "w") as file:
    rulefile_write_rhythymic_staff(file, "2/4", pattern)
  
  subprocess.run(f"lilypond -o {working_folder}/{png_filename} -dpreview -dno-print-pages ly/main.ly")
  os.remove(f"{working_folder}/{png_filename}.preview.pdf")
  

def get_random_rudiment():

  note_sym_sticking = {
    0 : 'c16^"R"',
    1 : 'c16^"L"',
    2 : 'c16->^"R"',
    3 : 'c16->^"L"',
  }
  
  stick_patterns = generate_notes(note_sym_sticking, 8)
  stick_patterns = format_notes(note_sym_sticking, stick_patterns)
  random_index = round( random.random() * len(stick_patterns) )
  random_stick_pattern = [ stick_patterns[random_index] ]
  
  return random_stick_pattern


def rotate_notes(note_sym, note_pattern):
    
  note_data = []
  
  for i in range(len(note_pattern)):
    rotated = note_pattern[i:] + note_pattern[:i]
    rotated_notes = [note_sym[x] for x in rotated]
    note_data.append(rotated_notes)

  return note_data


def generate_notes(note_sym, notes_per_measure):
  
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

    na_n3 = note_array[-3 + note]
    na_n2 = note_array[-2 + note]
    na_n1 = note_array[-1 + note]
    na_0 = note_array[note]
    
    # No more than two left-hands next to eachother
    if (("L" in na_n2) and ("L" in na_n1) and ("L" in na_0)):
        return False
    
    # No more than two right-hands next to eachother
    if (("R" in na_n2) and ("R" in na_n1) and ("R" in na_0)):
        return False
      
    # No more than two right-hand accents next to eachother
    if (('->^"R"' in na_n2) and ('->^"R"' in na_n1) and ('->^"R"' in na_0)):
        return False
    
    # No more than two left-hand accents next to eachother
    if (('->^"L"' in na_n2) and ('->^"L"' in na_n1) and ('->^"L"' in na_0)):
        return False
      
    # No more than three consecutive accents (left or right ) next to eachother
    if (('->' in na_n3) and ('->' in na_n2) and ('->' in na_n1) and ('->' in na_0)):
        return False


  return True


def format_notes(note_sym, note_data):
  
  note_data_formatted = []
  max_str_len = max(len(value) for value in note_sym.values())
  
  for note_array in note_data:
    note_data_formatted.append([x + " " * (max_str_len - len(x)) for x in note_array])

  note_data_formatted = [(" ".join(x) + '\n') for x in note_data_formatted] 
  
  return note_data_formatted



def format_triplets(note_data):
  
  note_data_triplets = []
  
  note_data = [data.strip() for data in note_data]
  
  for data in note_data:
    for chunk in chunker(data.split(), 3):
      note_data_triplets.append(rf"\tuplet 3/4 {{{' '.join(chunk)}}} ")
  
  return note_data_triplets


if __name__ == "__main__":
    main()