#!/usr/bin/python3

import __init__
import sys

print("Domain fronted youtube, a circumvention tool for accessing youtube.com")
print("Copyright (C) 2017 Michael Korotkov")
print("This program comes with ABSOLUTELY NO WARRANTY, to the extent permitted by applicable law.")
print()
print("Type h for help")

while True:
    u = input("> ")
    if u == "q": sys.exit(0)
    elif u == "h":
        print("Commands: ")
        print("\tq: quit\n\th: display this help menu\n\tl: license information\n\ts <query>: search youtube\n\td <yt-link>: download youtube video to ~/Videos/youtubedltmp\n\tdebugoff: turn off verbose debug\n\tdebugon: turn on verbose debug\n\tld: run the interactive legacy downloader")
    elif u == "l":
        print("This program is licensed under GNU General Public License v3. \
More information can be found in the LICENSE file located in this program's root directory or at https://www.gnu.org/licenses/gpl-3.0.en.html")
    elif u.partition(" ")[0] == "s":
        q = u.partition(" ")[2]
        if q:
            results = __init__.searchyoutube(q)
            for r in results:
                if r["is_video"]:
                    print(r["title"] + " (https://www.youtube.com" + r["url"] + ")")
                    print(" by " + r["channel_name"] + " (https://www.youtube.com" + r["channel_url"] + ")\n")
        else: print("Usage: s <query>")
    elif u.partition(" ")[0] == "d":
        link = u.partition(" ")[2]
        if link: __init__.downloadfromlink(link)
        else: print("Usage: d <youtube-link>")
    elif u == "debugoff":
        __init__.debug = False
    elif u == "debugon":
        __init__.debug = True
    elif u == "ld":
        __init__.legacydownloader()

