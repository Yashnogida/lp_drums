# For List of note symbols:
# https://lilypond.org/doc/v2.24/Documentation/notation/percussion-notes

from common import *
import subprocess
import random
import time
import os
import sys
# from pypdf import PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader


note_sym_sticking = {
  0 : 'c16^"R"',
  1 : 'c16^"L"',
}
    
note_sym_accents = {
  0 : "sn16",
  1 : "sn16->",
}
  
def main():

  practice_pdf = canvas.Canvas("practice_sheet.pdf")  

  # Get a random sticking pattern
  stick_patterns = generate_notes(note_sym_sticking, 8)
  stick_patterns = format_notes(note_sym_sticking, stick_patterns)
  random_index = round( random.random() * len(stick_patterns) )
  random_stick_pattern = [ stick_patterns[random_index] ]

  # Get a random accent pattern
  accent_patterns = generate_notes(note_sym_accents, 8)
  accent_patterns = format_notes(note_sym_accents, accent_patterns)
  random_index = round( random.random() * len(accent_patterns) )
  random_accent_pattern = [ accent_patterns[random_index] ]
  
  add_exercise_to_pdf(practice_pdf, random_stick_pattern, random_accent_pattern)
   
  practice_pdf.save()   # Save and Close the PDF file



def add_exercise_to_pdf(pdf_object, stick_pattern, accent_pattern):
  
  stick_pdf_filename = "stick"
  stick_image_path = f"{stick_pdf_filename}.preview.png"
  
  # Add Sticking Pattern to PDF
  with open("ly/staff.ly", "w") as file:
    rulefile_write_rhythymic_staff(file, "2/4", stick_pattern)
  
  subprocess.run(f"lilypond -o {stick_pdf_filename} -dpreview -dresolution=1000 ly/main.ly")
  
  img = ImageReader(stick_image_path)
  img_width, img_height = img.getSize()
  img_width_scaled = img_width * 0.1
  img_height_scaled = img_height * 0.1

  pdf_object.drawImage(stick_image_path, 50, 700, width=img_width_scaled, height=img_height_scaled, preserveAspectRatio=True, mask='auto')
  
  os.remove(stick_image_path)
  os.remove(f"{stick_pdf_filename}.pdf")
  os.remove(f"{stick_pdf_filename}.preview.pdf")

  # Add Accent Pattern to PDF
  accent_pdf_filename = "accent"
  accent_image_path = f"{accent_pdf_filename}.preview.png"

  with open("ly/staff.ly", "w") as file:
    rulefile_write_drumstaff(file, "2/4", accent_pattern)
  
  subprocess.run(f"lilypond -o {accent_pdf_filename} -dpreview -dresolution=1000 ly/main.ly")
  
  # Reload the new image after regenerating it
  img = ImageReader(accent_image_path)
  img_width, img_height = img.getSize()
  img_width_scaled = img_width * 0.1
  img_height_scaled = img_height * 0.1

  pdf_object.drawImage(accent_image_path, 300, 700, width=img_width_scaled, height=img_height_scaled, preserveAspectRatio=True, mask='auto')
  
  os.remove(accent_image_path)
  os.remove(f"{accent_pdf_filename}.pdf")
  os.remove(f"{accent_pdf_filename}.preview.pdf")
  
  
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

    na_n2 = note_array[-2 + note]
    na_n1 = note_array[-1 + note]
    na_0 = note_array[note]
    
    # No more than two left-hands next to eachother
    if (("L" in na_n2) and ("L" in na_n1) and ("L" in na_0)):
        return False
    
    if (("R" in na_n2) and ("R" in na_n1) and ("R" in na_0)):
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