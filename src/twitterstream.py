# This file is the code used in the project.

import oauth2 as oauth
import urllib2 as urllib
import json
from sentiment import *
from load_sentiment import *

api_key = "avngLhaJFPziKYQkI4bJqobfY"
api_secret = "qqdYCAH2etbI2rOHBXmlbTk1rXNK5TGAnDXPAnEG3xSNIe4VG2"
access_token_key = "831078007-oe1TBcecaLDEQcW1Hx1mhaq2pICIb9P2mclhSGX0"
access_token_secret = "XsUa71xGSotYCxZHcflhiwvvX63zkVUecRzOa0NZbvS0F"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  print "functino called"
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)
  print "fdasfs"
  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()
  print "Fsdaf"
  proxy = urllib.ProxyHandler()
  opener = urllib.build_opener(proxy)
  urllib.install_opener(opener)
  print "FAsdfasdgfasd"
  response=urllib.urlopen(urllib.Request(url,encoded_post_data))
  #print  len(response.read())
  print "34254"


  return response

def fetchsamples():
  url = "https://stream.twitter.com/1/statuses/filter.json?locations=68,8,97,37"
  parameters = []
  print "         fdas       "
  response = twitterreq(url, "POST", parameters)
  print "fffffffffffffffffffffff"
  return response

if __name__ == '__main__':
  fetchsamples()
