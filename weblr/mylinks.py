# This module builds a dictionary (Dweb) containing commonly used
# websites or file and folder locations on your local hard drive.
# For your convenience, some websites have been added for you:
# 'egis'   opens the Los Angeles County Enterprise GIS website
# 'g'      opens Google
# 'gm'     opens Google Maps
# 'h'      opens ESRI's online help for ArcGIS
# 'liw'    opens our Department's Land Information Website
# 'proj'   opens, if it exists on your local drive, that folder in Windows Explorer
# 'navla'  opens L.A. City's Navigate LA Website
# 'osm'    opens the Open Street Map site
# 'viewla' opens our Department's View LA Website
# 
# You can easily add similar shortcuts to often used folders or files, 
# locally or on file servers in addition to websites you commonly use. 
# All you need to do is edit the text below. For example, if you want to 
# add Bing to your list of url's, you can add 
# 'b'   : 'http://www.bing.com',
# where 'b' (inside single quotes) is the code you enter at the main prompt, 
# and 'http://www.bing.com' (also inside single quotes) is your url.
# Note that each line needs a colon to separate your code from your url,
# and the comma has to be at the end of each line.
# John Hickok, last update May 26, 2015

Dweb = {
'egis'  : 'http://egis3.lacounty.gov/eGIS/',
'g'     : 'http://www.google.com', 
'gm'    : 'http://maps.google.com/',
'h'     : 'http://resources.arcgis.com/en/help/',
'navla' : 'http://navigatela.lacity.org/index.cfm',
'proj'  : 'file://C:/MyFiles/Projects',
'osm'   : 'http://www.openstreetmap.org/',
'viewla': 'http://pwgisw11/website/viewla/viewer.asp',
}
