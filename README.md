# vT_Gmail
Python command line script to search Gmail emails (Google Apps)

Google Developer's Console - create your app, generate the client_sercret.json file, download it, and enable the Gmail API for that client (steps here - https://developers.google.com/gmail/api/quickstart/quickstart-python)

Install Google Client Library (python) with 

easy_install --upgrade google-api-python-client
-OR-
pip install --upgrade google-api-python-client

In a directory, copy the vT_Gmail.py file and client_secret.json file.

Use it as:

python vT_Gmail.py<br />
python vT_Gmail.py -u me
python vT_Gmail.py -u me -l INBOX
python vT_Gmail.py -u me -l INBOX -ist True
python vT_Gmail.py -u me -l INBOX -ist True -m 5
python vT_Gmail.py -u me -l INBOX -ist True -m 5 -q "something interesting"

On first run, authorize the script using your Google Apps login via the browser.

usage: main.py [-h] [-u USERID] [-m MAXRESULTS] [-csf CLIENTSECRETFILE] [-d DEBUG] [-q QUERYFOR] [-l LABEL] [-i INCLUDESPAMTRASH]

vT_Gmail search tool

optional arguments:
  -h, --help            show this help message and exit
  -u USERID, --userId USERID
      User Id (email), default 'me'
  -m MAXRESULTS, --maxResults MAXRESULTS
      Maximum results, default 5
  -csf CLIENTSECRETFILE, --clientSecretFile CLIENTSECRETFILE
      Client Secret file, default clients_secret.json
  -d DEBUG, --debug DEBUG
      True | False, default False
  -q QUERYFOR, --queryFor QUERYFOR
      search for, default Gmail
  -l LABEL, --label LABEL
      Label / folder to search in, default INBOX
  -i INCLUDESPAMTRASH, --includeSpamTrash INCLUDESPAMTRASH
      Include Spam/Trash in search, default False
