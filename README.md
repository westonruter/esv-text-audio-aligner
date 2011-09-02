ESV Text/Audio Aligner
======================

Pulls down the ESV text and audio from the ESV API, then aligns the text and
audio chapter-by-chapter by means of [CMU Sphinx](http://cmusphinx.sourceforge.net/)
and generates `{book}.{chapter}.timings.json` timing files in the `data/`
directory. The audio and text for each chapter is also saved in this directory.
Previously-aligned chapters are skipped unless `--force`d. There is an
ongoing [discussion](http://sourceforge.net/projects/cmusphinx/forums/forum/382337/topic/4503550)
on the CMU Sphinx forums on the quality of the alignment data it provides.

__Author__: Weston Ruter ([@westonruter](https://twitter.com/westonruter)) <http://weston.ruter.net/>  
__GitHub__: https://github.com/westonruter/esv-audio-timings  
__Dependencies__: Python 2.7, java, ant, [sox](http://sox.sourceforge.net/), svn

The ESV Text and MP3 data downloaded by this script is subject to [copyright](http://www.crossway.org/rights-permissions/esv/):

 > The Holy Bible, English Standard Version copyright (c)2001 by Crossway Bibles, a
 > publishing ministry of Good News Publishers. Used by permission. All rights
 > reserved.

ESV API usage terms (see [full conditions](http://www.esvapi.org/#conditions)):

 > You can access the ESV text using the key "IP" (without the quotes). This
 > key limits you to 5,000 queries per day from a single IP address. You are
 > bound by the below conditions of use, including the non-commercial
 > aspects.

Background
----------

This project was birthed out of a desire to realize the read-along app, where
the currently-spoken word in the audio is higlighted in the text on the screen.
I made an [HTML5 Audio Read-Along prototype](http://weston.ruter.net/projects/html5-audio-read-along/)
(includes writeup) featuring a passage from Luke 2 of the ESV, but the actual audio timing
data for the Luke 2 sample I had to obtain manually (read: painstakingly). This
project aims to generate the audio word timings automatically so that the entire
Bible can be used in a read-along app.

Usage
-----

    $ python align.py [-f|--force] [osisBook [[chapter], [chapter]...]]...

Examples
--------

Align Genesis 1:

    $ python align.py Gen 1

Align John 3, overridding any existing timings:

    $ python align.py -f John 3

Align Genesis 1-3, Psalm 1, and all of Colossians:

    $ python align.py Gen 1 2 3 Ps 1 Col

License
-------
Dual licensed under the MIT or GPL Version 2 licenses.  
MIT License: http://creativecommons.org/licenses/MIT/  
GPL 2.0 license: http://creativecommons.org/licenses/GPL/2.0/
