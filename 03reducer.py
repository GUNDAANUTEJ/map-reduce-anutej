import sys

thisKey = ""
thisValue = 0

for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    country,cumulative_total_cases = datalist

    if country != thisKey:   # we've moved to another key
      if thisKey:
        # output the previous key-summaryvalue result
        print(thisKey,'\t',thisValue)

      # start over for each new key
      thisKey = country
      thisValue = 0
  
    # apply the aggregation function
    thisValue  = thisValue + 1

# output the final key-summaryvalue result outside the loop
print(thisKey,'\t',thisValue)