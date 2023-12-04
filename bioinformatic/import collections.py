def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities


sequences, qualities =readFastq('ERR037900_1.first1000.fastq')
print(sequences[:5])

import collections
count=collections.Counter()
for seq in sequences:
    count.update(seq)
print(count)
