print("Hello, world!")

outputFile = open("output.txt", "w")
outputFile.write(str(outputFile))
outputFile.close()

f = open('output.txt', 'r')
output = f.read().strip('][').split(', ')
outputFile = open("outputFromtextFile.txt", "w")
outputFile.write(outputFile)