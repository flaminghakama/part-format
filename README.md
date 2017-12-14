h2. Overview 

h3. Input

Supply a list of the pdf files you want to print, optionally preceded with the desired page layout formats
* Exampe:  create-print-job.py -outputFilePrefix Smooch smooch-Flute.pdf 3 smooch-English-Horn-in-F.pdf 4 smooch-violin-I.pdf 4

The page layout formats can be ommitted, in which case a default layout format will be chosen.
This will be based on the number of pages in the file.


Output: 

* Creates two pdf files, one for insides, and one for outsides.  
** The order of the pages in the insides will be reversed, to accommodate re-feeding the pages
** Files are named <name>-outside.pdf and <name>-inside.pdf
** <name> is either specified as a command line option -outputFilePrefix, or a default (based on time)
** Displays the number of pages needed for the batch, the file names, and the print commands 


Command line processing

Define <name> based on the presence of -outputFilePrefix, or use the default date format YYMMDD-HHMMSS
For the expected 

Next we process the file names and page layout formats.

# Look at the first argument and expect it to be a file name.
# Validate that it is an existing file, or report the error and exit.
# Look at the next argument.  If it matches a valid page layout format, use that format for the file.  Otherwise, determine the number of pages in the file and choose the default layout for that number of pages.

defaultFormats = {
	'1': '1',
	'1': '2',
	'3': '1L',
	'1': '1L',
	'1': '1L',
	'1': '1L',
	'1': '1L',
	'1': '1L',
	'1': '1L',
	'1': '1L',
	'1': '1L',



1L: 1 page (L) => X 1
1R: 1 page (R) => 1 X

2CL: 2 page compact (L) => X 1 | 2 X
2CR: 2 page compact (R) => 2 X | X 1

2: 2 page => X X | 1 2 

3: 3 page / 2 page with title => X 1 | 2 3 

4: 4 page, 3 page with title => 4 1 | 2 3

5L: 5 page (L) / 4 page with title (L) =>  X 1 | 2 5, X 3 | 4 X
5L: 5 page (R) / 4 page with title (R) =>  X 1 | 2 5, 4 X | X 3

6L: 6 page (L) / 5 page with title (L) => 6 1 | 2 5, X 3 | 4 X
6R: 6 page (R) / 5 page with title (R) => 6 1 | 2 5, 4 X | X 3

7: 7 page, 6 page with title => X 1 | 2 7, 6 3 | 4 5 

8: 8 page, 7 page with title => 8 1 | 2 7, 6 3 | 4 5

9L: 9 page (L) / 8 page with title (L) => X 1 | 2 9,  8 3 | 4 7 , X 5 | 6 X  
9R: 9 page (R) / 8 page with title (R) => X 1 | 2 9,  8 3 | 4 7 , 6 X | X 5

10L: 10 page (L) / 9 page with title (L) => 10 1 | 2 9, 8 3 | 4 7, X 5 | 6 X 
10R: 10 page (R) / 9 page with title (R) => 10 1 | 2 9, 8 3 | 4 7, 6 X | X 5

11: 11 page, 10 page with title => X 1 | 2 11 , 10 3 | 4 9 , 8 5 | 6 7 

12: 	12 page, 11 page with title => 12 1 | 2 11, 10 3 | 4 9, 8 5 | 6 7 





For full-page formats, the front and back sides are queued up in a straightforward manner.

For half-page formats (1, 2C, 5, 6C, 9, 10), the queuing goes as follows:
* complete pages are treated as full-page formats, and queued immediately.
* When there is a half page, it alternates L - R.  The half-page sheet is queued when both sides are full.
* When done, if there is an incomplete sheet, queue it up 


Example:

4 2C 4 4 5

4 is one page queued immediately
2C is added as L and not queued
4 is one page queued immediately
4 is one page queued immediately
5 has first page queued immediately
half-page of 5 is added as R to the 2C, and this page is queued




Layout Formats:

1L: 1 page (L) => X 1
1R: 1 page (R) => 1 X

2CL: 2 page compact (L) => X 1 | 2 X
2CR: 2 page compact (R) => 2 X | X 1

2: 2 page => X X | 1 2 

3: 3 page / 2 page with title => X 1 | 2 3 

4: 4 page, 3 page with title => 4 1 | 2 3

5L: 5 page (L) / 4 page with title (L) =>  X 1 | 2 5, X 3 | 4 X
5L: 5 page (R) / 4 page with title (R) =>  X 1 | 2 5, 4 X | X 3

6CL: 6 page compact (L) / 5 page with title (L) => 6 1 | 2 5, X 3 | 4 X
6CR: 6 page compact (R) / 5 page with title (R) => 6 1 | 2 5, 4 X | X 3

7: 7 page, 6 page with title => X 1 | 2 7, 6 3 | 4 5 

8: 8 page, 7 page with title => 8 1 | 2 7, 6 3 | 4 5

9L: 9 page (L) / 8 page with title (L) => X 1 | 2 9,  8 3 | 4 7 , X 5 | 6 X  
9R: 9 page (R) / 8 page with title (R) => X 1 | 2 9,  8 3 | 4 7 , 6 X | X 5

10L: 10 page (L) / 9 page with title (L) => 10 1 | 2 9, 8 3 | 4 7, X 5 | 6 X 
10R: 10 page (R) / 9 page with title (R) => 10 1 | 2 9, 8 3 | 4 7, 6 X | X 5

11: 11 page, 10 page with title => X 1 | 2 11 , 10 3 | 4 9 , 8 5 | 6 7 

12: 	12 page, 11 page with title => 12 1 | 2 11, 10 3 | 4 9, 8 5 | 6 7 
