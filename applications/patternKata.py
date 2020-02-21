def pattern(n):
    outputStr = ""
    if n < 1:
        return ""
    else:
        for i in range(1, n+1):
            for j in range(i):
                outputStr += str(i)
            outputStr += "\n"
        return outputStr[:-1]
