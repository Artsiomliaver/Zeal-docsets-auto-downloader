import re

f = open("urlist.json", "r")
mylines = f.readlines()

found = []
for line in mylines:
    try:

        val = re.search("(?P<url>https?://[^\s]+)", line).group("url")
        url = val.replace('"},', '')
        with open("out.txt", "a", encoding="utf8") as myfile:
            myfile.write(url + "\n")
        print(val)
    except:
        pass