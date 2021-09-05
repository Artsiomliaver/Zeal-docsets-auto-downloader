import sys
import json
import os.path
from urllib.request import urlretrieve
import wget

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize:  # near the end
            sys.stderr.write("\n")
    else:  # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))


with open("urlist.json", "r") as docset_json:
    docset_list = json.load(docset_json)

    for docset in docset_list:
        docset_name = "%s.tgz" % docset["name"]
        docset_filepath = os.path.join("official_docsets", docset_name)

        sys.stderr.write("Downloading docset %s in %s \n" % (docset_name, docset_filepath))
        # urlretrieve(docset["url"], docset_filepath, reporthook)
        wget.download(docset["url"], docset_filepath)
