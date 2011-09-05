#!/usr/bin/env python
"""
Basic metadata for books of the Bible
"""

class BookInfo:
    def __init__(self, chapters, osis, name):
        self.chapters = chapters
        self.osis = osis
        self.name = name

# @todo This might work better as an OrderedDict, keyed by osisBook
books = (
    BookInfo(range(1,50+1),  'Gen',    'Genesis'),
    BookInfo(range(1,40+1),  'Exod',   'Exodus'),
    BookInfo(range(1,27+1),  'Lev',    'Leviticus'),
    BookInfo(range(1,36+1),  'Num',    'Numbers'),
    BookInfo(range(1,34+1),  'Deut',   'Deuteronomy'),
    BookInfo(range(1,24+1),  'Josh',   'Joshua'),
    BookInfo(range(1,21+1),  'Judg',   'Judges'),
    BookInfo(range(1,4+1),   'Ruth',   'Ruth'),
    BookInfo(range(1,31+1),  '1Sam',   '1 Samuel'),
    BookInfo(range(1,24+1),  '2Sam',   '2 Samuel'),
    BookInfo(range(1,22+1),  '1Kgs',   '1 Kings'),
    BookInfo(range(1,25+1),  '2Kgs',   '2 Kings'),
    BookInfo(range(1,29+1),  '1Chr',   '1 Chronicles'),
    BookInfo(range(1,36+1),  '2Chr',   '2 Chronicles'),
    BookInfo(range(1,10+1),  'Ezra',   'Ezra'),
    BookInfo(range(1,13+1),  'Neh',    'Nehemiah'),
    BookInfo(range(1,10+1),  'Esth',   'Esther'),
    BookInfo(range(1,42+1),  'Job',    'Job'),
    BookInfo(range(1,150+1), 'Ps',     'Psalms'),
    BookInfo(range(1,31+1),  'Prov',   'Proverbs'),
    BookInfo(range(1,12+1),  'Eccl',   'Ecclesiastes'),
    BookInfo(range(1,8+1),   'Song',   'Song of Solomon'),
    BookInfo(range(1,66+1),  'Isa',    'Isaiah'),
    BookInfo(range(1,52+1),  'Jer',    'Jeremiah'),
    BookInfo(range(1,5+1),   'Lam',    'Lamentations'),
    BookInfo(range(1,48+1),  'Ezek',   'Ezekiel'),
    BookInfo(range(1,12+1),  'Dan',    'Daniel'),
    BookInfo(range(1,14+1),  'Hos',    'Hosea'),
    BookInfo(range(1,3+1),   'Joel',   'Joel'),
    BookInfo(range(1,9+1),   'Amos',   'Amos'),
    BookInfo(range(1,1+1),   'Obad',   'Obadiah'),
    BookInfo(range(1,4+1),   'Jonah',  'Jonah'),
    BookInfo(range(1,7+1),   'Mic',    'Micah'),
    BookInfo(range(1,3+1),   'Nah',    'Nahum'),
    BookInfo(range(1,3+1),   'Hab',    'Habakkuk'),
    BookInfo(range(1,3+1),   'Zeph',   'Zephaniah'),
    BookInfo(range(1,2+1),   'Hag',    'Haggai'),
    BookInfo(range(1,14+1),  'Zech',   'Zechariah'),
    BookInfo(range(1,4+1),   'Mal',    'Malachi'),
    BookInfo(range(1,28+1),  'Matt',   'Matthew'),
    BookInfo(range(1,16+1),  'Mark',   'Mark'),
    BookInfo(range(1,24+1),  'Luke',   'Luke'),
    BookInfo(range(1,21+1),  'John',   'John'),
    BookInfo(range(1,28+1),  'Acts',   'Acts'),
    BookInfo(range(1,16+1),  'Rom',    'Romans'),
    BookInfo(range(1,16+1),  '1Cor',   '1 Corinthians'),
    BookInfo(range(1,13+1),  '2Cor',   '2 Corinthians'),
    BookInfo(range(1,6+1),   'Gal',    'Galatians'),
    BookInfo(range(1,6+1),   'Eph',    'Ephesians'),
    BookInfo(range(1,4+1),   'Phil',   'Philippians'),
    BookInfo(range(1,4+1),   'Col',    'Colossians'),
    BookInfo(range(1,5+1),   '1Thess', '1 Thessalonians'),
    BookInfo(range(1,3+1),   '2Thess', '2 Thessalonians'),
    BookInfo(range(1,6+1),   '1Tim',   '1 Timothy'),
    BookInfo(range(1,4+1),   '2Tim',   '2 Timothy'),
    BookInfo(range(1,3+1),   'Titus',  'Titus'),
    BookInfo(range(1,1+1),   'Phlm',   'Philemon'),
    BookInfo(range(1,13+1),  'Heb',    'Hebrews'),
    BookInfo(range(1,5+1),   'Jas',    'James'),
    BookInfo(range(1,5+1),   '1Pet',   '1 Peter'),
    BookInfo(range(1,3+1),   '2Pet',   '2 Peter'),
    BookInfo(range(1,5+1),   '1John',  '1 John'),
    BookInfo(range(1,1+1),   '2John',  '2 John'),
    BookInfo(range(1,1+1),   '3John',  '3 John'),
    BookInfo(range(1,1+1),   'Jude',   'Jude'),
    BookInfo(range(1,22+1),  'Rev',    'Revelation'),
)


def get_book_subset(args):
    """
    Get a subset of BookInfo books; if args is empty, returns all books
    
    args -- a list of osisBooks and chapter numbers; the chapter numbers are associated
    
    with their immediately-preceding osisBook. If an osisBook appears without any
    subsequent chapters, then all chapters in the book will be returned.
    
    >>> subset_books = get_book_subset('John', '1')
    >>> len(subset_books)
    1
    >>> subset_books[0].osis
    'John'
    >>> len(subset_books[0].chapters)
    1
    >>> subset_books[0].chapters[0]
    1
    >>> subset_books = get_book_subset('Mark', '1', '3', '6', 'Jude')
    >>> subset_books[0].chapters
    [1, 3, 6]
    >>> len(subset_books)
    2
    >>> subset_books[1].osis
    'Jude'
    >>> subset_books[1].chapters
    [1]
    >>> len(get_book_subset())
    66
    >>> subset_books = get_book_subset('Mark', '1', 'Mark')
    Traceback (most recent call last):
    ...
    ValueError: You already provided the osisBook 'Mark'
    >>> subset_books = get_book_subset('1', 'Mark')
    Traceback (most recent call last):
    ...
    ValueError: Expected osisBook. A chapter must be preceded by an osisBook
    >>> subset_books = get_book_subset('Jude', 2)
    Traceback (most recent call last):
    ...
    ValueError: Chapter '2' does not exist in Jude
    >>> subset_books = get_book_subset('Matt', 1, 2, 3, 'FOO')
    Traceback (most recent call last):
    ...
    ValueError: Invalid arg 'FOO'. Expected valid osisBook or chapter.
    >>> subset_books = get_book_subset('Matt', 1, 2, 1)
    Traceback (most recent call last):
    ...
    ValueError: You already provided chapter '1' for Matt
    
    """
    
    import re
    from copy import deepcopy
    from collections import OrderedDict
    
    osis_books = [book.osis for book in books]
    current_osis_book = None
    subset_book_dict = OrderedDict()
    for arg in args:
        # osisBook
        if arg in osis_books:
            if arg in subset_book_dict:
                raise ValueError("You already provided the osisBook '%s'" % arg)
            current_osis_book = arg
            subset_book_dict[current_osis_book] = []
        # chapter
        elif re.match('^\d+$', str(arg)):
            if current_osis_book is None:
                raise ValueError("Expected osisBook. A chapter must be preceded by an osisBook")
            
            chapter = int(arg)
            if chapter not in books[osis_books.index(current_osis_book)].chapters:
                raise ValueError("Chapter '%d' does not exist in %s" % (chapter, current_osis_book))
            
            if chapter in subset_book_dict[current_osis_book]:
                raise ValueError("You already provided chapter '%d' for %s" % (chapter, current_osis_book))
            subset_book_dict[current_osis_book].append(chapter)
        else:
            raise ValueError("Invalid arg '%s'. Expected valid osisBook or chapter." % arg)
    
    if len(subset_book_dict.keys()) == 0:
        return books
    else:
        subset_books = []
        for osis_book, chapters in subset_book_dict.iteritems():
            if len(chapters) == 0:
                subset_books.append(books[osis_books.index(osis_book)])
            else:
                book_info = deepcopy(books[osis_books.index(osis_book)])
                book_info.chapters = chapters
                subset_books.append(book_info)
        return subset_books


# Run tests
if __name__ == '__main__':
    import sys
    if '--json' in sys.argv:
        import json
        print json.dumps([book.__dict__ for book in books], indent=4)
    else:
        print "Running tests wthout without any args"
        import doctest
        doctest.testmod()
