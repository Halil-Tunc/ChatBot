# This part of my code welcomes the user and collects the users name and age.
name = input ("Hello I am the Elite 101 ChatBot, what's your name? ")
print (f"Hello, {name}.")
age = input ("How old are you? ")

if int(age) == 13 or int(age) < 13:
  print (f"What I wouldn't give to be {age} again!")
  
  print (f"How can I help you today?")
  print (f"1. Where can I find the cheapest toys?")
  print (f"2. Where can I find the cheapest video games?")
  print (f"3. Where can I find the cheapest game consoles?")
  print (f"4. Exit conversation")
  choice = input ("Enter the given number of your choice: ")

  if choice == "1":
    print (f"This is meant to be a place holder for a continuation in the future.")
  if choice == "2":
    print (f"This is meant to ba a place holder for a continuation in the future.")
  if choice =="3":
    print (f"This is meant to be a place holder for a continuation in the future.")
  if choice == "4":
    print (f"Goodbye, {name}.")
    exit()

if int(age) == 14 or int(age) < 18 and int(age) > 14:
  print (f"The good old days!")
  
  print (f"How can I help you today?")
  print (f"1. Where can I get my learners permit?")
  print (f"2. Where can I get my drivers license?")
  print (f"3. Where can I get employed?")
  print (f"4. Exit conversation")
  choice = input ("Enter the given number of your choice: ")

  if choice == "1":
    print (f"This is meant to be a place holder for a continuation in the future.")
  if choice == "2":
    print (f"This is meant to ba a place holder for a continuation in the future.")
  if choice =="3":
    print (f"This is meant to be a place holder for a continuation in the future.")
  if choice == "4":
    print (f"Goodbye, {name}.")
    exit()
    
if int(age) == 18 or int(age) > 18 and int(age) < 125:
  print (f"time flies by, doesn't it?")
  
  print (f"How can I help you today?")
  print (f"1. When can I retire?")
  print (f"2. Where can I apply for the military?")
  print (f"3. Where can I vote?")
  print (f"4. Exit conversation")
  choice = input ("Enter the given number of your choice: ")

  if choice == "1":
    print (f"This is meant to be a place holder for a continuation in the future.")
  if choice == "2":
    print (f"This is meant to ba a place holder for a continuation in the future.")
  if choice =="3":
    print (f"This is meant to be a place holder for a continuation in the future.")
  if choice == "4":
    print (f"Goodbye, {name}.")
    exit()
    
if int(age) == 125 or int(age) > 125:
  print (f"You've gotta be kidding me, the oldest a human can be is 125.")
if not(int(age)<=0) or not(int(age)>=0):
  print (f"Please enter a real number.")

