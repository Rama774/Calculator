def multiplication(x,y):
 print(x*y)
def summation(x,y):
 print(x + y)
def partition(x,y):
 print(x/y)
def subtraction(x,y):
 print(x-y)

global count
count=0

while True:

  a=input('choose what you want (-,+,*,/)')
  x= int(input('choose number 1'))
  y= int(input('choose number 2'))
  if a=='*':
    multiplication(x,y)
    count = count + 1
    h = input("Do you need more help?")
    if h == 'no':
        print(f" we are happy to help you with {count} proplems ")
        break

    if a=='+':
      summation(x,y)
      count = count + 1
      h = input("Do you need more help?")
      if h == 'no':
          print(f" we are happy to help you with {count} proplems ")
          break
  if a=="/":
      partition(x,y)
      count=count+1
      h = input("Do you need more help?")
      if h == 'no':
          print(f" we are happy to help you with {count} proplems ")
          break
  if a=='-':
      subtraction(x,y)
      count=count+1
      h = input("Do you need more help?")
      if h == 'no':
          print(f" we are happy to help you with {count} proplems ")
          break







