f = open("file1", "r")
f.write('"work is worship"')   # ERROR because file opened in read-mode
f.close()
