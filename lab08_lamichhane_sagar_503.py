#Name : Sagar Lamichhane
#Course : 1411-001
#Date : 10/31/2017
#
#
#Problem
#A python proram to generate the chances of winning and money spent by a person if he played lotto drawing from 1992 to 2017
#
#
#Given:
#Lotto drawings from 1992 to 2017 with the chances to win prize depending on the number match with drawings.
#2 matching numbers - $2
#3 matching numbers - $10 
#4 matching numbers - $100
#5 matching numbers - $10,000
#6 matching numbers - $100,000
#Each ticket cost $1
#
#
#Analysis
#Input : Input the lotto ticket as random numbers
#Output :  Check the winning prize and show the amount that you would have spent on buying lotto tickets.
#
#METHOD/ALGORITHM:
#Introduce the program
#Input any unique 6 digit numbers starting from 1 to 54.
#The program checks your winning prize with the same ticket you put as an input with dwawings from 1992 to 2017.
#The progrem tells how much money you would have spent on buying a dollar ticket from 1992 to 2017.
#Program also creates a set of 6 integers that would win the least or the most money over time 
#
#
#Test Cases:
#TEST CASE 1:
#INPUT : {1,17,9,45,51,7}
#OUTPUT : winnings :: 170 dollars
#       : You would have spent 289 dollars on tickets 
#
#
#TEST CASE 2:
#INPUT : [4,17,9,28,39,50}
#OUTPUT : winnings :: 0 dollars
#       : You would have spent 0 dollars on tickets
#
#PROGRAM
#
#
import csv      #import csv
from random import *    #get random numbers
amount = 0

def any_num(a_number):  #create function to get rendon numbers
    for l in range(6):
        a_number.append(str(randint(1, 54)))  #numbers from 1 to 54
    return a_number

try:  #create try execption handler   

    a_number = []   #generate lists
    any_num(a_number)

    file_name = "lottotexas.csv"  #open filename to read excel file
    a_word = open(file_name, "r")
    reader = csv.reader(a_word)  

    b_list = {}
    x = 0
    
    for i in reader:
        date = ""
        any_lists = []
        
        date = date + i[1] + "/" + i[2] + "/" + i[3]   #creating dates seperated by /

        for char in range (4, 10):       #listig winning tickets seperated by ,
            any_lists.append(i[char])

        b_list[date] = any_lists

    for a_word in b_list.values():
        x += 1
        y = 0
        for n in a_number:
            if n in a_word:  #loop to check input numbers matched with winning numbers
                y += 1       #and provide winning prize accordingly
        if y == 2:
            amount += 2
        elif y == 3:
            amount += 10
        elif y == 4:
            amount += 100
        elif y == 5:
            amount += 10000
        elif y == 6:
            amount += 100000

except IOError:   
    print ("Cannot open ", file_name)  # incase wrong filename is given
print("Your Lotto ticket is  ", a_number)   #printing necessary outputs
print("Your total winning from 1992 to 2017 are " , amount, "dollars")
print("You would have spent", x, "dollars on Texas lotto tickets from 1992 to 2017")
