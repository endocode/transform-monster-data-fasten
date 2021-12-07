#import sys
import re

class transformData:

    inputFile = input("Enter the name of the input file: ") # sys.argv[1]
    outputFile = input("Enter the name of the output file: ") # sys.argv[2]


    with open(inputFile) as f:

        for messages in f:
            m = re.search(r"\|.*", messages)
            print(m.group(0))
            m = m.group(0)

            projectName = re.search(r"((?<=artifactId\":\")).*(?=\",\"version)", messages)
            print(projectName.group(0))
            projectName = projectName.group(0)

            projectVersion = re.search(r"((?<=version\":\")).*?(?=\")", messages)
            print(projectVersion.group(0))
            projectVersion =  projectVersion.group(0)

            output = open(outputFile, "a")
            output.write(str(projectName) + ":" + str(projectVersion) + str(m) + "\n")
            output.close()

    f.close()
