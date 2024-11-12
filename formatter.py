with open("preregistrations.txt", "r") as f:
    data = f.readlines()

new = ""

for line in data:
    new += '{ x: "' + line.split("|")[0] + '", y: ' + line.split("|")[1].strip() + ' },\n'

print(new)
