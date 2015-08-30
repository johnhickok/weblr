#!/usr/bin/env python
# Thanks to everyone on the 4th floor, we have access to a lot of 
# scanned land documents. To accelerate access to these documents,
# I built this simple script for my own use, and maybe to share it with 
# some of my friends. jhickok@dpw.lacounty.gov, 10/31/2012
# UPDATE - Python's answer to swith-case http://bytebaker.com/2008/11/03/switch-case-statement-in-python/

# Module for opening web pages and for sqlite3 queries
# For more help on Python and sqlite3, 
# visit http://docs.python.org/library/sqlite3.html
# In the folder \\pwgisfile\AssetManagement\JohnH\weblr there are two files 
# that this script accesses: OldTract.db (sqlite database) and README.html

import webbrowser
import sqlite3
import mylinks
import myapps
import os
import subprocess

# Set up empty variables (I am a C programmer at heart!)
# Declare TEXT variables:
doctype = ns = mbt = pgt = twnshipt = rnget = ''

# Declare INTEGER variables:
mb = pg = twnship = rnge = 0

print """
Enter 'a' (Assessor), MB, Page
Enter 't' (Tract), MB, Page
Enter 'p' (Parcel Map) MB, Page
Enter 'r' (Record of Survey), MB, Page
Enter 'mr' (Miscellaneous Records), MB, Page
Enter 'twp' (Township Plat), Township, n/s, Range

Enter 'a' to go to the Assessor's Parcel Viewer
Enter 't' to go to the Main Web Page (tracts)
Enter 'f' to go to the Main Web Page (field books)
Enter 'q' to quit (after you close the browser!)

THE USER OF THIS SCRIPT AGREES TO AND ACCEPTS ALL 
DISCLAIMERS ON ALL WEB SITES ACCESSED.
"""

# BEGIN WHILE LOOP
while 1:

  instring = raw_input( "Enter :  " )
  
  # User input 'q' escapes the while loop and exits the program
  if instring == 'q': break
  
  # Split user input instring
  
  list1 = instring.split()
  
  # Assign variables based on number of entries
  # Ensure numbers entered are integers
  
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
     
  
  # For map book (mb) and page (pg) variables, convert integer values to text 
  # with leading zeroes. Map book numbers for tract maps and Assessor maps need
  # four digits, while most others need three. For PLSS plats, range numbers 
  # need two digits. Los Angeles County straddles the Base Line; townships only
  # need single digits.
  if doctype in ('t', 'T', 'a', 'A'):
    if mb < 10:
      mbt = '000' + str(mb)
    elif (mb >= 10 and mb < 100):
      mbt = '00' + str(mb)
    elif (mb >= 100 and mb < 1000):
      mbt = '0' + str(mb)
    elif (mb >= 1000 and mb < 10000):
      mbt = str(mb)
    else: print "You may have typed the wrong Map Book Number."
  
  # Parcel Maps, Records of Survey, Misc Records share similar text structures
  elif doctype in ('p', 'P', 'r', 'R', 'mr', 'MR', 'Mr', 'mR'):
    if mb < 10:
      mbt = '00' + str(mb)
    elif (mb >= 10 and mb < 100):
      mbt = '0' + str(mb)
    elif (mb >= 100 and mb < 1000):
      mbt = str(mb)
    else: print "You may have typed the wrong Map Book Number."    
  
  if pg < 10:
    pgt = '00' + str(pg)
  elif (pg >= 10 and pg < 100):
    pgt = '0' + str(pg)
  elif (pg >= 100 and pg < 1000):
    pgt = str(pg)
  else: print "You may have typed the wrong Page Number."    

  
  # The user enters 'twp' to view a Township plat
  if doctype in ('twp', 'TWP', 'Twp'):
    #REVISION: "SELECT COUNT(*) FROM TWP_PLATTS WHERE TWP = 9 AND NS = 'N' AND RNGE = 11;"
    # select substr('0000000000' || mycolumn, -10, 10) from mytable
    
    twnshipt = str(twnship)
    if rnge < 10:
      rnget = '0' + str(rnge)
    elif (rnge >= 10 and rnge < 21):
      rnget = str(rnge)
    else: print """
      You may have entered the wrong Township and Range numbers.
      L.A. County lies within Townships 5 South through 8 North and
      Ranges 20 West through 7 West. No 'e' or 'w' is needed.
      """
  
  # Text strings to begin urls
  webpdf = 'http://dpw.lacounty.gov/sur/nas/landrecords/' 
  webmain = 'http://dpw.lacounty.gov/smpm/landrecords/'

  # The following block of "if" statements open urls in your default browser.
  # The first two statements search the user's custom dictionaries
  # mylinks.py and myapps.py. The rest are 'hard-wired' into this core script.
  # User's custom dictionaries override whatever is further below.
  
  if mylinks.Dweb.has_key(doctype):
    webbrowser.open(mylinks.Dweb[doctype])
    
  elif myapps.Dapp.has_key(doctype):
    os.startfile(myapps.Dapp[doctype])
    
  # Added the next 2 lines for opening Pictometry Online in Firefox
  elif doctype == 'pol':
    subprocess.call([r'C:\Program Files\Mozilla Firefox\firefox.exe',
    '-new-tab', 'https://pol.pictometry.com/en-us/app/login.php'])
  
  elif (doctype == 'a' or doctype == 'A') and len(list1) == 3:
    webbrowser.open('http://maps.assessor.lacounty.gov/Geocortex/Essentials/REST/sites/PAIS/VirtualDirectory/AssessorMaps/ViewMap.html?val=' + mbt + '-' + pgt)
  
  #elif ((doctype == 't' or doctype == 'T') and mb > 24):
  elif doctype in ('t', 'T') and mb > 24:
    webbrowser.open(webpdf + 'tract/MB' + mbt + '/TR' + mbt + '-' + pgt + '.pdf')
  
  elif doctype in ('p', 'P'):
    webbrowser.open(webpdf + 'parcel/PM' + mbt + '/PM' + mbt + '-' + pgt + '.pdf')
  
  elif doctype in ('r', 'R') and len(list1) == 3:
    webbrowser.open(webpdf + 'survey/RS' + mbt + '/RS' + mbt + '-' + pgt + '.pdf')
  
  elif doctype in ('mr', 'MR', 'Mr'):
    webbrowser.open(webpdf + 'misc/MR' + mbt + '/MR' + mbt + '-' + pgt + '.pdf')
  
  elif doctype in ('twp', 'TWP', 'Twp'):
    webbrowser.open(webpdf + 'Township/T%20' + twnshipt + '%20' + ns + '%20R%20' + rnget + '%20W.pdf')
  
  elif doctype in ('a', 'A') and len(list1) == 1:
    webbrowser.open('http://assessormap.co.la.ca.us/mapping/viewer.asp')

  elif doctype in ('t', 'T') and len(list1) == 1:
    webbrowser.open(webmain + 'TractMaps.aspx')
  
  elif doctype in ('f', 'F'):
    webbrowser.open(webmain + 'FieldBooks.aspx')
  	
  elif ((doctype == 't' or doctype == 'T') and mb < 24):
    # A sqlite database was created for tract map books 1 through 24
    # From around 1900 to 1913, tracts were typically named and not numbered, 
    # and it was common practice to place more than one tract on a 
    # recorded map book and page.
    
    listurl = []
    
    webbrowser.open('about:blank')
    
    c = sqlite3.connect('OldTract.db')
    
    # parse a query search string qsearch
    qsrch = 'SELECT [LINK] FROM tblTract WHERE (((tblTract.MB)=' + str(mb) + ') AND ((tblTract.PG)=' + str(pg) + '))'
    
    for row in c.execute(qsrch):
    	listurl.append(str(row[0]))  
    
    for url in listurl:
    	webbrowser.open(url)
    
    c.close()
  
  else: webbrowser.open('\\\\pwgisfile\\AssetManagement\\JohnH\\weblr\\README.html')

