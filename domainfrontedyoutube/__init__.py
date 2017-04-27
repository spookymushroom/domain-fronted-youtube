#!/usr/bin/python3
import urllib.request as ur
import urllib.parse as up
import html.parser
import os

savedir = "~/Videos"



globalheaders = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0"}
headers = {"Host":"www.youtube.com"}
headers.update(globalheaders)



def getvideoid(url):
    parsed_url = up.urlparse(url)
    if parsed_url.netloc == "youtu.be":
        return parsed_url.path.strip("/")
    elif parsed_url.netloc == "youtube.com" or parsed_url.netloc == "www.youtube.com":
        q = up.parse_qs(parsed_url.query)
        return q["v"][0]

def getmetaurl(video_id):
    return "https://www.youtube.com/get_video_info?video_id={}".format(video_id)


class FrontedURL:
    def __init__(self,url,frontingdomain="drive.google.com"):
        self.originalurl = url
        parsed_url = up.urlparse(url)
        s = parsed_url.scheme
        d = parsed_url.netloc
        p = parsed_url.path
        q = parsed_url.query
        new_url = s + "://" + frontingdomain + p + "?" + q
        self.url = new_url
        self.headers["Host"] = d
    originalurl = ""
    url = ""
    headers = {}

def openFrontedURL(fronted_url):
    global globalheaders
    headers = fronted_url.headers
    headers.update(globalheaders)
    req = ur.Request(fronted_url.url,headers=headers)
    res = ur.urlopen(req)
    return res

def unpackmetaresponse(res):
    b = res.read()
    s = b.decode("utf-8")
    j = up.parse_qs(s)
    j_stream_map = up.parse_qs(j["url_encoded_fmt_stream_map"][0])
    return j_stream_map
    


if __name__ == "__main__":
    video_url = input("Enter video url: ")

    video_id = getvideoid(video_url)
    meta_url = getmetaurl(video_id)


    fronted_url = FrontedURL(meta_url)
    res = openFrontedURL(fronted_url)

    j_stream_map = unpackmetaresponse(res)

    print(j_stream_map["url"])
    print(j_stream_map["quality"])
    print(j_stream_map["type"])



    #AUTOMATICALLY USES FIRST URL
    req2 = ur.Request(j_stream_map["url"][0],headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0","Origin":"https://www.youtube.com","Referer":video_url})

    res2 = ur.urlopen(req2)

    savedir_full = os.path.expanduser(savedir)
    filename = savedir_full+"/youtubedltmp"

    CHUNK = 16*1024
    with open(filename,"wb") as f:
        while True:
            chunk = res2.read(CHUNK)
            if not chunk: break
            f.write(chunk)



