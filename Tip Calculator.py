print("Welcome To The Tip Calculator!")

bill=(float(input("Total Bill:$")))

tip=int(input("How Much tip Would You Like To Give? 10, 12, or 15? "))

people=int(input("people to split the bill?"))

tip_as_percent=tip/100

total_tip_amount=bill*tip_as_percent

total_bill=bill + total_tip_amount

bill_per_person=total_bill/people


Final_Bill=round(bill_per_person,2)

print(f"Each Person Should Pay{Final_Bill}")
      
