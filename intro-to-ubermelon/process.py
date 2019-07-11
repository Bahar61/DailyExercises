log_file = open("um-server-01.txt") #opening certain file from a different server


def sales_reports(log_file):
    for line in log_file: #loops through each line of log_file
        line = line.rstrip() #assigns method .rstrip() to line 
        day = line[0:3]
        if day == "Mon": # gives condition that if the day is equal to Mon then print the line
            print(line)


sales_reports(log_file) #calls the function
