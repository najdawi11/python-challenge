import os
import csv



#print a line of 20
def print_line():

    line = "-"
    for i in range(20):
        line = line + "-"
    return line


#write results data in a file

def print_in_file(print_Data):
    
    resulting = os.path.join("", "analysis", "election_result.txt")
    with open(resulting, "w") as f:
        f.write("\n".join(print_Data))


#print the result for voting
def print_Results(numVotes,winner_Name,data):

    # array to print file
    print_Data = []

    print("Election Results")
    print_Data.append("Election Results")

    print(print_line())
    print_Data.append(print_line())

    print(f"Total Votes : "+str(numVotes))
    print_Data.append(f"Total Votes : "+str(numVotes))

    print(print_line())
    print_Data.append(print_line())
    
    for item in data:
        print(f"{item[1]}: %{((int(item[2])/numVotes)*100):.3f} ({item[2]})")
        print_Data.append(f"{item[1]}: %{((int(item[2])/numVotes)*100):.3f} ({item[2]})")
    

    print(print_line())
    print_Data.append(print_line())

    print(f"Winner : "+winner_Name)
    print_Data.append(f"Winner : "+winner_Name)
    
    print(print_line())
    print_Data.append(print_line())

       
    print_in_file(print_Data)



election_csv = os.path.join("", "Resources", "election_data.csv")

with open(election_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

#read the header 
    header = next(csv_reader)

    
#variables that hold rows in input file
    index = []
    i_BallotID = []
    i_County = []
    i_Candidate = []

    
    o_Index = []
    o_Candidate = []
    o_NumVote = []

     
    f_Index = []
    f_Candidate = []
    f_NumVote = []


    
    
    rownumber = 1

    

    for row in csv_reader:
        
        index.append(rownumber)
        i_BallotID.append(row[0])
        i_County.append(row[1])
        i_Candidate.append(row[2])

        rownumber += 1

print("num de rows "+str(rownumber))


index.append(rownumber)
i_BallotID.append("End")
i_County.append("End")
i_Candidate.append(0)
#read the input file
rownumber += 1


    

#hold rows of first result
curr_o_index = 1
curr_Candidate = i_Candidate[1]    
curr_votes = 1

# change the candidate
for i in range(1,rownumber):

   

    if (i_County[i] =="End"):

        break

    if (curr_Candidate != i_Candidate[i+1]): 

        o_Index.append(curr_o_index)
        o_Candidate.append(curr_Candidate)
        curr_votes += 1
        o_NumVote.append(curr_votes)
        curr_o_index += 1

        curr_Candidate = i_Candidate[i+1]
        curr_votes = 0

    else: 

        curr_votes += 1       

    
o_Index.append(curr_o_index)
o_Candidate.append("End")
o_NumVote.append(0)

curr_o_index += 1

#holds the index of the most voting candidate
Winner_name = "" 
Winner_votes = 0 

found_Cand_Index = 1

for i in range(0,curr_o_index+1):

    found = False

    if i==0:

        f_Index.append(i)
        f_Candidate.append(o_Candidate[i])
        f_NumVote.append(int(o_NumVote[i]))
        Winner_name = o_Candidate[i]
        Winner_votes = o_NumVote[i]

    elif o_Candidate[i]=="End":

        break

    else:

        for j in range(0,found_Cand_Index):

           

            if o_Candidate[i]==f_Candidate[j]:

                f_NumVote[j] += o_NumVote[i]
                found = True

                
                if f_NumVote[j]> Winner_votes:
                    Winner_votes = f_NumVote[j]
                    Winner_name = o_Candidate[i]
                break

        if found==False: # did not find the candidate
                
            found_Cand_Index += 1    
            f_Index.append(found_Cand_Index)
            f_Candidate.append(o_Candidate[i])
            f_NumVote.append(o_NumVote[i])
            
            # this Candidate has more votes? 
            if o_NumVote[i]> Winner_votes:
                Winner_votes = o_NumVote[i]
                Winner_name = o_Candidate[i]   



#show results and create file 

data_list_f = zip(f_Index, f_Candidate, f_NumVote)

print_Results(rownumber-2,Winner_name,data_list_f)
