def calcrate():
    fname=input("Enter names :")
    age=int(input("Enter age :"))
    if age<=17:
        print("Not valid for persons under 18years of age try again the the next ",18-age," years")
        exit()
    else:
        year1=int(input("Enter  year of investment :"))
        amnt=int(input("Enter Investment amount :"))
        yearcounts1=int(input("Enter year of withdrawal :"))
        rate = 4
        rateyear=yearcounts1 - year1
        interestincome1 = amnt *rate * rateyear
        interestincome1final=interestincome1/100
        totalamnt=amnt +interestincome1final
        final_total=totalamnt *rate * rateyear
        print( "Your income/profit by the end of " ,rateyear, " year(s)  provincially ,therefore "
        "your total earnings will be ", final_total)


print(calcrate())


