
###
###  Note Generation 
### 

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

###
### Rulefile Writing
### 

def rulefile_write_title(file, title):
      file.write("\header {\n")
      file.write("  " + f'title = \markup {{{title}}}\n')
      file.write("  " + f'instrument = \markup {{{title}}}\n')
      file.write("  " + 'tagline = ""\n')
      file.write("}\n")
      
      
def rulefile_write_drumstaff(file, time_signature, formatted_note_data):
    file.write("\n")
    file.write("\\new DrumStaff <<\n")
    file.write("  \\drummode {\n")
    
    file.write("\n")
    file.write(f"     \\time {time_signature}\n")
    file.write("\n")
    
    for entry in formatted_note_data:
        file.write("     " + entry.strip() + "\n")
    file.write("\n")
    
    file.write("  }\n")
    file.write(">>\n")  # Close DrumStaff
    
def rulefile_write_rhythymic_staff(file, time_signature, formatted_note_data):

    file.write("\n")
    file.write("\markup \\vspace #1\n")
    file.write("\n")

    file.write("\\new RhythmicStaff {\n")

    file.write("\n")
    file.write(f"     \\time {time_signature}\n")
    file.write("\n")
    
    for entry in formatted_note_data:
        file.write("     " + entry.strip() + "\n")
    file.write("\n")
    
    file.write("}\n")  # Close RhythmicStaff

def rulefile_write_section_title(file, title):
    file.write("\n")
    file.write("\\markup \\column {\n")
    file.write("  \\vspace #1\n")
    # file.write("  \\fill-line { \\bold \"" + title + "\" }\n")  # For Centered Section Title
    file.write(f'  \\bold "{title}"\n')                          # For Left-Aligned Section Title
    file.write("  \\vspace #0.5\n")
    file.write("}\n")
    file.write("\n")