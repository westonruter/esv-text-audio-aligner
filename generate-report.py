#!/usr/bin/env python
"""
Report generator to help provide feedback to the CMU Sphinx project.
Usage: generate-report.py osisBook chapter
"""

import json
import codecs
import sys
import re
import math

# Get args
if len(sys.argv) < 3:
    print "Needs book and chapter as args"
    sys.exit(1)
book = sys.argv[1]
chapter = int(sys.argv[2])

# Get timings
timings_file = "data/%s.%d.timings.json" % (book, chapter)
with codecs.open(timings_file, encoding='utf-8') as f:
    timings = json.loads(f.read())

# Get the original
text_file = "data/%s.%d.txt" % (book, chapter)
with codecs.open(text_file, encoding='utf-8') as f:
    original_words = map(lambda s: re.sub(r'^\W+|\W+$', '', s), f.read().strip().split())

print "Words in source text:", len(original_words)
print "Words found by aligner:", len(timings)
print "Number of <unk> words:", len(filter(lambda t: t['word'] is None, timings))

missing_original_words = list(original_words)
for timing in timings:
    if missing_original_words[0] == timing['word']:
        missing_original_words.pop(0)

print "Number of words that were left off: %d (%.1f%%)" % (len(missing_original_words), float(len(missing_original_words))/len(original_words)*100)

word_max_length = max([len(word) for word in original_words])
pad_format = "%% -%ds" % (word_max_length+1) # so meta

timings_queue = list(timings)
for timing in timings_queue:
    sys.stdout.write('%.01fs ' % (timing['end'] - timing['start']))
    word = '<unk>'
    if timing['word'] is None:
        word = '<unk>'
    else:
        word = timing['word']
    sys.stdout.write(pad_format % word)
    sys.stdout.write(' ')
    
    for i in range(0, int((timing['end'] - timing['start'])*10)+1):
        if timing['word'] is None:
            sys.stdout.write('-')
        else:
            sys.stdout.write('+')
    print

print "Words left off: ", len(missing_original_words)
