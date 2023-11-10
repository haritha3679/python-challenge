# budget_data.csv has several years profit and loss budget_data in mmm-yy date format
# Read the data from .csv and put in array. 
# Sort it. This I have added eventhough the data is given in chronological just to make sure even if data is not given in chronological order the change works.
# Find Total months, total value ,average change,Greatest change in  profit and Loss . 
import os
import csv
from datetime import datetime
def parse_date(date_str):
    return datetime.strptime(date_str,"%b-%y")

#directory_path = "C:\haritha\python-challenge\pybank\Resources"
file_name = "budget_data.csv"
output_fname = "financial_analysis.txt"
total = 0 
sum_change = 0
max_date = "Jan-02"
min_date = "Jan-02"
mon_count = 1

csvpath = os.path.join(os.getcwd(),"Resources",file_name)
outpath = os.path.join(os.path.curdir,output_fname)
print(csvpath)
if os.path.exists(csvpath):
    print(f"file path:{csvpath}")
else:
    print(f"File not found:{csvpath}")

with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that holds contents 
     
     csvreader = csv.DictReader(csvfile,delimiter=",")
     formatted_data = []
     for row in csvreader:
         
         formatted_data.append({'Date':parse_date( row['Date']), 
                                'Value': float(row['Profit/Losses'])})
     
#I sorted the data as analysis of the budget changes would be time based but i see the result given is not time based and asis
     sortedlist = sorted(formatted_data,key=lambda row: row["Date"])
     max_value = 0
     min_value = 0
     avg_change = 0
     avg_change1 = 0
     
     day_before_value = 0
     len = 0
    
     for row in sortedlist:
       
       value = float(row['Value'])
       
       date_str = row['Date'] 
       total = total + value
       len = len + 1
       if len > 1:
        if date_str1 is not date_str:
            mon_count = mon_count + 1

       
       if day_before_value is not None:
            
            change =  value  - day_before_value
            if len > 1:
                sum_change = change + sum_change
            
            
            if max_value is None or change > max_value:
                max_value = change
                max_date = date_str
               
            if change < min_value:
                min_value = change
                min_date = date_str
               
        
            
            day_before_value = value
            date_str1 = date_str
#Close the file    
csvfile.close()
avg_change = sum_change / (len - 1)   
# Write all the data  - have to format before submission and use some functions  
output_data = []
output_data.append("Financial Analysis \n")
index = 1
output_data.insert(index + 1,"----------------------------------------\n")
print("Financial Analysis")
print("----------------------------------------")

print(f"Total Months: {mon_count:.0f}")
output_data.append(f"Total Months: {mon_count:.0f}\n")
total = int(total)
print(f"Total:  ${total}")
index = index + 1
output_data.append(f"Total:  ${total}\n")
print(f"Average change: ${avg_change:.2f}")
output_data.append(f"Average change: ${avg_change:.2f}\n")
format_date =  max_date.strftime('%b-%y')   
print(f"Greatest Increase in Profits: {format_date} (${max_value:.0f})")
output_data.append(f"Greatest Increase in Profits: {format_date} (${max_value:.0f})\n")

format_date =  min_date.strftime('%b-%y')   
print(f"Greatest Decrease in Profits:{format_date} (${min_value:.0F})")
output_data.append(f"Greatest Decrease in Profits:{format_date} (${min_value:.0F})")

with open(outpath,'w') as file:
    file.writelines(output_data)