'''Restruarant order management system'''

#Creating the menus/meals using "dictionary"
"""Veg Menu"""
# Menu 01
menu_veg={}
menu_veg["Veg Palao"]=149
menu_veg["Palak Paneer"]=199
menu_veg["Paneer Butter Masaala"]=249
menu_veg["Veg Burger"]=229
menu_veg["Veg Pizza"]=279

"""Non veg menu"""
# Menu 02
menu_nveg={}
menu_nveg["Butter Chicken"]=299
menu_nveg["Fish Moilee"]=139
menu_nveg["Pizza"]=319
menu_nveg["Burger"]=289
menu_nveg["Mutton Kosha"]=399

"""Starter Menu"""
# Menu 03
menu_st={}
menu_st["Chicken Tandoori"]=99
menu_st["Prawn Malai"]=109
menu_st["Fried Chicken"]=139
menu_st["Paneer Tikka"]=119
menu_st["Aloo Chat"]=79

"""Drinks Menu"""
# Menu 04
menu_dr={}
menu_dr["Mango Lassi"]=99
menu_dr["Masala Chai"]=39
menu_dr["Coffee"]=49
menu_dr["Cold Drinks"]=69
menu_dr["Virgin Mojito"]=159

#generate random alpha numeric code for transaction 
import random
import string
def generate_random_alphanumeric(length):
    characters = string.ascii_letters + string.digits  
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Generate an order number
import datetime
def generate_order_number():
    now = datetime.datetime.now()
    order_number = now.strftime('%Y%m%d%H%M%S') 
    return order_number

def order_token():
  now = datetime.datetime.now()
  token = now.strftime('%H%M%S')
  return token

odr_ttl=0 #order total will be added here
str1=input("Welcome to Restro SA\nWould you like to start your order?(y/n)")
if str1.lower()=="y":
  print("Great! You are just few steps away:\n","\tTo open 'Starter Menu' press 'st':\n","\tTo open 'Veg Menu' press 'veg':\n","\tTo open 'Non Veg Menu' press 'nveg':\n","\tTo open 'Drinks Cart' press 'dr'\n","\tPress 'all' for 'All Menu':\n")
  
  while True:
    key1=input()
    if key1.lower()=="st":
      print("Starter For U ",menu_st)
      break
    elif key1.lower()=="veg":
      print("Veg For U ",menu_veg)
      break
    elif key1.lower()=="nveg":
      print("Non Veg For U ",menu_nveg)
      break
    elif key1.lower()=="dr":
      print("Drinks For U ",menu_dr)
      break
    elif key1.lower()=="all":
      print("Starter For U ",menu_st,"\n","Veg For U ",menu_veg,"\n","Non Veg For U ",menu_nveg,"\n","Drinks For U ",menu_dr,"\n")
      break
    else:
      print("Invalid Choice, Please Try Again")
      
  print("\n\n")
  cart=["\nSelected items in Cart:\n"]
  odr_val=0
  cpn_list={
    'FIRST':30,
    'Family':25,
    'BIG4':13,
    'Abxyz':11,
    'SARAJIT':10,
    'specialONE':49,
    'couple45':30
  }
  while True:
    item=input("Enter your item:\n")
    if item in menu_st:
      odr_ttl+=menu_st[item]
      odr_val+=1
      print("your selected item is: ",item," Price at Rs.",menu_st[item])
      cart.append(item)
    elif item in menu_veg:
      odr_ttl+=menu_veg[item]
      odr_val+=1
      print("your selected item is: ",item," Price at Rs.",menu_veg[item])
      cart.append(item)
    elif item in menu_nveg:
      odr_ttl+=menu_nveg[item]
      odr_val+=1
      print("your selected item is: ",item," Price at Rs.",menu_nveg[item])
      cart.append(item)
    elif item in menu_dr:
      odr_ttl+=menu_dr[item]
      odr_val+=1
      print("your selected item is: ",item," Price at Rs.",menu_dr[item])
      cart.append(item)
    else:
      print("\n\n\tThe entered item: ", item,"is not available, SORRY!\n\n")
    key2=input("Would you like to add another item(y/n):\n")
    if key2.lower()!="y":
      break
            
  
  print("Dear Customer, you have added ", odr_val, " items in your cart\n")
  print(cart[0],"\n")
  for i in range(1,(odr_val+1)):
    if cart[i] in menu_st:
      print("\t",cart[i]," priced at Rs. ",menu_st[cart[i]])
    elif cart[i] in menu_veg:
      print("\t",cart[i]," priced at Rs. ",menu_veg[cart[i]])
    elif cart[i] in menu_nveg:
      print("\t",cart[i]," priced at Rs. ",menu_nveg[cart[i]])
    else:
      print("\t",cart[i]," priced at Rs. ",menu_dr[cart[i]])
    i+=1
  print("   \n")
  print("\nTotal Value of Cart is:\t",odr_ttl, "  for  ",odr_val, "  items")
  while True:
    key3=input("To Continue Press Yes:\n")
    if key3.lower()!="yes":
      print("Invalid input, Press Yes:\n")
    else:
      for i in range(1,(odr_val+1)):
        if cart[i] in menu_st:
          print("\t",cart[i]," priced at Rs. ",menu_st[cart[i]])
        elif cart[i] in menu_veg:
          print("\t",cart[i]," priced at Rs. ",menu_veg[cart[i]])
        elif cart[i] in menu_nveg:
          print("\t",cart[i]," priced at Rs. ",menu_nveg[cart[i]])
        else:
          print("\t",cart[i]," priced at Rs. ",menu_dr[cart[i]])
        i+=1
      print("Cart Value:\t\t\t",odr_ttl)
      print("\nGST Added:    18%\n")
      print("\nService Tax Added:    5%\n")
      odr_ttl=odr_ttl+(odr_ttl*18/100)+(odr_ttl*5/100)
      print("\nGrand Total:\t\t\t",odr_ttl)
      key4=input("Do you have any COUPON (y/n):\n")
      if key4.lower()=="y":
        while True:
          coupon=input("Enter your coupon (FIRST,Family,BIG4,Abxyz,SARAJIT,specialONE,couple45):\n")
          if coupon in cpn_list:
            print("Congrats! you unlocked OFFER of ",cpn_list[coupon],"% deduction on your order for ",coupon," coupon")
            deduct=odr_ttl*cpn_list[coupon]/100
            odr_ttl=odr_ttl-(odr_ttl*cpn_list[coupon]/100)
            print("\tAmount deducted: ",deduct)
            print("\nAmount to be paid for your order Rs. ",odr_ttl)
            key5=input("'Submit' to complete your order:\n 'cancel/any key' to cancel your order:\n")
            if key5.lower()=="submit":
              print("\tYour order is placed Successfully! Cheers!\n")
              print("\tOrder Token: ",order_token(),"\n")
              print("\tTransaction Id: ",generate_random_alphanumeric(15),"\n")
              print("\tOrder ID: ",generate_order_number(),"\n")
              print("Amount Paid: ",odr_ttl)
            else:
              print("Your Order is Canceled")
            break
          else:
            print("Oops! Invalid Coupon, Please try again\n")
        break
      else:
        print("\nAmount to be paid Rs. ",odr_ttl)
        key6=input("To complete your order press 'y':\nTo cancel order press 'n'/any key:")
        if key6.lower()=="y":
          print("\tCheers! you have SUCCESSFULLY placed your order\n")
          print("\tOrder Token: ",order_token(),"\n")
          print("\tTransaction Id: ",generate_random_alphanumeric(15),"\n")
          print("\tOrder ID: ",generate_order_number(),"\n")
          print("Amount Paid: ",odr_ttl)
        else:
          print("Your Order is Canceled!")
      break  
else:
  print("Sorry! you did not order anything,")