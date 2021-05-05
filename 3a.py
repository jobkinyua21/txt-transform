import os
num_lines = 0
num_words = 0

with open("3_file.txt", 'r') as filein:

    read_data = filein.read().splitlines()
    w = [len(word) for line in read_data for word in line.rstrip().split(" ")]
    for line in read_data:
        # line=line.strip()
        line = line.strip(os.linesep)

        wordslist = line.split()
        num_lines = num_lines + 1
        num_words = num_words + len(wordslist)
    w_avg = sum(w) / len(w)

# load file where to save our work
with open("text_out.txt", 'w') as fileout:
    for p in read_data:
        words = p.split()
        fileout.write(' '.join(reversed(words)).upper())
        fileout.write('\n')

# with open("text_out.txt", 'r')as myfile:
#     d = myfile.read()
#     print(d)


print("Total number of lines:", num_lines)
print("Total number of words:", num_words)
print("Mean of word:", round(w_avg, 3))
