#!/usr/bin/python3
from urllib.request import FancyURLopener
import re


email = '' # @gmail.com can be left out
password  = ''
url = 'https://%s:%s@mail.google.com/mail/feed/atom' % (email, password)
opener = FancyURLopener()
page = opener.open(url)

contents = page.read().decode('utf-8')

ifrom = contents.index('<fullcount>') + 11
ito   = contents.index('</fullcount>')
titles = contents.split('<title>')
fullcount = contents[ifrom:ito]
print(fullcount + ' new messages\n')
for mess in titles[2:]:
    mess = (re.sub(r'(<modified>)[\w|\-|:]*', '', mess))
    mess = (re.sub(r'\<[^>]*\>(tag:)*', ' ', mess))
    mess =(re.sub(r'(gmail.google.com,2004:)\d*', '', mess))
    mess = (re.sub(r'\&[^&]*\;','', mess))
    print(mess[:45])

page.close()
