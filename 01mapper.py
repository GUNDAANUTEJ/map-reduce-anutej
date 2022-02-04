import sys

for line in sys.stdin:  
    dataList = line.strip().split(",") 
    
    if (len(dataList) == 6) :
        country,cumulative_total_cases,daily_new_cases,active_cases,cumulative_total_deaths,daily_new_deaths = dataList 
        print (country,"\t", cumulative_total_cases)
