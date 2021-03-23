# author: github.com/teo113
# desc: This script finds text in a text based input file, replaces the text, creates a new output file.

in_file = open(fr'D:\path_to_file\input.txt', 'r')
out_file = open(fr'D:\path_to_file\output.txt', 'r')

find = ('\\', 'this word', 'hello')
replace = ('/', 'that word', 'goodbye')

for line in in_file:
    for check, rep in zip(find, replace):
        line = line.replace(check, rep)
    out_file.write(line)
in_file.close()
out_file.close()

# repeat for other files
# potential to rewrite find/replace list as a loop
