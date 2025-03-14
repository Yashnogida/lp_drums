# lp_drums

Generating Drum Permutations Sheet Music with Lilypond

This is expecting the lilypond executable to be a path variable. To create a sheet of music, create or edit a rulefile (Python file in the "rules" directory). In the rulefile, indicate the time signature, notes per measure, not symbol, and any filtering in pre_rule and post_rule functions. 

To make a PDF from the rulefile, run the main.py python script with the name of the rule like:

`python3 main.py [rulefile]`

PDF will be output in the "pdf" directory.
