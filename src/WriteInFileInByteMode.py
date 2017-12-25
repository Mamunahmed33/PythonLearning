fw = open("C:\\Users\\User\\Desktop\\a.txt", "w")
newline = "\n\n\n Hello"
fw.write(newline)
fw.close()

fw = open("C:\\Users\\User\\Desktop\\b.txt", "wb")
newline = "\n\n\n Hello".encode("utf-8")
fw.write(newline)
fw.close()
