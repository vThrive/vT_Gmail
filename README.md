# vT_Gmail
Python command line script to search Gmail emails (Google Apps)

Google Developer's Console - create your app, generate the client_sercret.json file, download it, and enable the Gmail API for that client (steps here - https://developers.google.com/gmail/api/quickstart/quickstart-python)

Install Google Client Library (python) with 

easy_install --upgrade google-api-python-client
-OR-
pip install --upgrade google-api-python-client

In a directory, copy the vT_Gmail.py file and client_secret.json file.

Use it as:

Note that here "l" is for "label", it is not "I"

python vT_Gmail.py<br />
python vT_Gmail.py -u me<br />
python vT_Gmail.py -u me -l INBOX <br />
python vT_Gmail.py -u me -l INBOX -ist True<br />
python vT_Gmail.py -u me -l INBOX -ist True -m 5<br />
python vT_Gmail.py -u me -l INBOX -ist True -m 5 -q "something interesting"<br />

On first run, authorize the script using your Google Apps login via the browser.

usage: main.py [-h] [-u USERID] [-m MAXRESULTS] [-csf CLIENTSECRETFILE] [-d DEBUG] [-q QUERYFOR] [-l LABEL] [-i INCLUDESPAMTRASH]

vT_Gmail search tool

optional arguments:<br />
  -h, --help            show this help message and exit<br />
  -u USERID, --userId USERID<br />
      User Id (email), default 'me'<br />
  -m MAXRESULTS, --maxResults MAXRESULTS<br />
      Maximum results, default 5<br />
  -csf CLIENTSECRETFILE, --clientSecretFile CLIENTSECRETFILE<br />
      Client Secret file, default clients_secret.json<br />
  -d DEBUG, --debug DEBUG<br />
      True | False, default False<br />
  -q QUERYFOR, --queryFor QUERYFOR<br />
      search for, default Gmail<br />
  -l LABEL, --label LABEL<br />
      Label / folder to search in, default INBOX<br />
  -i INCLUDESPAMTRASH, --includeSpamTrash INCLUDESPAMTRASH<br />
      Include Spam/Trash in search, default False<br />
