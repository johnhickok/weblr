#!/usr/bin/env python
# Thanks to everyone on the 4th floor, we have access to a lot of 
# scanned land documents. To accelerate access to these documents,
# I built this simple script for my own use, and maybe share it with 
# some of my friends. jhickok@dpw.lacounty.gov, 10/31/2012

# Module for opening web pages and for sqlite3
# For more help on Python and sqlite3, visit http://docs.python.org/library/sqlite3.html
# John Hickok, May 22, 2013

import webbrowser
import sqlite3
import urllib

# Set up empty variables (I am a C programmer at heart!)

# Text:
doctype = ns = mbt = pgt = twnshipt = rnget = ''

# Integers:
mb = pg = twnship = rnge = 0

print """
Enter 'a' (Assessor), MB, Page
Enter 't' (Tract), MB, Page
Enter 'p' (Parcel Map) MB, Page
Enter 'r' (Record of Survey), MB, Page
Enter 'mr' (Miscellaneos Records), MB, Page
Enter 'twp' (Township Plat), Township, n/s, Range

Enter 'pwfb' (Public Works Field Book), MB, Page
Enter 'rdfb' (Road Department Field Book), MB, Page
Enter 'cefb' (County Engineering Field Book), MB, Page
Enter 'csfb' (County Surveyor Field Book), MB, Page
Enter 'fcfb' (Flood Control Field Book), MB, Page
Enter 'fdfb' (Flood Control Storm Drain), MB, Page
Enter 'crfb' (Corner Records), MB, Page
(To get the entire field book, don't add the page number)

Enter 'w' to go to the Main Web Page (tracts)
Enter 'f' to go to the Main Web Page (field books)
Enter 'readme' to open the README file
Enter 'q' to quit
"""

# BEGIN WHILE LOOP
while 1:

  instring = raw_input( "Enter :  " )

  # ESCAPE HERE
  if instring == 'q': break
  
  # Split user input instring
  
  list1 = instring.split()
  
  # Assign variables based on number of entries
  # Ensure numbers entered are integers
  
  if (instring[0:4] == 'pwfb' or 
      instring[0:4] == 'rdfb' or 
      instring[0:4] == 'cefb' or 
      instring[0:4] == 'csfb' or 
      instring[0:4] == 'fcfb' or 
      instring[0:4] == 'fdfb'):
      
    if len(list1) == 2:
      doctype = list1[0]
      fmb = list1[1]
        
    elif len(list1) == 3:
      doctype = list1[0]
      fmb = list1[1]
      fpg = list1[2]

  else:          
    if len(list1) == 1:
      doctype = list1[0]
    
    elif len(list1) == 3:
      doctype = list1[0]
      mb = int(list1[1])
      pg = int(list1[2])
        
    elif len(list1) == 4:
      doctype = list1[0]
      twnship = int(list1[1])
      ns = list1[2]
      rnge = int(list1[3])
    
    else: print "Only enter 1, 3 or 4 items"
     
  
  # For map book (mb) and page (pg) variables, convert
  # integer values to text with leading zeroes. Map book numbers
  # for tract maps need four digits, while most others need three
  # For PLSS plats, range numbers need two digits. Los Angeles 
  # County straddles the Base Line; townships only need single digits.
     
  if (doctype == 't' 
      or doctype == 'T'
      or doctype == 'a'
      or doctype == 'A'
      ):
    if mb < 10:
      mbt = '000' + str(mb)
    elif (mb >= 10 and mb < 100):
      mbt = '00' + str(mb)
    elif (mb >= 100 and mb < 1000):
      mbt = '0' + str(mb)
    elif (mb >= 1000 and mb < 10000):
      mbt = str(mb)
                
    else: webbrowser.open('\\\\pwgisfile\\AssetManagement\\JohnH\\weblr\\README.html')
  
  
  elif (doctype == 'p' 
      or doctype == 'r' 
      or doctype == 'mr' ):
    if mb < 10:
      mbt = '00' + str(mb)
    elif (mb >= 10 and mb < 100):
      mbt = '0' + str(mb)
    elif (mb >= 100 and mb < 1000):
      mbt = str(mb)
          
    else: webbrowser.open('\\\\pwgisfile\\AssetManagement\\JohnH\\weblr\\README.html')    
  
  if pg < 10:
    pgt = '00' + str(pg)
  elif (pg >= 10 and pg < 100):
    pgt = '0' + str(pg)
  elif (pg >= 100 and pg < 1000):
    pgt = str(pg)
     
  else: webbrowser.open('\\\\pwgisfile\\AssetManagement\\JohnH\\weblr\\README.html')
  
  if doctype == 'twp':
    twnshipt = str(twnship)
    if rnge < 10:
      rnget = '0' + str(rnge)
    elif (rnge >= 10 and rnge < 100):
      rnget = str(rnge)
    else: webbrowser.open('\\\\pwgisfile\\AssetManagement\\JohnH\\weblr\\README.html')
  
  
  # Text strings to begin urls
  webpdf = 'http://dpw.lacounty.gov/sur/nas/landrecords/' 
  webmain = 'http://dpw.lacounty.gov/sur/surveyrecord/'
  fbmain = 'http://dpw.lacounty.gov/sur/nas/landrecords/'
  
  #print webpdf
  #print webmain 
  
  
  # Populate variable url:
  
  if (doctype == 't' and mb > 23):
    print 'Downloading map book ' + str(mb) + ' page(s) ' + str(pg) + ' through...'
    urllib.urlretrieve(webpdf + 'tract/MB' + mbt + '/TR' + mbt + '-' + pgt + '.pdf', 'TR' + mbt + '-' + pgt + '.pdf')
    print 'Done'
    
  elif doctype == 'p':
    print 'Downloading map book ' + str(mb) + ' page(s) ' + str(pg) + ' through...'
    urllib.urlretrieve(webpdf + 'parcel/PM' + mbt + '/PM' + mbt + '-' + pgt + '.pdf', 'PM' + mbt + '-' + pgt + '.pdf')
    print 'Done'
  
  elif doctype == 'r':
    print 'Downloading map book ' + str(mb) + ' page(s) ' + str(pg) + ' through...'
    urllib.urlretrieve(webpdf + 'survey/RS' + mbt + '/RS' + mbt + '-' + pgt + '.pdf', 'RS' + mbt + '-' + pgt + '.pdf')
    print 'Done'
  
  elif doctype == 'mr':
    print 'Downloading map book ' + str(mb) + ' page(s) ' + str(pg) + ' through...'
    urllib.urlretrieve(webpdf + 'misc/MR' + mbt + '/MR' + mbt + '-' + pgt + '.pdf', 'MR' + mbt + '-' + pgt + '.pdf')
    print 'Done'
  
  elif doctype == 'twp':
    print 'Downloading your Township Plat...'
    urllib.urlretrieve(webpdf + 'Township/T%20' + twnshipt + '%20' + ns + '%20R%20' + rnget + '%20W.pdf', 'T' + twnshipt + ns.upper() + rnget + 'W.pdf')
    print 'Done'
      
# TEST - ADD FIELD PAGE LINKS

  elif doctype == 'pwfb' and len(list1) == 3:
    print 'Downloading your field page...'
    urllib.urlretrieve(webpdf + 'centerlines/PWFB' + fmb + '-' + fpg + '.pdf', 'PWFB' + fmb + '-' + fpg + '.pdf')
    print 'Done'

  elif doctype == 'rdfb' and len(list1) == 3:
    print 'Downloading your field page...'
    urllib.urlretrieve(webpdf + 'centerlines/RDFB' + fmb + '-' + fpg + '.pdf', 'RDFB' + fmb + '-' + fpg + '.pdf')
    print 'Done'

  elif doctype == 'cefb' and len(list1) == 3:
    print 'Downloading your field page...'
    urllib.urlretrieve(webpdf + 'centerlines/CEFB' + fmb + '-' + fpg + '.pdf', 'CEFB' + fmb + '-' + fpg + '.pdf')
    print 'Done'

  elif doctype == 'csfb' and len(list1) == 3:
    print 'Downloading your field page...'
    urllib.urlretrieve(webpdf + 'centerlines/CSFB' + fmb + '-' + fpg + '.pdf', 'CSFB' + fmb + '-' + fpg + '.pdf')
    print 'Done'

  elif doctype == 'fcfb' and len(list1) == 3:
    print 'Downloading your field page...'
    urllib.urlretrieve(webpdf + 'centerlines/FCFB' + fmb + '-' + fpg + '.pdf', 'FCFB' + fmb + '-' + fpg + '.pdf')
    print 'Done'

  elif doctype == 'fdfb' and len(list1) == 3:
    print 'Downloading your field page...'
    urllib.urlretrieve(webpdf + 'centerlines/FDFB' + fmb + '-' + fpg + '.pdf', 'FDFB' + fmb + '-' + fpg + '.pdf')
    print 'Done'

# TEST - ADD FIELD BOOK LINKS

  elif doctype == 'pwfb' and len(list1) == 2:
    print 'Downloading your field book...'
    urllib.urlretrieve(webpdf + 'fieldbooks/PWFB/PWFB' + fmb + '.pdf', 'PWFB' + fmb + '.pdf')
    print 'Done'

  elif doctype == 'cefb' and len(list1) == 3:
    print 'Downloading your field book...'
    urllib.urlretrieve(webpdf + 'fieldbooks/CEFB/CEFB' + fmb + '.pdf', 'CEFB' + fmb + '.pdf')
    print 'Done'

  elif doctype == 'csfb' and len(list1) == 3:
    print 'Downloading your field book...'
    urllib.urlretrieve(webpdf + 'fieldbooks/CSFB/CSFB' + fmb + '.pdf', 'CSFB' + fmb + '.pdf')
    print 'Done'


# OTHER HELPFUL WEB PAGES

  elif doctype == 't' and len(list1) == 1:
    webbrowser.open(webmain + 'tractMain.cfm')
  
  elif doctype == 'f':
    webbrowser.open(webmain + 'fbMain.cfm')
  
  elif (doctype == 'readme' or doctype == 'README'):
    webbrowser.open('\\\\pwgisfile\\AssetManagement\\JohnH\\weblr\\README.html')
  	
  elif (doctype == 't' and mb < 23):
  # sqlite database was created for tract map books 1 through 23
  # From around 1900 to 1913, tracts were typically named and not numbered, 
  # and it was common practice to place more than one tract on a 
  # recorded map book and page.
  
    c = sqlite3.connect('OldTract.db')
  
    qsrch = 'SELECT [LINK], [REF] FROM tblTract WHERE (((tblTract.MB)=' + str(mb) + ') AND ((tblTract.PG)=' + str(pg) + '))'

    for row in c.execute(qsrch):
      print 'Downloading ' + str(row[1])
      urllib.urlretrieve(str(row[0]) , str(row[1]) + '.pdf' )
      print 'Done'
  
    c.close()
  
  #else: url = '\\\\pwgisfile\\AssetManagement\\JohnH\\weblr\\README.html'
  
  else: print "No URL? Try again!"
