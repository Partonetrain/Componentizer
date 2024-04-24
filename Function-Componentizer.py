#inputFileName = input("Input name of mcfunction file: ")
inputFileName = "pick.mcfunction"
file = open(inputFileName, "r")
lines = file.readlines()

component = "["

transl = { #1-to-1 translations. Higher entries will be translated first!
    "Unbreakable:1b": "unbreakable={}",
    "Charged:1b": "",

    "Damage:": "damage=",
    "RepairCost:": "repair_cost=",
    "map:": "map=",
    "CustomModelData:": "custom_model_data=",


    "0b": "false",
    "1b": "true"
}

arrayTransl = { #the names of array tags that will be translated, the actual content of them will need to be reformatted
    "Enchantments:": "enchantments="
}

i = 0

def fixOldTags(tag):
    for key in transl:
        tag = tag.replace(key, transl[key])
    
    #call more complex translations here
    return tag
    

while i < len(lines):
    originalLine = lines[i]
    nbt = originalLine.split("{", 1)[1] #split by {, only first occurence and set to [index 1 of split strings]
    nbt = nbt.rsplit("}", 1)[0] #reverse split by {, only last occurence and set to [index 0]
    print(nbt)
    component = component + fixOldTags(nbt)
    
    i = i+1


component = component + "]"