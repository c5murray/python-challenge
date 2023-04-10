import csv

csvpath = "Resources/budget_data.csv"

# Reading in the file.

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    Month = []
    profitLoss = []
    profitLossCahnge = []
    totalProfitLoss = 0
    maxProfitLossChange = 0
    minProfitLossChange = 0
    maxProfitLossMonth = ' '
    minProfitLossMonth = ' '
    
# Each row will append the local list to include the month, Profit/Loss, and the Total Profit/Loss
  for row in csvreader:
    Month.append(row[0])
    profitLoss.append(float(row[1]))
    totalProfitLoss += float(row[1])
    
# The average change in Profit/loss
  averageProfitLossChange = round(
    sum(profitLossChange) / len(profitLossChange), 2)
  
# Print results
print("Financial Analysis")
print("-------------------")
print("Total Months: " + str(len(Month)))
print("Total Revenue: " + '${:,.2f}'.format(averageProfitLossChange))
print("Average Revenue Change: " + '${:,.2f}'.format(averageProfitLossChange))
print("Greatest Increase in Profits: " +str(minProfitLossMonth) +
      " " + '${:,.2f}'.format(minProfitLossChange))

# Provide output for pybank_results file
output = "pybank_results.txt"
    file.write("Financial Analysis\n")
    file.write("-----------------\n")
    file.write("Total Months: " + strg(len(Month))+"\n")
    file.write("Total Revenue: " + '${:,.2f}'.format(totalProfitLoss)+"\n")
    file.write("Average Revenue Change: " + '${:,.2f}'.format(averageProfitLossChange)+"\n")
    file.write("Greatest Increase in Profits: " + str(maxProfitLossMonth) + " " + '${:,.2f}'.format(maxProfitLossChange)+"\n")
    file.write("Greatest Decrease in Profits: " + str(minProfitLossMonth) + " " + '${:,.2f}'.format(minProfitLossChange)+"\n")
