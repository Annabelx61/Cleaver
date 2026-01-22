import numpy as np

# Importing list of names
firstNameList = []
with open("firstnamelist.txt") as file:
    for line in file:
        stripped_line = line.strip()
        values = stripped_line.split(" ")
        for i in range(len(values)):
            firstNameList.append(values[i])

print(firstNameList)
print(len(firstNameList))

firstNameList_write = "\n".join(firstNameList) + "\n"
with open("firstnamelist.txt", "w") as file:
    file.writelines(firstNameList_write)

lastNameList = []
with open("lastnamelist.txt") as file:
    for line in file:
        stripped_line = line.strip()
        lastNameList.append(stripped_line)

print(lastNameList)
print(len(lastNameList))

def generateName():
    # Getting first name
    index = np.random.randint(0, len(firstNameList))
    firstname = firstNameList[index]

    # Getting last name
    index = np.random.randint(0, len(lastNameList))
    lastname = lastNameList[index]

    print(firstname + ' ' + lastname)

generateName()