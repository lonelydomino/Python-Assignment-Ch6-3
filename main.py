#Write Python code to get 2 inputs x and y.  Check if both are positive.  If yes then display the larger of the two

x = input("Please enter x: ")
y = input("Please enter y: ")

if int(x) > 0 and int(y) > 0:
  if x > y:
    print("The greater number is " + x)
  else:
    print("The greater number is " + y)
