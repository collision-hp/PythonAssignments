def validurl(url):
    if url.startswith("https://") or url.startswith("http://"):
        if url.endswith(".com"):
            return True
        else:
            return False
    else:
        return False

url="https://youtube.com"
print(validurl(url))