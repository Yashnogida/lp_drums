# lp_drums
Generating Drum Permutations Sheet Music with Lilypond

This is expecting the lilypond executable to be a path variable. To create a sheet of music, edit the a.py file to create the note symbols (drums to permutate) and rules for permutations. 

Run "build.bat (filename)" where "filename" is the name of the sheet music pdf that will be put in the "pdf" directory. This script will create temp.ly files and run lilypond on the a.ly file (which includes this file), which will create the sheet music.

