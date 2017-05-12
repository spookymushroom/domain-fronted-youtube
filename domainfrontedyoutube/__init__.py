#!/usr/bin/python3
import urllib.request as ur
import urllib.parse as up
import html.parser
import os

savedir = "~/Videos"

debug = True

globalheaders = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0"}


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

def downloadvideo(j_stream_map,video_id,savedir,CHUNK=16*1024):
    '''Video id required to set Referrer header'''
    global debug
    video_url = "https://www.youtube.com/watch?v=" + video_id
    download_url = j_stream_map["url"][0].split(";")[0]
    if debug: 
        print("Opening:",download_url)
        print("Setting referer to:",video_url)
    req = ur.Request(download_url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0","Origin":"https://www.youtube.com","Referer":video_url})
    res = ur.urlopen(req)
    savedir_full = os.path.expanduser(savedir)
    filename = savedir_full+"/youtubedltmp"
    
    with open(filename,"wb") as f:
        while True:
            chunk = res.read(CHUNK)
            if not chunk: break
            f.write(chunk)



if __name__ == "__main__":
    video_url_input = input("Enter video url: ")

    video_id = getvideoid(video_url_input)
    meta_url = getmetaurl(video_id)


    fronted_url = FrontedURL(meta_url)
    res = openFrontedURL(fronted_url)

    j_stream_map = unpackmetaresponse(res)

#    print(j_stream_map["url"])
#    print(j_stream_map["quality"])
#    print(j_stream_map["type"])

    downloadvideo(j_stream_map,video_id,savedir)



