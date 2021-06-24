text = "this is a long name"

label = ""


for item in text.split():
    label += item
    label += "\n"

print(label)