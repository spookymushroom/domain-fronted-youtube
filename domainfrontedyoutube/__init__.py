#!/usr/bin/python3
import urllib.request as ur
import urllib.parse as up
import html.parser

req = ur.Request("https://drive.google.com/watch?v=eQVXIPVRbCU",headers={"Host":"www.youtube.com","User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0"})
res = ur.urlopen(req)
b = res.read()
s = b.decode("utf-8")


class PageParser(html.parser.HTMLParser):
    pass


#ALL THE URLS IT SPITS BACK GIVE AN ERROR 403, WILL NEED TO FIX

#j = up.parse_qs(s)
#j2 = up.parse_qs(j["url_encoded_fmt_stream_map"][0])
#print(j2["url"])

#req2 = ur.Request(j2["url"][2],headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0"})


#res2 = ur.urlopen(req2)
