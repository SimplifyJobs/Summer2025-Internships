# Convert README.md list to csv
# tested using Python 3.7.6

InputFileName = "README.md"
OutputFileName = "table.csv"
Seperator = ","

lines = open(InputFileName,"r").readlines()
outputfile = open(OutputFileName, "w")
outputfile.write("Name" + Seperator + "Link" + Seperator + "Notes\n")

# delete unneeded lines
for _ in range(len(lines)):
    if lines[0] == "|---|---|-------------|\n":
        del lines[0]
        break
    else:
        del lines[0]

# generate table
for line in lines:
    l = line.split('|')
    
    if len(l) > 1:
        notes = "\"" + l[3] + "\""
        company = l[1].split('](') 
        name = company[0][1:]
        link = company[1][0:-1]
        
        outputfile.write(name + Seperator + link + Seperator + notes + "\n")
