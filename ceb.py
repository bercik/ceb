#!/usr/bin/python

from lib import io

import cookielib
import urllib
import urllib2
import re
import smtplib
from email.mime.text import MIMEText

if __name__ == "__main__":
    # get user info frome text file
    user_info = io.ReadPasswordsAndLogins()

#baza
    URL = 'http://planck.ftj.agh.edu.pl:8008/obieralne/Login.do'
    SEMESTER = '.*true.*' # sprawdzaj czy 'false'(zimowy) albo 'true'(letni)

#email
    SUBJECT = 'no elo'
    MESSAGE = 'baza zostala otwarta'


# Store the cookies and create an opener that will hold them
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

# Input parameters we are going to send
    payload = {
      'login': user_info['login'],
      'haslo': user_info['password'],
      'send': 'Logowanie'
      }

    data = urllib.urlencode(payload)
    req = urllib2.Request(URL, data)

    resp = urllib2.urlopen(req)
    contents = resp.read()

    semesterLine = re.search(".*selected.*", contents, re.MULTILINE).group(0)
    match = re.search(SEMESTER, semesterLine)

    if match:
        print "send mail!!!" 

    if match:
            msg = "\r\n".join([
              "From: ".join(user_info['email_address']),
              "To: ".join(user_info['email_address']),
              "Subject: ".join(SUBJECT),
              "",
              MESSAGE
              ])
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(user_info['email_address'], user_info['email_password'])
            server.sendmail(user_info['email_address'], user_info['email_address'], msg)
            server.quit()
