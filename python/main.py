# Python program to handle command line arguments 

import sys

# Get command line arguments 
inputs = sys.argv

# Initialize output string 
outputs = '"'

# Traverse command line arguments 
for i in range(1, len(inputs)): 
   
    # If current argument contains space, add double 
    # quotes and comma to output string 
    if ' ' in inputs[i]: 
        outputs += ('", "') 
   
    # Else simply add the argument to output string 
    else: 
        outputs += inputs[i] 
  
# Add ending double quotes 
outputs += '"'

# Print the output string 
print(outputs)