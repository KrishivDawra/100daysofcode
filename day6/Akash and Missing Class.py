school=int(input())
for s in range(school):
  w=int(input())
  if w%7==6:
      s=w//7+1
      print(s)
  else: 
      s=w//7
      print(s)
