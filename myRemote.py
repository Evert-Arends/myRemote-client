#File written by Evert Arends, all rights reserverd. First run: Thursday November 26 in 2015 around 3 PM.#
import os, os.path
import platform
import urllib2
import base64
import sys
#Check if keyfile exsitst#
hd = os.path.expanduser('~')
dir = os.path.expanduser('~/.myRemote/')
fl = os.path.expanduser('~/.myRemote/user.kb')
if not os.path.exists(dir):
    os.mkdir(os.path.join(hd, '.myRemote'))
    print 'Created dir: .myRemote'

#Url variables#
ip = 'http://programmeerbazen.nl/ip.php' #Returns IP
get = 'get.php?M=' #Returns key if positive
data= 'data.php?data=' #Inserts information
#base = 'https://baseurl.com/Stub/For/App' #Base URL, every url that needs this gets included (baseurl + var)
message = 'msg.php?M=' #Check if there is a message availible (Url var)
command = 'cmd.php?M=' #Gets the command from DB(Urls var)
register = 'reg.php?K=' #Registers inserted key(Urls var)
#!Url variables#

#Reading the key, and if it does not exists asks for a new one.
try:
    fp = open(fl)
    key = fp.read(1000) #max lines to read.
    if(not key):
        print 'Empty? please delete your .myRemote folder in your home/appdata folder.', key
        sys.exit(42)
except IOError:
    key = raw_input("Key?")
    fp = open(fl, 'w+')
    print 'empty'
    fp.write(key)
    try:
        from urllib.request import urlopen
    except ImportError:
        from  urllib2 import urlopen
    s = urlopen(base + register + key)
    print base + register + key
fp.close()
print 'succes!'
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
s = urlopen(ip)
pcName = platform.uname()[1]
osName = platform.system()
pip = s.read()
#Encoding sData into a base64 string, so I can post spaces and weird characters.
sData = base64.b64encode(key + ',' + pcName + ',' + osName + ',' + pip)
#sData = base64.b64encode(sData)
data = data + sData
print data
print base64.b64decode(data)
#Request URL with a get parameter, which makes it easier to store the data on the serverself.
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
#s = urlopen(base + data)
print base + data
