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


    

def main():

  
  root = Tk()
  root.title('Rudiment Generator')
  root.geometry("800x875")
  root.configure(background='White')
  
  # Set up the Frames
  score_window = Frame(root, bg="White", highlightbackground="black", highlightthickness=1)
  score_window.configure(height=707, width=500)
  score_window.grid_propagate(0)  # Fix it to support A5 and Letter Paper Size
  score_window.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
  
  control_window = Frame(root, bg="grey", highlightbackground="black", highlightthickness=1) 
  control_window.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

  control_subwindows = []
  score_pngs = []
  
  for i in range(6):
    
    control_subwindows.append(Frame(control_window, bg="red", highlightbackground="black", highlightthickness=1))
    control_subwindows[i].grid(row=i, column=0, sticky="nsew", padx=5, pady=45)

    button_generate = Button(control_subwindows[i], text="Generate", command=click_generate_rudiment)
    button_generate["highlightthickness"] = 0
    button_generate.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
  
    button_edit_rudiment = Button(control_subwindows[i], text="Edit Rudiment", command=click_edit_rudiment)
    button_edit_rudiment["highlightthickness"] = 0
    button_edit_rudiment.grid( row=1, column=0, padx=1, pady=1, sticky="nsew")

    png_filepath = create_png( get_random_rudiment(), f"test_{i}")
    score_pngs.append( ImageTk.PhotoImage( Image.open(png_filepath) ))
    panel = Label(score_window, image = score_pngs[i], bd=0)
    panel.grid(row=i, column=0, padx=10, pady=20, sticky="nsew")
  
  root.mainloop()
  
def click_generate_rudiment():
  print("Generating Rudiment...")
  
 
def click_edit_rudiment():
  rudiment_editor = Tk()
  rudiment_editor.mainloop()
  
  print("Editing Rudiment...")
  

def create_png(pattern, png_filename):
  
  working_folder = "temp"

  with open("ly/staff.ly", "w") as file:
    rulefile_write_rhythymic_staff(file, "2/4", pattern)
  
  subprocess.run(f"lilypond -o {working_folder}/{png_filename} -dpreview -dno-print-pages ly/main.ly")
  os.remove(f"{working_folder}/{png_filename}.preview.pdf")
  
  return f"{working_folder}/{png_filename}.preview.png"
  

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