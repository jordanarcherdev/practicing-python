import sys

try:
    File = open("myfile.txt") ,
except IOError as e:
    print("Error opening file!\r\n" + "Error Text: {0}".format(e.strerror))
else:
    print("File opened as expected.")
    File.close();
