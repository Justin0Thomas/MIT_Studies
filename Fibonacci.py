# Created on Tues Oct 4 2021
# Justin Thomas 
# Shows a user defined number of Fibonacci sequence numbers
def fibonacci(uptonumber):
  # Zero is a special case
  if(uptonumber == 0):
    print("You must enter a positive whole number")
  #set the first value of a
  a = 0
  # then 1 being the second
  # of the first two numbers in
  # the sequence
  b = 1
  # make sure c is null initially
  c = 0
  for n in range(1,uptonumber):
     print(a)
     c = (a + b)
     a = b
     b = c

uptonumber = int(input("How many fibonacci numbers?: "))
fibonacci(uptonumber)
 
 
