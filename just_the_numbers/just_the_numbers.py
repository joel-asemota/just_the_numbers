def accumulating():
  List = []
  Strings = input("Please enter a list of strings: ")
  List = Strings.split(" ")
  return List

def length(n):
  r = []
  for i in n:
    r.append(len(n))
  return r

def main():
  y = accumulating()
  x = length(y)
  print(x)

main()
