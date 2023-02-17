def main():
  intro()
  try: 
    g = int(input(" Enter the number of gallons: "))
    gallons_to_liters(gallons)
    print()
  except:
    print("An exception occured, try another number")
    print()
    main()

def intro():
    print("This program convert measurement ")
    print("Gallons into liters")
    print()

def gallons_to_liters(gallons):
   liters = gallons * 3.78541
   print("That converts to", liters,"liters")
   print()
   response= str(input("Continue to another conversion? Yes or No "))
   if response == "no":
    print()
    print("Thank you and goodbye")
   elif response== "yes":
      print()
      main()
   else:
      print(response)
main()
   