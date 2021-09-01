# input your command-line args here
inputs = "-a -b -c -examples"
outputs = "\""
for i in inputs:
    if i == ' ':
        outputs += ("\", \"")
    else:
        outputs += (i)
outputs += "\""
print(outputs)