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

COLOR_CARMINE = "#931f1d";
COLOR_CHAMOISEE = "#937b63";
COLOR_MOSS = "#8a9b68";
COLOR_LAPIS = "#175676";
COLOR_WHITE = "#ffffff";
  
NUMBER_WIDGETS = 6

root = Tk()

score_window = Frame(root, bg=COLOR_WHITE, highlightbackground=COLOR_WHITE, highlightthickness=1)
control_window = Frame(root, bg=COLOR_WHITE, highlightbackground=COLOR_WHITE, highlightthickness=1) 

control_subwindows = []
score_objects = []
png_objects = []
  

def main():

  gui_init()
  root.mainloop()

def gui_init():
  
  root.resizable(False, False)
  root.title('Rudiment Generator')
  root.geometry("620x875")
  root.configure(background=COLOR_CHAMOISEE)
  
  score_window.configure(height=707, width=500)
  score_window.grid_propagate(0)  # Fix it to support A5 Paper Size
  score_window.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
  
  control_window.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
  
  for i in range(NUMBER_WIDGETS):
    
    control_subwindows.append(Frame(control_window, bg="red", highlightbackground=COLOR_WHITE, highlightthickness=1))
    control_subwindows[i].grid(row=i, column=0, sticky="nsew", padx=5, pady=45)

    button_generate = Button(control_subwindows[i], text="Generate", command=click_generate_rudiment)
    button_generate["highlightthickness"] = 0
    button_generate.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
  
    png_objects.append( ImageTk.PhotoImage( Image.open("temp/default.png") ) )
    score_objects.append(Label(score_window, image = png_objects[i], bd=0))
    score_objects[i].place(in_=score_window, anchor = CENTER, relx = .5, rely = (i/NUMBER_WIDGETS)+0.075)

    score_objects[i].bind("<Button-1>", func=mouse_click)
    

def mouse_click(arg):
  print(arg)
  Frame(control_window, bg="red", highlightbackground=COLOR_WHITE, highlightthickness=1)
  score_objects[0]["highlightthickness"] = 1
  score_objects[0]["highlightbackground"] = COLOR_MOSS
  score_objects[0].place(in_=score_window, anchor = CENTER, relx = .5, rely = (0/NUMBER_WIDGETS)+0.075)
  
def click_generate_rudiment():
  png_filepath = create_png(get_random_rudiment(), "banana")
  png_objects[0] = ImageTk.PhotoImage( Image.open(f"{png_filepath}") )
  score_objects[0] = Label(score_window, image = png_objects[0], bd=0)
  score_objects[0].place(in_=score_window, anchor = CENTER, relx = .5, rely = (0/NUMBER_WIDGETS)+0.075)
  
  

def create_png(pattern, png_filename):
  
  working_folder = "temp"

  with open("ly/staff.ly", "w") as file:
    rulefile_write_rhythymic_staff(file, "2/4", pattern)
  
  subprocess.run(f"lilypond -o {working_folder}/{png_filename} -dpreview -dno-print-pages ly/main.ly")
  os.remove(f"{working_folder}/{png_filename}.preview.pdf")
  crop_png(f"{working_folder}/{png_filename}.preview.png")
  
  return f"{working_folder}/{png_filename}.preview.png"
  

# Removes dead whitespace from the top and bottom of the PNG file
def crop_png(png_filepath):

  img = Image.open(png_filepath)
  
  img_size_width, img_size_height = img.size
  
  pixel_rows = []
  cropped_pixel_rows = []
  
  for i in range(img_size_height):
    pixel_rows.append( [img.getpixel((x, i)) for x in range(img_size_width)] )
    pixel_count = 0
    for j in range(img_size_width):
      pixel_count += 1 if pixel_rows[i][j] == (255, 255, 255) else 0
    if not (pixel_count == img_size_width):
      cropped_pixel_rows.append(pixel_rows[i])

  flat_pixels = [pixel for row in cropped_pixel_rows for pixel in row]

  new_img = Image.new(img.mode, (img_size_width, len(cropped_pixel_rows)))
  new_img.putdata(flat_pixels)
  new_img.save(png_filepath)
  
  

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
  
  print(random_stick_pattern)
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