#!/usr/bin/env python
"""
ESV Text/Audio Aligner using CMU Sphinx
Pulls down the ESV text and audio from the ESV API, then generates
chapyer-by-chapter {book}.{chapter}.timings.json files in the data/ directory.
Previously-aligned chapters are skipped unless forced.

Author: Weston Ruter <http://weston.ruter.net/> @westonruter
Project: https://github.com/westonruter/esv-audio-timings
Dependencies: Python 2.7, java, ant, sox, svn

The ESV Text and MP3 data downloaded by this script is subject to copyright:
    The Holy Bible, English Standard Version copyright (c)2001 by Crossway Bibles, a
    publishing ministry of Good News Publishers. Used by permission. All rights
    reserved. <http://www.crossway.org/rights-permissions/esv/>

ESV API usage terms available from http://www.esvapi.org/
    You can access the ESV text using the key "IP" (without the quotes). This
    key limits you to 5,000 queries per day from a single IP address. You are
    bound by the below conditions of use, including the non-commercial
    aspects. <http://www.esvapi.org/#conditions>

USAGE:
$ python align.py [-f|--force] [osisBook] [chapter, [chapter]...] [osisBook] [chapter, [chapter]...] ...

See README for examples and further information.

Dual licensed under the MIT or GPL Version 2 licenses.
MIT License: http://creativecommons.org/licenses/MIT/
GPL 2.0 license: http://creativecommons.org/licenses/GPL/2.0/
"""

import subprocess
import os
from os import path
import urllib
import codecs
import sys
import shutil
import json
import re
from time import time as clock
import bookinfo

def align(argv):
    """ Main function for this module (see its docstring for usage) """
    
    init_start_time = clock()
    
    __dir__ = path.realpath(path.dirname(__file__))
    sphinx_long_audio_aligner_repo_url = "http://cmusphinx.svn.sourceforge.net/svnroot/cmusphinx/branches/long-audio-aligner/Aligner"
    long_audio_aligner_path = __dir__ + '/long-audio-aligner'
    data_path = __dir__ + '/data'
    is_force = ('--force' in sys.argv or '-f' in sys.argv)
    
    books = bookinfo.get_book_subset(argv)
    
    # svn co http://cmusphinx.svn.sourceforge.net/svnroot/cmusphinx/branches/long-audio-aligner/Aligner aligner
    if not path.exists(long_audio_aligner_path):
        print "Fetching long-audio-aligner from Sourceforge..."
        subprocess.call(['svn', 'co', sphinx_long_audio_aligner_repo_url, long_audio_aligner_path])
    
    # Remove the initial batchFile since we don't want to process it anyway
    f = open(long_audio_aligner_path + '/resource/batchFile.txt', 'w')
    f.write('')
    f.close()
    
    # Build the Java project
    cwd = os.path.realpath(os.curdir)
    os.chdir(long_audio_aligner_path)
    print "Running ant...",
    retcode = subprocess.call(['ant'])
    if retcode != 0:
        print "fail (have you ant?)"
        sys.exit(1)
    else:
        print "done"
    os.chdir(cwd)
    
    # Create the data directory which is where we put all the ESV data: audio, text, HTML, alignments
    if not path.exists(data_path):
        print "Making data dir"
        os.mkdir(data_path)
    
    for book in books:
        print "########################"
        print "%s (%s)" % (book.name, book.osis)
        print "########################"
        
        book_start_time = clock()
        
        for chapter in book.chapters:
            chapter_start_time = clock()
            
            mp3_file = data_path + '/%s.%d.mp3' % (book.osis, chapter)
            print "%s %d" % (book.osis, chapter)
            
            # Fetch MP3
            if not os.path.exists(mp3_file):
                mp3_url = 'http://www.esvapi.org/v2/rest/passageQuery?key=IP&output-format=mp3&passage={book}+{chapter}'.format(
                    book=book.name,
                    chapter=chapter
                )
                print "Downloading MP3...",
                fi = urllib.urlopen(mp3_url)
                if not fi.getcode() or fi.getcode() != 200:
                    print "Failed, getcode =", fi.getcode()
                    sys.exit(1)
                else:
                    print "done"
                fo = open(mp3_file, 'w')
                fo.write(fi.read())
                fi.close()
                fo.close()
            else:
                print "Skipping MP3 (already-fetched)"
                
            # Convert to WAV
            wav_file = mp3_file.replace('.mp3', '.wav')
            if not os.path.exists(wav_file):
                print "Generating WAV file from MP3...",
                retcode = subprocess.call(['sox', mp3_file, wav_file, 'rate', '16k'])
                if retcode != 0:
                    print "fail (have you installed SoX?)"
                    sys.exit(1)
                else:
                    print "done"
            else:
                print "Skipping WAV (already-generated)"
            
            # Fetch text for chapter for Aligner
            text_file = data_path + '/%s.%d.txt' % (book.osis, chapter)
            if not path.exists(text_file):
                print "Fetching text...",
                params = (
                    'key=IP',
                    'output-format=plain-text',
                    'passage=' + urllib.quote('{book}+{chapter}'.format(book=book.name, chapter=chapter)),
                    'include-passage-references=false',
                    'include-first-verse-numbers=false',
                    'include-verse-numbers=false',
                    'include-footnotes=false',
                    'include-short-copyright=false',
                    'include-passage-horizontal-lines=false',
                    'include-heading-horizontal-lines=false',
                    'include-headings=false',
                    'include-subheadings=false',
                    'include-selahs=true',
                    'line-length=0',
                )
                text_url = 'http://www.esvapi.org/v2/rest/passageQuery?' + '&'.join(params)
                fi = urllib.urlopen(text_url)
                # @todo What is the encoding of the response??
                if not fi.getcode() or fi.getcode() != 200:
                    print "Failed, getcode =", fi.getcode()
                    sys.exit(1)
                else:
                    print "done"
                fo = open(text_file, 'w')
                chapter_text = fi.read()
                fo.write(chapter_text)
                fi.close()
                fo.close()
            else:
                fi = codecs.open(text_file, mode='r', encoding='utf-8')
                chapter_text = fi.read()
                fi.close()
                print "Skipping text (already-fetched)"
            
            # Fetch HTML for chapter
            html_file = data_path + '/%s.%d.html' % (book.osis, chapter)
            if not path.exists(html_file):
                print "Fetching HTML...",
                params = (
                    'key=IP',
                    'passage=' + urllib.quote('{book}+{chapter}'.format(book=book.name, chapter=chapter)),
                    'include-passage-references=false',
                    'include-first-verse-numbers=false',
                    'include-verse-numbers=true',
                    'include-footnotes=true',
                    'include-surrounding-chapters=false',
                    'include-audio-link=false',
                    'include-short-copyright=false',
                    'include-copyright=true',
                )
                html_url = 'http://www.esvapi.org/v2/rest/passageQuery?' + '&'.join(params)
                fi = urllib.urlopen(html_url)
                if not fi.getcode() or fi.getcode() != 200:
                    print "Failed, getcode =", fi.getcode()
                    sys.exit(1)
                else:
                    print "done"
                fo = open(html_file, 'w')
                fo.write(fi.read())
                fi.close()
                fo.close()
            else:
                print "Skipping HTML (already-fetched)"
            
            # Create batch file for this chapter
            f = open(long_audio_aligner_path + '/resource/batchFile.txt', 'w')
            f.write('../data/{book}.{chapter}.txt ../data/{book}.{chapter}.wav'.format(book=book.osis, chapter=chapter))
            f.close()
            
            # Now run the aligner on the batchFile
            timings_file = data_path + '/%s.%d.timings.json' % (book.osis, chapter)
            if not path.exists(timings_file) or is_force:
                print "Aligning text...",
                
                cwd = path.realpath(path.curdir)
                os.chdir(long_audio_aligner_path)
                retcode = subprocess.call(['java', '-Xmx3g', '-jar', 'bin/aligner.jar'])
                if retcode != 0:
                    print "fail (haz Java?)"
                    sys.exit(0)
                else:
                    print "success"
                os.chdir(cwd)
                
                # Chapter word segments
                unnormalized_word_chunks = chapter_text.strip().split()
                
                # Copy the aligned output into the data directory
                fi = codecs.open(long_audio_aligner_path + '/timedOutput/1.txt', encoding='utf-8')
                raw_timings = fi.read().split()
                fi.close()
                
                # Parse the timings out of the raw timings, and then pair up the
                # normalized word from Sphinx with the actual word from the text
                timings = []
                normalize_word_chunk = lambda s: re.sub(r'\W', '', s).lower()
                stip_punc = lambda s: re.sub(r'^\W+|\W+$', '', s)
                for raw_timing in raw_timings:
                    matches = re.match(r'(.+)\((.+),(.+)\)', raw_timing)
                    word = matches.group(1)
                    if word == '<unk>':
                        word = None
                    else:
                        skipped_words = 0
                        while True:
                            unnormalized_word_chunk = unnormalized_word_chunks.pop(0)
                            if word == normalize_word_chunk(unnormalized_word_chunk):
                                word = stip_punc(unnormalized_word_chunk)
                                break
                            skipped_words.append(unnormalized_word_chunk)
                            if len(skipped_words) > 5:
                                print "Warning! Skipping several words: " + ", ".join(skipped_words)
                    
                    timings.append({
                        "word":  word,
                        "start": float(matches.group(2)),
                        "end":   float(matches.group(3)),
                    })
                fo = codecs.open(timings_file, mode='w', encoding='utf-8')
                fo.write(json.dumps(timings, indent=2))
                fo.close()
            else:
                print "Text already aligned"
            
            print "Time: %.02fs" % (clock() - chapter_start_time)
            print "--"
        
        print "%s book execution time: %.02fs" % (book.name, clock() - book_start_time)
        
    print "Total execution time: %.02fs" % (clock() - init_start_time)


# Run tests
if __name__ == '__main__':
    align(sys.argv[1:])
