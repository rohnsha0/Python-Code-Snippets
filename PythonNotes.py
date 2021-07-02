print("My Name is Rohan")
#Printing Hello Word (the data inside brackets displays data and is called Console
bio_age="I'm 18 Years Old"
#bio_age is a variable that stores data into it
print(bio_age)
#printing variables 
bio_age="I'll be 19 next year"
bio_school="I'm a student of Shree Jain Vidyalaya"
print(bio_age)
#we can add strings with string during as well as add custom values during print command
print(bio_age + bio_school)
print(bio_school + " but previously  was a student of Calcutta Anglo Gujarati School")
#dont use quotations ("") for algebraic around numbers
print(12 + 12)
#We can set any feature on or off by simply adding true or falso command that'll be stored in a variable without any quotations
powered_on = True
print("Current system Status:")
print(powered_on)
#Similarly, use not in front of True/False to negate their values
print("Now:")
print(not powered_on)
#comparing inputs and expected datas are done with a operater ==
entered_pin=2048
expected_pin=2039
print("System Password Check:")
print(entered_pin == expected_pin)
#compared results can be commanded  not equal by using != display
print("Is Password Wrong:")
print(entered_pin != expected_pin)
#We can also compare numbers by using <,> as well as <=, >=
print("Question: 23 < 6?")
print(23 < 6)
print("Question: Check if 23 is less than equal to 100")
print(23 <= 100)
#apart from nunber, strings can also be checked! by simply using == and if isnt equal to the value expected then !=
expected_answer="apple"
entered_answer="mango"
print("Check if entered answer is same as expected!")
print(expected_answer == entered_answer)
print("Is the answer incorrect?")
print(expected_answer != entered_answer)
#Strings, numbers are collectively called Types
#Now we can add two types i.e. strings and numbers using a specially designed formatted string
notification = (f"You have {6} unread messages")
print(notification)
#Conditions, the one that decides whether  run or skip a line of code using If True/False: and adding two spaces before next line to form code block
newsletter = (f"You have {7} New Friend Request")
frequency = 6 <= 9
if True:
  print(newsletter)
input_a = "Kolkata"
input_b = "Delhi"
print("User Input: Kolkata")
if input_a == "Kolkata":
  print("You're on the right track")
print("User Input: Delhi")
if input_b != "Kolkata":
  print("Sorry, You're Going Wrong")
#simply use a default response for all returning false in If statement, with the help of If/else statement
input_c = "Mohali"
if input_a != "Kolkata":
  print("Yay, You're on Right Track")
else:
  print("Sorry You've Got a wrong Path")
#using elif gives a much more confined and narrowed answers!
print("Input is Kolkata")
if input_a == "Kolkata":
  print("You're Welcome")
elif input_b == "Delhi":
  print("Sorry, You're near National Capital")
else:
  print("Sorry, You need to check your route")
#in addition to if/else/elif statement, we may add an alternative conditions to the statement using or/and
input_d = "Bankura"
if input_a == "Kolkata" or input_d == "Bankura":
  print("You're Near")
if input_c == "Mohali" and input_b == "Delhi":
  print("You're Going Wrong!")
