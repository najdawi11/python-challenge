import os
import csv

# Function: print a line of 20 caracteres like this "-"

def print_line():

    line = "-"
    for i in range(20):
        line = line + "-"
    return line


# Function: write the result data in a file

def print_in_file(print_Data):
    
    resulting = os.path.join("analysis", "PyPoll_result.txt")
    
    with open(resulting, "w") as f:
        f.write("\n".join(print_Data))

# Function: print the result calculation of voting data 

# Function: print the result calculation of voting data 

def print_Results(numRows,sumAmount,max_change,min_change,data):

    # build array to print on file
    print_Data = []

    change_Amount_Sum = 0

    print("Financial Analysis")
    print_Data.append("Financial Analysis")
    
    print(print_line())
    print_Data.append(print_line())

    print(f"Total Months: {str(numRows)}")
    print_Data.append(f"Total Months: {str(numRows)}")
    
    print(f"Total: ${sumAmount:.0f}")
    print_Data.append(f"Total: ${sumAmount:.0f}")

    for row in data:
        change_Amount_Sum += row    

    print(f"Average Change: : ${change_Amount_Sum/len(data):.2f}")
    print_Data.append(f"Average Change: : ${change_Amount_Sum/len(data):.2f}")

    print(f"Greatest Increase in Profits:  {max_change[0]} (${max_change[1]})")
    print_Data.append(f"Greatest Increase in Profits:  {max_change[0]} (${max_change[1]})")
    print(f"Greatest Decrease in Profits:  {min_change[0]} (${min_change[1]})")
    print_Data.append(f"Greatest Decrease in Profits:  {min_change[0]} (${min_change[1]})")

    print(print_line())
    print_Data.append(print_line())
    
    # write the results in file        
    print_in_file(print_Data)



budget_csv = os.path.join("", "Resources", "budget_data.csv")

with open(budget_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    # read the header 
    header = next(csv_reader)

    data = []
    change_Amount = []

    below_amount = 0
    max_change = []
    min_change = []
    
    rownumber = 1
    sum_total_Amount = 0

    for row in csv_reader:
        
        if rownumber == 1:

            below_amount = float(row[1])

            max_change.append(row[0]) # append date
            max_change.append(float(row[1])) # append amount

            min_change.append(row[0]) # append date
            min_change.append(float(row[1])) # append amount

            sum_total_Amount += float(row[1])

        else:
            
            change_Amount.append(float(row[1])-below_amount)
            sum_total_Amount += float(row[1])

        #greatest increase 
        if max_change[1] < float(row[1])-below_amount:
            max_change[1] = float(row[1])-below_amount # hold new amount
            max_change[0] = row[0] # hold new date

        #greatest decrease 
        if min_change[1] > float(row[1])-below_amount:
            min_change[1] = float(row[1])-below_amount # hold new amount
            min_change[0] = row[0] # hold new date

        below_amount = float(row[1])
        rownumber += 1


print_Results(rownumber-1,sum_total_Amount,max_change,min_change,change_Amount)