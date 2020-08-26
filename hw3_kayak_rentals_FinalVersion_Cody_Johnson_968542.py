# Cody Johnson (968542)

# Kayak Rentals, Homework 3 on OO-python
# 
# This homework is 210 points, 30 points each for 7 problems.
# It isn't due until Friday of week 7 (almost 3 weeks from
# assignment date Mon of week 5, 5/4/20).
#
# THERE WILL BE SOME CLASS TIME ALLOTTED for us to help one
# another with these problems. But be ready to show your
# screen and the code you've already produced.

'''
You have been contracted by the Lake Shore Renters to analyze
their rental data and help them optimize their business.

They rent Kayaks out of three shops to a set of customers.
The kayaks, customers, rentals and word tag data are in 
four text tab-delimited files.

Use python to parse these data. Write classes for Kayak,
Customer, and Rental. 

When a kayak is rented the staff members often add word tags
to the rental record, describing the customer experience. Ie
did the customer seem bored or did they damage the boat? 
Create some kind of data structure for the word tags so you
can work with them. Objects feel too heavy for this task,
perhaps just a dictionary with key=word, value=score will
suffice. Positive scores are desirable traits in customers.
'''

import os
import pandas as pd # in using miniconda with pandas to compile and run code inside Visual Studio Code
from enum import Enum
import re

filePath = str()
filePath = 'C:/Users/2cody/Desktop/Data Science/HW3/' # <---------------SET THIS TO YOUR FILE PATH SO HALF MY CODE DOESNT BREAK

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



cls()
#tags.columns = ["note_keyword", "value_score"]

# To get you started - this reads the Tags.txt file
#infile = 'Tags.txt'
#first = True
'''with open(infile, 'rt') as fin:
    for line in fin:
        if first:
            first = False
            print("Header is: " + line, end='')
        else:
            data = line.rstrip().split('\t') # split on tab character
            print(f'This record has: {data[0]}, {data[1]}')
print('...done.')
'''


# 0 - Parse the files and create objects
'''
Read in the text tab-delimited files and instantiate
objects in your classes. You might store the objects
in global-scope variables or instantiate a single
LakeShoreRenters object and store all data in it.
'''

# Below I read each file into a panda dataframe
tags = pd.read_csv(str(filePath) + 'Tags.txt', sep="\t", header=None)
customers = pd.read_csv(str(filePath) + 'Customer.txt', sep="\t", header=None)
kayaks = pd.read_csv(str(filePath) + 'Kayaks.txt', sep="\t", header=None)
rentals = pd.read_csv(str(filePath) + 'Rentals.txt', sep="\t", header=None)


# Uncomment this code to see data I have stored in each of the variables.
'''
print("Tags:\n")
print(tags)
print("\nCustomers:\n")
print(customers)
print("\nKayaks:\n")
print(kayaks)
print("\nRentals:\n")
print(rentals)
'''

# 1 - What is the total revenue from these rentals?
'''
Each Kayak rental has a $10 cost just to take the boat.
Then, there is also a charge per hour. The Kayak dataset
shows the weekday rate in dollars per hour (without a $
to make it easier to parse). Rentals on Sat and Sun are
always 20% higher hourly rate than weekday rate because 
demand is higher. (It is still a fixed $10 up front for
taking the boat out).

Calculate the total revenue from all rentals.
'''


def getRate(rentalID):
    for x in range(1, len(kayaks[0])):
        if (int(rentalID) == int(kayaks[0][x])):
            rentalRate = kayaks[2][x] # searches kayak dataframe for a matching key provided from rental dataframe, if match, get rate
            return rentalRate
    input("There was no rental rate for provided ID, this shouldnt happen...") # if here no value was found during loop
    return -1


kayakProfit = float()
totalProfit = float()

def calcCost(rate, dayNam, duration): # i am assuming the rent day is same for number of days, example, if day is Sunday, then for however many days 
    if((str(dayNam) == "Sat") or (str(dayNam) == "Sun")): #if sat or sun
        rate += 20 # add 20%, i am assuming rate is percentage as is, not that i need to move the decimal 2 spaces over, that would seem too small of rate
    #print("Rate: " + str(rate) + " Duration: " + str(duration))
    dayCost = (rate * duration) + 10 # cost for days rental is rate * the duration + the upfront $10
    return dayCost

for x in range(1, len(rentals[0])): # prints each kayak with their total earned profit
    kayakRate = getRate(rentals[0][x]) #sends rental ID into functions to get rate
    kayakProfit = calcCost(float(kayakRate), str(rentals[3][x]), float(rentals[4][x]))
    #print("Kayak " + kayaks[0][x] + ": $" + str(kayakProfit)) # I was originally going to show this, since I need it for future question I will print answer there instead
    totalProfit += kayakProfit

print("\nTotal profit: $" + str("{:,}".format(round(totalProfit,2))))
#print(rentals)
#print("\nTest grab rental rate, ID: " + rentals[0][3] + " Rate: " + str(getRate(rentals[0][3])))
input("\nContinue to next question?")
cls()


# 2 - What is the total revenue for each shop?
'''
Using python, report a table of shops and their total 
revenue. Then, generate a barplot() in R and screenshot it 
into a report.
'''
#last code i got profit per kayak, this time i need profit per shop
#this time ill add an if statement to check if kayak[1][x] == specific location, save profit in that var
#------------------do weekend extra bonus
class Shop(Enum):
    north = 0
    west = 1
    east = 2

def calcCost_V2(rate, dayNam, duration): # i am assuming the rent day is same for number of days, example, if day is Sunday, then for however many days 
    if((str(dayNam) == "Sat") or (str(dayNam) == "Sun")): #if sat or sun
        rate += 20 # add 20%, i am assuming rate is percentage as is, not that i need to move the decimal 2 spaces over, that would seem too small of rate
    #print("Rate: " + str(rate) + " Duration: " + str(duration) + " Location: " + str(location))
    dayCost = (rate * duration) + 10 # cost for days rental is rate * the duration + the upfront $10
    return dayCost

shopProfit = [0,0,0]

for x in range(1, len(rentals[0])): #loop list of rentals
    for y in range(1, len(kayaks[0])):#loop across list of kayaks
        if(kayaks[0][y] == rentals[0][x]):#if kayak id matches id of rental do info and store info in that location
            kayakRate = getRate(rentals[0][x]) #sends rental ID into functions to get rate
            kayakProfit = calcCost_V2(float(kayakRate), str(rentals[3][x]), float(rentals[4][x]))
            location = kayaks[1][y]
            shopProfit[Shop[location].value] += kayakProfit
    
print()
shopList = list()
shopProfitList = list()
for x in range(len(Shop)):
    print("Shop " + str(Shop(x).name) + " profits: $" + str(round(shopProfit[x],2)) + "\n")
    shopList.append(Shop(x).name)
    shopProfitList.append(round(shopProfit[x],2))

shopRevenue = pd.DataFrame({'shop_name' : shopList, 'shop_revenue' : shopProfitList})
#print(kayakRevenue) # <---------this is to test data going to be exported
shopRevenue.to_csv(str(filePath) + 'shopRevenue.csv', index=False, encoding='utf-8')
print("\nData Exported.\nBarplot is named 'shop_rev.jpeg'\n")
# R code for generating shop_rev.jpeg below
# shopRevenue <- read.csv(file="shopRevenue.csv")
# ggplot(shopRevenue, aes(x=shop_name, y=shop_revenue)) + geom_bar(stat="identity")
input("\nContinue to next question?")
cls()


# 3 - What is the total revenue for each kayak?
'''
Using python, generate an outfile with two columns:
kayak_id
total_revenue

Next, load this into R and generate a barplot. Screenshot
that into your report.
'''


# I accidentally did this in question #1, so thats cool!
id_List = list()
profit_List = list()

for x in range(1, len(kayaks[0])):
    id_List.append(x)
for x in range(1, len(kayaks[0])):
    profit_List.append(0)

for x in range(1, len(rentals[0])): # loops over list of rentals going line by line till at end
    for y in range(1, len(kayaks[0])):#each line on rentals list we want to loop kayaks and find associated kayak for rental
        if(kayaks[0][y] == rentals[0][x]):#if kayak id matches id of rental do info and store info in that location
            kayakRate = getRate(rentals[0][x]) #sends rental ID into functions to get rate
            kayakProfit = calcCost(float(kayakRate), str(rentals[3][x]), float(rentals[4][x]))
            profit_List[int(kayaks[0][y])-1] += round(kayakProfit,2)

kayakRevenue = pd.DataFrame({'kayak_id' : id_List, 'total_revenue' : profit_List})
#print(kayakRevenue) # <---------this is to test data going to be exported
kayakRevenue.to_csv(str(filePath) + 'kayakRevenue.csv', index=False, encoding='utf-8')
print("\nData Exported.\nBarplot is named 'kayak_rev.jpeg'\n")
# R code for generating kayak_rev.jpeg below
# kayakRevenue <- read.csv(file="kayakRevenue.csv")
# ggplot(kayakRevenue, aes(x=kayak_id, y=total_revenue, fill=kayak_id)) + geom_bar(stat="identity")
input("\nContinue to next question?")

cls()

# 4 - Customer data
'''
For each customer calculate the number of times they
have rented, the kayak ID they rented most times, and
the total number of hours they have rented all kayaks.

Write these data to an outfile "customer_report.txt"
--->I have additonal data I am writting out, its easy to change I just though a report would likely have a persons full name
'''


kayakCount = list() # index is kayakID, value stored is number of times it was rented by a person
customerID = list()
customerName = list()
favKayak = list()
totalHrs = list()

def emptyKayakCount():
    for x in range(len(kayakCount)):
        kayakCount[x] = 0

for x in range(1,len(kayaks)):
        kayakCount.append(0)

for x in range(1,len(customers)):
    customerID.append(customers[0][x])
    customerName.append(str(customers[1][x]) + " " + customers[2][x])
    favKayak.append(0) #fills 20 locations with 0
    totalHrs.append(0) #fills 20 locations with 0
# at this point everything is empty


for x in range(len(customerID)): #loops x for each customer
    emptyKayakCount()#this is to empty count for each new customer
    for y in range(len(rentals)): #for each x, run through rentals tables
        if(customerID[x] == rentals[1][y]): #if customer id is same as person who rented kayak on that line, do the following...
            totalHrs[x] += round(float(rentals[4][y]),4) # grab rentals[4][x] <-- time spent
            kayakCount[int(rentals[0][y]) - 1] += 1 # check kayakID and increment
            #print(kayakCount)
            #print("customerID at x=" + str(x) + " is the following: " + str(customerID[x]))
        #by here I have total number of times each kayak was rented by a person, below I will store ID of most used
        compareVal = -1 # temp val to store comparison value, if compare value is bigger than stored value, replace favKayak with value
        biggestVal = 0 #stores biggest value
    for i in range(len(kayakCount)):
        compareVal = kayakCount[i]
        if(compareVal > biggestVal):#if compare value is bigger than "biggest value", store compare into biggest to make true
            biggestVal = compareVal
            favKayak[x] = i+1#then store i (aka ID of kayak)


customerInfo = pd.DataFrame({'customerID' : customerID, 'customerName' : customerName, 'favoriteKayak' : favKayak, 'totalRentalTime' : totalHrs})
customerInfo.to_csv(str(filePath) + 'customer_report.txt', sep="\t", index=False, encoding='utf-8')
print("\nWrote to file customer_report.txt")
#print(customerInfo) #this shows what would be printed to file
#only issue(or as i call it a feature) with this setup is, if a person rents 2 kayaks for same amount of time
#example kayak_id=3 and kayak_id=7 is rented same amount of time, the favorite kayak returned is 3
#below I left my notes

#get number of times rented, also display real name from customer table
#most rented kayak
#total num hours of all rentals

#based off customer id check how many times their id appears in list of data, that is number of times rented
#create an array of size 20, each time customer id pops up, get kayak id and increment array index at kayak id location
#when incrementing number of kayak rentals, grab rentals[4][x] <--number of hours rented and store into total sum variable

input("\nContinue to next question?")
cls()



# 5 - Scoring the rental experience
'''
The business has been collecting keyword tags when 
somebody rents a kayak. If somebody is "helpful" or
"polite" we like that customer more than if they have
a "damage" or "rescue-required" tag.

For each rental, calculate and store a value score
using the keywords. If there are no keywords score 
could be None or 0 (your choice), otherwise it will
be an integer sum of the value_scores for the word tags. 
'''

#I interpreted this question as each customer has tags associated with them -> those tags have a score -> that score represents person
#below i will get tag associated with entry, find value of tag and store it as a sum for that person
customerScore = list()
customerTagCount = list() #this is going to be used for next question ;)
for x in range(1,len(customers)):
    customerScore.append(0)#fills customer score with enough locations per each customer and 0s it out
    customerTagCount.append(0)
#First create an dataframe to store all people, peopleInfo[id][First and Last Name][score] <--- code has been moved to bottom
#create a tags enum, with all data from tags.txt
'''
for x in range(1,len(tags)): #this is code I used to format enum variables, I couldnt think of a better way that isnt over complicated
    formattedTags.append(str(tags[0][x]) + " = " + str(tags[1][x]))
tagsDF = pd.DataFrame({'title' : formattedTags})
tagsDF.to_csv('C:/Users/2cody/Desktop/Data Science/HW3/tagsEDIT.txt', sep="\n", index=False, encoding='utf-8')
#previous failed test
'''


#go through each rental, check rentals[1][x] <-- id,    store name in peopleInfo[ rentals[1][x] ][x], once name is stored
#grab rentals[5][x] <--- notes, each entry is comma seperated, get data via regex, loop through data compared against tags enum and store into peopleInfo[][][SCORE]
for x in range(1,len(rentals)):#loops through rentals dataframe
    customerIndex = int(rentals[1][x]) - 1
    searchText = str(rentals[5][x])
    x = re.findall("[a-zA-Z-]*\S", searchText)
    for y in range(len(x)):
        #print("X=" + str(x[y]) + ",\n")#gives each indivial string value
        for z in range(1,len(tags)):#loops through tag dataframe
            if(str(x[y]) == str(tags[0][z])):
                #print("x=" + str(x[y]) + " matches tag=" + str(tags[0][z]) + ", returning value=" + str(tags[1][z])) #debug line to show data
                customerScore[customerIndex] += int(tags[1][z])
                customerTagCount[customerIndex] += 1 # increments the number of tags contributing to score(this is used to divide and get average later...)
    #print("---------------------------------")#used this with debug to show sepration between each match test

#by this point all users should have a score and line below can run
peopleInfo = pd.DataFrame({'customerID' : customerID, 'customerName' : customerName, 'score' : customerScore, 'tagAmount' : customerTagCount})
print(peopleInfo)

#next check what is highest score from my dataFrame BUT DO THIS ON NEXT QUESTION

#my notes are below
#make function that takes rentals>notes as param, then that compares it against enum and returns a score
#have regex store, the number of items grabbed, if a note has 3 comments, return number 3
#have function return data in the form   valArray[score][number of comments]
input("\nContinue to next question?")
cls()
print("\n")

# 6 - Finding the good and bad customers
'''
We should be able to identify the best and worst
customers using the rental value scores.

Calculate a "customer_score" that is the average
of the rental scores for that customer.

Identify the 5 best and 5 worst customers. Produce
some kind of graphic display of customer scores.

Are there predictors for who is a good or bad
customer? Produce a report with the customer
scores grouped by sex. In R generate a boxplot for
each sex M, F, X showing the distribution of 
customer scores.
'''
customer_score = list()
'''for x in range(1,len(customers)):
    customer_score.append(0)# fill it with zeros
'''
for x in range(len(peopleInfo)):
    average = int(customerScore[x]) / int(customerTagCount[x]) # X + 1 == customerID
    
    customer_score.append(round(average,4))# customerID - 1 == index
#print("Customer_Score in order based of ID[1-20]")
#print(customer_score)
#print()
#i have average of all scores by here, next need to sort top scores vs lowest scores into an array with two values [customerID][score]
#make 2 arrays, highest score, another lowest score
#store top 5 scores
greaterNum = list()
idNum = list()
testNum = float()
sexList = list()

for x in range(5):
    greaterNum.append(-100)#fills customer score with enough locations per each customer and 0s it out
    idNum.append(0)
    sexList.append("blank")
#print("--------------------------------------------------")
for x in range(len(customer_score)):
    testNum = customer_score[x]
    for y in range(len(greaterNum)):
        if(testNum > greaterNum[0]):
            greaterNum[0] = testNum # set new largest number in first(smallest position) in list
            #print("greaterNum="+str(greaterNum))
            greaterNum.sort() # sort list in correct order
            #print("AFTER SORT greaterNum="+str(greaterNum))
        break

for x in range(len(customer_score)): # loop over customer score 
    for y in range(len(greaterNum)):# loop over greaterNum
        if(float(customer_score[x]) == float(greaterNum[y])): # comparing values of greater num to customer score, to get customerID
            #if inside here, greater num matches with customer score, get x + 1 and store as customerID
            idNum[y] = int(x) + 1
            for z in range(1,len(customers)):#loop over list of customers
                if(int(customers[0][z]) == int(idNum[y])):#grab customerID and see if equal to idNum[y](customers ID number)
                    #print("customers[0][z]=" + str(customers[0][z]) + "\nidNum[y]=" + str(idNum[y]) + "\ncustomers[3][z]=" + str(customers[3][z])+"\n--------------------------")
                    sexList[y] = customers[3][z]#once i know row of customerID, ill grab the sex associated
                    break

#print("Sorted greaterNum = " + str(greaterNum))
#print("sorted customerID = " + str(idNum))
#print("--------------------------------------------------")
userScore = pd.DataFrame({'bestCustomer_ID' : idNum,'bestCustomer_Score' : greaterNum, 'best_sex' : sexList})

for x in range(5):
    greaterNum[x]=100
    sexList[x]="BLANK"
#at this point I have best customers, im just copying and pasting code changing a line or so to get least
for x in range(len(customer_score)):
    testNum = customer_score[x]
    for y in range(len(greaterNum)):
        if(testNum < greaterNum[0]):
            greaterNum[0] = testNum # set new largest number in first(smallest position) in list
            #print("greaterNum="+str(greaterNum))
            greaterNum.sort(reverse=True) # sort list in correct order
            #print("AFTER SORT greaterNum="+str(greaterNum))
        break

for x in range(len(customer_score)): # loop over customer score 
    for y in range(len(greaterNum)):# loop over greaterNum
        if(float(customer_score[x]) == float(greaterNum[y])): # comparing values of greater num to customer score, to get customerID
            #if inside here, greater num matches with customer score, get x + 1 and store as customerID
            idNum[y] = int(x) + 1
            for z in range(1,len(customers)):#loop over list of customers
                if(int(customers[0][z]) == int(idNum[y])):#grab customerID and see if equal to idNum[y](customers ID number)
                    #print("customers[0][z]=" + str(customers[0][z]) + "\nidNum[y]=" + str(idNum[y]) + "\ncustomers[3][z]=" + str(customers[3][z])+"\n--------------------------")
                    sexList[y] = customers[3][z]#once i know row of customerID, ill grab the sex associated
                    break

#print("Sorted smallerNum = " + str(greaterNum))
#print("sorted customerID = " + str(idNum))
#print("--------------------------------------------------")
userScore.insert(3,'worstCustomer_ID',idNum)#add new column to dataframe at index 3
userScore.insert(4,'worstCustomer_Score',greaterNum)#add new column to dataframe at index 4
userScore.insert(5,'worst_sex',sexList)#add new column to dataframe at index 5
print()
print(userScore)
userScore.to_csv(str(filePath) + 'userScore.csv', index=False, encoding='utf-8')
print("\nExported data of best and worst as 'userScore.csv'\nR box plot saved as 'best_customers.jpeg'")
#best I can tell from boxplot is that people who dont mark their sex are better than both men and women
# the best people are sex: X(or should i say best person) but not enough to conclude its all of those people
#men are the worst and woman are just in between


#first get average rental score, go through each rental, grab notes, send it to enum compare functions,
#HOW DO I GET AVERAGE??? is it per note left? like if one rental has 4 notes, or is it just per row? i think per note
#to get sum of all scores, enum compare function will return score for each row, and number of notes on that line
#store score for row into total score sum, store number of comments as well in a sperate var called totalScore
#---DONT DO THIS, do sperate variables------maybe in form totalUserInfo[ totalScore ][ totalNotes ]
#once u done take total number of notes(NOT NUMBER OF ROWS IN RENTALS), and the sum of all scores
#customer_score = totalScore / totalNotes


#this info is just average, this does not give 5 best and worst customers
#still need to do the rest


input("\nPress any key to exit.")
cls()




'''
Are you feeling powerful with your code for this?
Keep going! These aren't required but give them a
try and feel free to include your solutions when
you submit your homework, maybe having work here
can fill in a few gaps you may have above.

Optional: Generate coupons for the five
best customers, half off if they want to come take
out their favorite kayak (most rented or most hours)
on their favorite day of the week (most visits or
most hours of rental, your choice how to define it).

Optional: Calculate the standard deviation
of the rental scores for each customer to see which
customers are most or least consistent in their rental
relationship with the business.

Optional: Calculate a 2nd customer metric called
"high_maintenance" which scores the average number of
word tags this customer's rental records has, whether
positive or negative. Some customer's don't have lots
of word tags, they just rent and we get revenue. Other
customers take more of our time and attention (the
ones with lots of tags). Who is the highest on the
"high_maintenance" statistic?
'''