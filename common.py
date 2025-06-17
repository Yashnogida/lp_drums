
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
