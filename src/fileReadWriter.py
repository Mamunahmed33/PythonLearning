fw = open('sample.txt', 'w')

fw.write('What a easy langauge python is!!!\n')
fw.write('I have started to love python')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read();
print(text)
