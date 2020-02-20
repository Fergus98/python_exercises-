def getBert(string):
    newstr=(string.lower()).split("bert")
    if len(newstr) > 2:
        return "".join(newstr[1:-1])[::-1]
    else: 
        return ""
