WebLR = Web Land Records. A simple Python script was created to retrieve Assessor pages, subdivision survey, and Record of Survey's stored on the DPW website.

WebLR.py - The core script used for retrieving web pages, typically recorded subdivisions.

mylinks.py - This file is easy for a non-Python programmer to edit, containing a single Python dictionary. The dictionary contains shortcuts to websites chosen by the user.

myapps.py - This file contains a single Python dictionary for users to define shortcuts that will open Windows applications.

OldTract.db - A small sqlite database containing urls for tracts stored in Map Books 1 through 24. 

WebLR_single.py - Just like WebLR, except the Windows Console closes after opening a single web page. Some users prefer this.

DownloadLR.py - Downloads PDF's where WebLR opens pages. This script is a little crude at this time. It should work well for Subdivisions and Survey records. Not much is planned at this time to develop this script.

THE USER OF THIS SCRIPT AGREES TO AND ACCEPTS ALL DISCLAIMERS ON ALL WEB SITES ACCESSED.

John Hickok, May 22, 2013
