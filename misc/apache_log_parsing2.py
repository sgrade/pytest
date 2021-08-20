FILE = "apache_log_parsing2.txt"

output = dict()

with open(FILE) as file:
    lines = file.read().splitlines()
    
    # Processing the file
    for line in lines:
        
        _line = line.split(" - - ")
        
        # Extracting subnet as a string
        subnet = _line[0].split('.')[0:2]
        subnet.append('0')
        subnet.append('0')
        subnet = '.'.join(subnet)

        
        # Extracting month
        month = _line[1].strip().split()[0][4:7]
        
        # Filling the output
        
        # Is month in output
        if month not in output.keys():
            output[month] = dict()
            
        # Is subnet in output[month]
        if subnet not in output[month].keys():
            output[month][subnet] = 0
        
        output[month][subnet] += 1
        
# Printing the output

# Since Python 3.8. dicts remember order
# [TODO] Check Python version in prod
last_three_months = list(output.keys())[-3:]

for month in last_three_months:
    lst = list()
    for subnet, cntr in output[month].items():
        lst.append("  " + str(cntr) + " - " + subnet)
    
    print(month)
    print('\n'.join(lst))
