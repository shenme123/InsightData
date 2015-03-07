import glob
import re
import collections
import sys
import os
import heapq

def error_message():
    # message if format of arguments not correct
    print "python my_word_count.py [input path] [output file]"
    print "eg: python my_running_median.py ./wc_input ./wc_output/med_result.txt"

def median(in_path, out_file):
    # read each file and find running median
    min_heap = []
    max_heap = []
    out = open(out_file, 'w')
    for name in sorted(glob.glob(in_path+"/*.txt")):
        print name
        try:
            f = open(name, 'r')
        except IOError:
            sys.stderr.write("ERROR: Cannot read input file %s.\n" % name)
            sys.exit(1)
        line = f.readline()
        while line:
            words = re.findall(r"[\w']+", line)
            length = len(words)
            #################################
            # at beginning, add first length to min_heap and output it as median.
            if len(min_heap)==0 and len(max_heap)==0:
                heapq.heappush(min_heap, length)
                out.write("%.1f\n" % length)
            # from the 2nd length
            else:
                # if new length is greater or equal to the root of min_heap, add -length to max_heap
                # if not, add to min_heap
                if length <= min_heap[0]:
                    heapq.heappush(max_heap, -length)
                else:
                    heapq.heappush(min_heap, length)
                # balance two heaps till the max difference of length is 1, and output current median
                diff = len(min_heap) - len(max_heap)
                if diff == 0:
                    out.write("%.1f\n" % ((min_heap[0]-max_heap[0])/2.0))
                elif diff == 1:
                    out.write("%.1f\n" % min_heap[0])
                elif diff == -1:
                    out.write("%.1f\n" % -max_heap[0])
                elif diff == 2:
                    heapq.heappush(max_heap, -heapq.heappop(min_heap))
                    out.write("%.1f\n" % ((min_heap[0]-max_heap[0])/2.0))
                elif diff == -2:
                    heapq.heappush(min_heap, -heapq.heappop(max_heap))
                    out.write("%.1f\n" % ((min_heap[0]-max_heap[0])/2.0))
            line = f.readline()
        f.close()

if __name__ == "__main__":
    # arguments check and read
    if len(sys.argv) != 3:  # Expect exactly two arguments: the training data file
        error_message()
        sys.exit(2)
    in_path = sys.argv[1]
    out_file = sys.argv[2]
    # accepting input and find running median
    median(in_path, out_file)