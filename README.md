
# Domain Fronted Youtube

Basic circumvention tool for searching and downloading from youtube, should \*.googlevideo.com and drive.google.com be unblocked. 
It can be used to bypass both tls inspection and outright blocks of the youtube domain by sending requests to 
the fronting domain (in this case drive.google.com) with the "Host: www.youtube.com" header. 
The video downloads themselves are left unobscured, as google does not support fronting for their ephemeral video 
links.

It currently supports limited search functionality and the ability to download videos given the youtube link.

## Usage:

This program can be run in interactive mode using:

```
  python3 domainfrontedyoutube/__main__.py
```

Or used as a module with:

```python
  import domainfrontedyoutube
  domainfrontedyoutube.downloadfromlink(link)
```

In interactive mode, video search is done with:

```
    s <query>
```

When using the script as a module, video (and channel) search is done with:

```python
  domainfrontedyoutube.searchyoutube(query)
```

The old interactive prompt is still accessible with: 

```
python3 domainfrontedyoutube/__init__.py
```

But it is now also accessible via the `ld` command in interactive mode.
