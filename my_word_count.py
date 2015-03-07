import glob
import re
import collections
import sys
import os

"""takes in a text file or set of text files from a directory
 and outputs the number of occurrences for each word"""

def error_message():
    # message if format of arguments not correct
    print "python my_word_count.py [input path] [output file]"
    print "eg: python ./wc_input ./wc_output/wc_result.txt"

def count(in_path):
    # read each file and parse line by line, collect counts
    word_count = {}
    for name in glob.glob(in_path+"/*.txt"):
        try:
            f = open(name, 'r')
        except IOError:
            sys.stderr.write("ERROR: Cannot read input file %s.\n" % name)
            sys.exit(1)
        line = f.readline()
        while line:
            words = re.findall(r"[\w']+", line)
            for word in words:
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            line = f.readline()
        f.close()
    return word_count

def print_result(word_count, out_file):
    # output result to destination file
    # create folder if not exist
    if not os.path.exists(os.path.dirname(out_file)):
        os.makedirs(os.path.dirname(out_file))
    f = open(out_file, 'w')
    for word in sorted(word_count):
        f.write("{0:20}{1}".format(word, word_count[word])+"\n")
    f.close()

if __name__ == "__main__":
    # arguments check and read
    if len(sys.argv) != 3:  # Expect exactly two arguments: the training data file
        error_message()
        sys.exit(2)
    in_path = sys.argv[1]
    out_file = sys.argv[2]
    # count words
    word_count = count(in_path)
    # output result
    print_result(word_count, out_file)



