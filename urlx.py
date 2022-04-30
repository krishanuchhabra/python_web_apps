#!/usr/bin/env python

import urllib

httpResponse = urllib.urlopen("http://localhost")

print httpResponse.code

#will give 200

print httpResponse.read()

#gives back html page code

#dir(httpResponse) will show what commands u can use with httpResponse

print httpResponse.headers.items()

for header,value in httpResponse.headers.items():
    print header + ":" + value

print httpResponse.headers.keys()

#shows what headers the request gives

url = "http://www.securitytube.net/groups?operation=view&groupid=10"

base_url = "http://www.securitytube.net/groups"

args = { 'operation':'view', 'groupid':'10'}

encode_args = urllib.urlencode(args)

print encode_args

#doing the same thing using base_url

fp2 = urllib.urlopen(base_url + '?' +encode_args)

print fp2.code

#for post fp2=urllib.urlopen(base_url, encode_args)



