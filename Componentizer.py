#inputFileName = input("Input name of mcfunction file: ")
inputFileName = "pick.mcfunction"
file = open(inputFileName, "r")
lines = file.readlines()

component = "["

transl = {
    "0b": "false",
    "1b": "true",
    "Damage:": "damage=",
    "RepairCost:": "repair_cost="
}

i = 0

def fixOldTags(tag):
    for key in transl:
        tag = tag.replace(key, transl[key])
    print(tag)

while i < len(lines):
    originalLine = lines[i]
    nbt = originalLine.split("{", 1)[1] #split by {, only first occurence and set to [index 1 of split strings]
    nbt = nbt.rsplit("}", 1)[0] #reverse split by {, only last occurence and set to [index 0]
    print(nbt)
    fixOldTags(nbt)
    
    i = i+1


component = component + "]"