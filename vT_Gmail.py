import httplib2

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

import argparse
import sys


#admin@presgroup.net
#scopes - https://developers.google.com/gmail/api/auth/scopes



import pprint
import sys

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

def initSA(service_account_email, service_account_pkcs12_file_path, user_email):
  """Build and returns a Gmail service object authorized with the service accounts that act on behalf of the given user.

  Args:
    user_email: The email of the user.
  Returns:
    Gmail service object.
  """
  
  f = file(service_account_pkcs12_file_path, 'rb')
  key = f.read()
  f.close()

  # Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
  # OAUTH_SCOPE='https://mail.google.com/'
  OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'
  
  credentials = SignedJwtAssertionCredentials(service_account_email, key, scope=OAUTH_SCOPE, sub=user_email)
  http = httplib2.Http()
  http = credentials.authorize(http)

  gmail_service = build('gmail', 'v1', http=http)

  return gmail_service



def init(csf):
  """Build and returns a Gmail service object authorized with the client id for a native application.

  Args:
    csf = client secret file in json format
  Returns:
    Gmail service object.
  """

  # Path to the client_secret.json file downloaded from the Developer Console
  CLIENT_SECRET_FILE = csf

  # Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
  OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'
  
  # Location of the credentials storage file
  STORAGE = Storage('gmail.storage')
  
  flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
  http = httplib2.Http()
  
  credentials = STORAGE.get()
  if credentials is None or credentials.invalid:
    credentials = run(flow, STORAGE, http=http)
  
  http = credentials.authorize(http)
  
  gmail_service = build('gmail', 'v1', http=http)

  return gmail_service

def vTgSearch(gmail_service, u, l, ist, m, q):

  #INBOX, SPAM, TRASH, UNREAD, STARRED, IMPORTANT, SENT, DRAFT, CATEGORY_PERSONAL, CATEGORY_SOCIAL, CATEGORY_PROMOTIONS, CATEGORY_UPDATES, CATEGORY_FORUMS
  #pageToken = 1
  messages = gmail_service.users().messages().list(userId=u, labelIds=l, includeSpamTrash=ist, maxResults=m, q=q).execute()
  
  if messages['resultSizeEstimate'] > 0:
    for message in messages['messages']:
      print 'Message ID: %s' % (message['id'])
      msg = gmail_service.users().messages().get(id=message['id'], userId=u, format='metadata').execute()
      from1 = to1 = subject1 = date1 = snippet1 = ''
      snippet1 = msg['snippet']
      for hdr in msg['payload']['headers']:
        if hdr['name'] == 'From':
          from1 = hdr['value']
        elif hdr['name'] == 'To':
          to1 = hdr['value']
        elif hdr['name'] == 'Subject':
          subject1 = hdr['value']
        elif hdr['name'] == 'Date':
          date1 = hdr['value']
      print 'Message\nFrom: %s\nTo: %s\nSubject: %s\nDate: %s\n%s' % (from1, to1, subject1, date1, snippet1)


if __name__ == "__main__":

  try:
    
    vT_Description = 'vT_Gmail search tool'
    vT_Epilog = 'Created by sandipshah@vthrive.com'
    
    parser = argparse.ArgumentParser(description=vT_Description, epilog=vT_Epilog)
    parser.add_argument('-u', '--userId', required=False, default='me', help='User Id (email), default \'me\'')
    parser.add_argument('-m', '--maxResults', required=False, default=5, help='Maximum results, default 5')
    parser.add_argument('-csf', '--clientSecretFile', required=False, default='client_secret.json', help='Client Secret file, default clients_secret.json')
    parser.add_argument('-d', '--debug', required=False, default=False, help='True | False, default False')
    parser.add_argument('-q', '--queryFor', required=False, default='Gmail', help='search for, default Gmail')
    parser.add_argument('-l', '--label', required=False, default='INBOX', help='Label / folder to search in, default INBOX')
    parser.add_argument('-i', '--includeSpamTrash', required=False, default=False, help='Include Spam/Trash in search, default False')
    parser.add_argument('-sa', '--useServiceAccount', required=False, default=False, help='Use Service Account')
    parser.add_argument('-sae', '--SAEmail', required=False, help='Service Account Email address')
    parser.add_argument('-k', '--key', required=False, default='key.p12', help='PKCS12 Key File Path, default key.p12')
    
    vT_args = parser.parse_args()
    
  except:
    parser.print_help()
    sys.exit(2)

  if isinstance(vT_args.debug, basestring):
    if vT_args.debug.capitalize() == 'True':
      vT_args.debug = True
      httplib2.debuglevel = 4
    else:
      vT_args.debug = False
      
  if isinstance(vT_args.label, basestring):
    vT_args.label = vT_args.label.upper()
  
  if isinstance(vT_args.useServiceAccount, basestring):
    vT_args.useServiceAccount = vT_args.useServiceAccount.upper()


  if vT_args.useServiceAccount:
    gmail_service = initSA(service_account_email = vT_args.SAEmail, service_account_pkcs12_file_path = vT_args.key, user_email = vT_args.userId)
  else:
    gmail_service = init(csf=vT_args.clientSecretFile)

  vTgSearch(gmail_service=gmail_service, u = vT_args.userId, l = vT_args.label, ist = vT_args.includeSpamTrash, m = vT_args.maxResults, q = vT_args.queryFor)
  
  print('---Done---')
