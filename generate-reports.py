#!/usr/bin/env python
"""
Report generator to help provide feedback to the CMU Sphinx project.
Usage: generate-reports.py [osisBook chapter[...]]...
"""

import json
import codecs
import sys
import re
import math
import bookinfo
import os

# Get args
books = bookinfo.get_book_subset(sys.argv[1:])

for bookinfo in books:
    for chapter in bookinfo.chapters:
        # Get timings
        timings_file = "data/%s.%d.timings.json" % (bookinfo.osis, chapter)
        if not os.path.exists(timings_file):
            continue
        with codecs.open(timings_file, encoding='utf-8') as f:
            timings = json.loads(f.read()).get('words')
        
        # Get the original
        text_file = "data/%s.%d.txt" % (bookinfo.osis, chapter)
        if not os.path.exists(text_file):
            continue
        with codecs.open(text_file, encoding='utf-8') as f:
            original_words = map(lambda s: re.sub(r'^\W+|\W+$', '', s), f.read().strip().split())
            assert(len(original_words) != 0)
        
        print '%s.%d' % (bookinfo.osis, chapter)
        
        freport = codecs.open('reports/%s.%d' % (bookinfo.osis, chapter), mode='w', encoding='utf-8')
        
        freport.write("Any data appearing in the ESV text column herein is copyrighted:\n")
        freport.write("The Holy Bible, English Standard Version copyright (c)2001 by Crossway Bibles,\n")
        freport.write("a publishing ministry of Good News Publishers. All rights reserved.\n")
        freport.write("<http://www.crossway.org/rights-permissions/esv/>\n\n")
        
        freport.write("Words in source text: %d\n" % len(original_words))
        freport.write("Words found by aligner: %d\n" % len(timings))
        freport.write("Number of <unk> words: %d\n" % len(filter(lambda t: t['word'] is None, timings)))
        
        missing_original_words = list(original_words)
        for timing in timings:
            if len(missing_original_words) == 0:
                assert(timing['word'] is None)
            elif missing_original_words[0] == timing['word']:
                missing_original_words.pop(0)
        
        if len(missing_original_words):
            freport.write("Number of words that were left off: %d (%.1f%%)\n" % (
                len(missing_original_words),
                float(len(missing_original_words))/len(original_words)*100
            ))
        else:
            freport.write("All words in the text are reported to be discovered in audio\n")
        word_max_length = max([len(word) for word in original_words])
        pad_format = "%% -%ds" % (word_max_length+1) # so meta
        
        timings_queue = list(timings)
        for timing in timings_queue:
            freport.write('% 2.01fs ' % (timing['end'] - timing['start']))
            word = '<unk>'
            if timing['word'] is None:
                word = '<unk>'
            else:
                word = timing['word']
            freport.write(pad_format % word)
            freport.write(' ')
            
            for i in range(0, int((timing['end'] - timing['start'])*10)+1):
                if timing['word'] is None:
                    freport.write('-')
                else:
                    freport.write('+')
            freport.write("\n")
        
        freport.write("Words left off: %d\n" % len(missing_original_words))
        
        freport.close()
