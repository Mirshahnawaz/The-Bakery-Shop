#IMPORTING LIBRARIES
import time



#METHODS OF FOOD:
def add_items():
   global samosa_stock,roll_stock
   samosa_stock = samosa_stock + int(input("HOW MANY SOMOSAS DO YOU WANT TO ADD = "))
   roll_stock = roll_stock + int(input("HOW MANY ROLLS DO YOU WANT TO ADD = "))
def show_items():
   global samosa_stock,roll_stock
   print(f'1.SAMOSAS IN STOCK = {samosa_stock}\n2.ROLLS IN STOCK = {roll_stock}')
       
def order_bill():
   global samosa_stock,roll_stock,lis_1,bill,bill2
   while True:
      global sales
      print(f'HELLO SIR WELCOME TO CHRIS EVANS BAKE SHOP\n...........MENU............\n1. SAMOSA\t\tRS 10\t\tSTOCK = {samosa_stock}\n2. ROLL\t\t\tRS 20\t\tSTOCK = {roll_stock}\n\tPRESS \"E\" TO EXIT THE MENU')
      cus = input("WHICH ITEM YOU WANT TO ORDER...?")
      lis_1.append(cus)
      if cus == "1":
         
         quan = int(input("HOW MANY SAMOSAS DO YOU WANT....?"))
         if quan > samosa_stock:
            print("SORRY SIR ONLY",samosa_stock,"SAMOSAS ARE AVAILABLE NOW")
         else:
            bill = bill + quan * 10            
            sales += quan
            print(f'{quan} SAMOSA ADDED TO YOUR CART..\nPRESS \"M\" TO GET THE BILL')
            
            samosa_stock -= quan
      elif cus == "E" or cus == "e":
         break
      
      elif cus == "M" or cus == "m":
         
         if "1" in lis_1 and "2" in lis_1 :
            total_bill_1 = bill + bill2
            print(f'SIR YOUR TOTAL BILL IS = {total_bill_1}')
            lis_1.clear()
            bill = 0
            bill2 = 0
            break
         
         elif "1" in lis_1 :
            total_bill_1 = bill
            print(f'SIR YOUR TOTAL BILL IS = {total_bill_1}')
            lis_1.clear()
            bill = 0
            break         
         elif "2" in lis_1:
            total_bill_1 = bill2
            print(f'SIR YOUR TOTAL BILL IS = {total_bill_1}')
            lis_1.clear()
            bill2 = 0
            break
         
      else:
         
         quan_1 = int(input("HOW MANY ROLL DO YOU WANT....?"))
         if quan_1 > roll_stock:
            print("SORRY SIR ONLY",roll_stock,"ROLLS ARE AVAILABLE NOW")
         else:
            bill2 = bill2 + quan_1 * 20
            sales += quan_1
            print(f'{quan_1} ROLLS ADDED TO YOUR CART...\nPRESS \"M\" TO GET THE BILL')
            
            roll_stock -= quan_1
      
   
#METHODS OF EMPLOYEE:
def set_wage_rate():
   global emp_A_wage_rate,emp_B_wage_rate
   emp_A_wage_rate =  int(input("WHAT IS THE WAGE RATE OF EMPLOYEE A="))
   emp_B_wage_rate =  int(input("WHAT IS THE WAGE RATE OF EMPLOYEE B="))
   add_hours_worked()
def add_hours_worked():
   global emp_A_hours,emp_B_hours
   emp_A_hours = emp_A_hours + int(input("EMPLOYEE A HOW MANY HOURS YOU WORKED? ="))
   emp_B_hours = emp_B_hours + int(input("EMPLOYEE B HOW MANY HOURS YOU WORKED? ="))
   calculate_payment()
def calculate_payment():
   global emp_A_wage_rate,emp_B_wage_rate,emp_A_hours,emp_B_hours
   print("CALCULATING PAYMENT PLEASE WAIT.",end = "")
   time.sleep(1)
   print(".",end = "")
   time.sleep(1)
   print(".",end = "")
   time.sleep(1)
   print(".",end = "")
   time.sleep(1)
   print(".",end = "")
   time.sleep(1)
   print(".")
   time.sleep(1)
   print(f'PAYMENT OF EMPLOYEE A = {emp_A_wage_rate*emp_A_hours}\nPAYMENT OF EMPLOYEE B = {emp_B_wage_rate*emp_B_hours}')
   calculating_bonus()
def calculating_bonus():
   global emp_A_wage_rate,emp_B_wage_rate,emp_A_hours,emp_B_hours,sales,targer_sales,bonus
   print("CALCULATING BONUS PLEASE WAIT.",end = "")
   time.sleep(1)
   print(".",end = "")
   time.sleep(1)
   print(".",end = "")
   time.sleep(1)
   print(".",end = "")
   time.sleep(1)
   print(".",end = "")
   time.sleep(1)
   print(".")
   time.sleep(1)
   if sales >= target_sales:
      bonus = 1000
      print("CONGRATULATION EMPLOYEES WE CHASED OUR TARGET OF SALES SO BONUS OF RS 1000 IS ADDED TO YOUR SALARY")
      print(f'TOTAL SALARY OF EMPLOYEE A = {emp_A_wage_rate*emp_A_hours+1000}\nTOTAL SALARY OF EMPLOYEE B = {emp_B_wage_rate*emp_B_hours+1000}')
      sales = 0
   else:
      print("SORRY EMPLOYEES WE DIDN'T CHASE OUR TARGET OF SALES SO THERE IS NO BONUS FOR YOU :/")


#METHODS OF BOUTIQUE
def add_boutique_items():
   global white_stock,ajrak_stock,boski_stock
   white_stock = white_stock + int(input("HOW MANY WHITE COTTON SUIT YOU WANT TO ADD IN BOUTIQUE? ="))
   ajrak_stock = ajrak_stock + int(input("HOW MANY SINDHI AJRAKS YOU WANT TO ADD IN BOUTIQUE? ="))
   boski_stock = boski_stock + int(input("HOW MANY PURE BOSKI SUIT YOU WANT TO ADD IN BOUTIQUE? ="))
def shopping():
   global white_stock,ajrak_stock,boski_stock,lis
   while True:
      print(f'HELLO SIR WELCOME TO SINDHI CULTURAL OUTFITS\n\t  ...........BOUTIQUE CATLOUGE...........\n\n1.WHITE COTTON SUIT\t\tRS 6000\t\tSTOCK = {white_stock}\n2.SINDHI AJRAK\t\t\tRS 3000\t        STOCK = {ajrak_stock}\n3.PURE BOSKI SUIT\t\tRS 8000\t\tSTOCK = {boski_stock}\n\t \n\t\tPRESS \"E\" TO EXIT THE CATALOGUE\t\t\t\t\t\t\t\t\t\n\n\n#NOTE#\nIF YOU WILL DO SHOPPING GREATER\nTHAN RS 10000 THAN YOU WILL\nGET 1 WHITE COTTON SUIT FREE\n AND YOU WILL DO SHOPPING\n GREATER THAN RS 20000 SO YOU WILL GET 2\n WHITE COTTON SUITS\n\n\n')
      
      b1 = input("WHICH THING YOU WANT BUY...?")
      lis.append(b1)
      
      if b1 == "1":
         quan_b1 = int(input("HOW MANY WHITE COTTON SUITS DO YOU WANT BUY....?"))
         if quan_b1 > white_stock:
            print("SORRY SIR ONLY",white_stock,"WHITE COTTON SUITS ARE AVAILABLE NOW")
         else:
            
            bill_b1 = quan_b1 * 6000
            print(f'{quan_b1} WHITE COTTON SUIT ADDED TO YOUR CART...\nPRESS \"M\" TO GET THE BILL')
            white_stock -= quan_b1
      elif b1 == "E" or b1 == "e":
         break
      
      elif b1 == "M" or b1 == "m":
         global total_bill
         
         
         if "1" in lis and "2" in lis and "3" in lis:
            total_bill = bill_b1 + bill_b2 + bill_b3
            print(f'SIR YOUR TOTAL BILL IS = {total_bill}')
            lis.clear()
            break
         elif "1" in lis and "2" in lis:
            total_bill = bill_b1 + bill_b2
            print(f'SIR YOUR TOTAL BILL IS = {total_bill}')
            lis.clear()
            break
         elif "1" in lis  and "3" in lis:
            total_bill = bill_b1 + bill_b3
            print(f'SIR YOUR TOTAL BILL IS = {total_bill}')
            lis.clear()
            break
         elif "1" in lis :
            total_bill = bill_b1
            print(f'SIR YOUR TOTAL BILL IS = {total_bill}')
            lis.clear()
            break
         elif "2" in lis and "3" in lis:
            total_bill = bill_b2 + bill_b3
            print(f'SIR YOUR TOTAL BILL IS = {total_bill}')
            lis.clear()
            break
         elif "2" in lis:
            total_bill = bill_b2
            print(f'SIR YOUR TOTAL BILL IS = {total_bill}')
            lis.clear()
            break
         elif "3" in lis:
            total_bill = bill_b3
            print(f'SIR YOUR TOTAL BILL IS = {total_bill}')
            lis.clear()
            break
         
         
      elif b1 == "2":         
         quan_b2 = int(input("HOW MANY SINDHI AJRAKS DO YOU WANT BUY....?"))
         if quan_b2 > ajrak_stock:
            print("SORRY SIR ONLY",ajrak_stock,"SINDHI AJRAK ARE AVAILABLE NOW")
         else:
            
            bill_b2 = quan_b2 * 3000
            print(f'{quan_b2} SINDHI AJRAK ADDED TO YOUR CART...\nPRESS \"M\" TO GET THE BILL')
            ajrak_stock -= quan_b2
      elif b1 == "3":         
         quan_b3 = int(input("HOW MANY PURE BOSKI SUITS DO YOU WANT BUY....?"))
         if quan_b3 > boski_stock:
            print("SORRY SIR ONLY",boski_stock,"BOSKI SUITS ARE AVAILABLE NOW")
         else:
            
            bill_b3 = quan_b3 * 8000
            print(f'{quan_b3} PURE BOSKI SUIT ADDED TO YOUR CART...\nPRESS \"M\" TO GET THE BILL')
            boski_stock -= quan_b3
   
def discount():
   global white_stock,ajrak_stock,boski_stock,total_bill
   if total_bill == 0:
      print("SORRY SIR YOU WON'T BE GIFTED BECAUSE YOU DIDN'T DO ANY SHOPPING :/")
   elif total_bill > 0 and total_bill < 10000:
      print("SORRY SIR YOU 'll BE GIFTED ONLY WHEN YOU HAD DONE SHOPPING OF RS 10000 AND ABOVE :/")
   elif total_bill >= 10000 and total_bill < 20000 :
      white_stock -= 1
      print("SIR CONGRATULAIONS YOU ARE GIFTED WITH 1 WHITE COTTON SUIT :)")
   elif total_bill > 20000:
      white_stock -= 2
      print("SIR CONGRATULAIONS YOU ARE GIFTED WITH 2 WHITE COTTON SUIT :)")
   total_bill = 0
      
   
   
      
   
   
   
   

   

   

   
   
   
   
   
   

#ATTRIBUTES OF FOOD
target_sales = 30
samosa_stock = 0
roll_stock = 0
samosa_price = 10
roll_price = 20
sales = 0
lis_1 = []
bill = 0
bill2 = 0

#ATTRIBUTE OF EMPLOYEE
emp_A_wage_rate = 0
emp_B_wage_rate = 0
emp_A_hours = 0
emp_B_hours = 0
bonus = 0


#ATTRIBUTES OF BOUTIQUE
white_cotton_suit = 6000
sindhi_ajrak = 3000
pure_boski = 8000
white_stock = 0
ajrak_stock = 0
boski_stock = 0
lis = []





#MAIN WINDOW
while True:
   
   print("#DEAR CUSTOMER WE HAVE TOTAL TWO SHOPS#\n1.CHRIS EVANS BAKE SHOP\n2.BOUTIQUE\n3.PRESS 3 IF YOU ARE AN EMPLOYEE\nPRESS \"E\" TO EXIT......")
   choice = input("WHERE ARE YOU WANT TO GO.....??\nENTER YOU CHOICE...")
   if choice == "1":
      while True:
         print("1.ADD ITEMS TO STOCK\n2.SHOW ITEMS IN STOCK\n3.TAKE ORDER AND BILL\nPRESS \"M\" TO GO TO THE MAIN MENU")
         ch = input("ENTER YOUR CHOICE=")
         if ch == "1":
            add_items()
         elif ch == "2":
            show_items()
         elif ch == "3":
            order_bill()
         else:
            break
            
         
      
   elif choice == "2":
      while True:
         print("1.ADD BOUTIQUE ITEMS TO STOCK\n2.SHOPPING AND TAKE BILL\n3.FREE GIFTS FOR CUSTOMER(IF YOU HAD DONE SHOPPING)\nPRESS \"M\" TO GO TO THE MAIN MENU")
         ch1 = input("ENTER YOUR CHOICE=")
         if ch1 == "1":
            add_boutique_items()
         elif ch1 == "2":
            shopping()
         elif ch1 == "3":
            discount()
         else:
            break
         
   elif choice == "3":
      set_wage_rate()
         
   elif choice == "E" or choice == "e":
      print("THANKS FOR COMING HAVE A GOOD DAY SIR :)")
      break





      
