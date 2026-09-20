import random 
import sys

snake=0
water=1
gun=2

choices=(0,1,2)
#Computer choice
AI=random.choice(choices)

#User choice
user=input("Enter your choice: ").lower()
if user=="snake":
  user=0
elif user=="water":
  user=1
elif user=="gun":
  user=2
elif user=="0":
  user=0
elif user=="1":
  user=1
elif user=="2":
  user=2
else:
  print("Invalid input")
  sys.exit()

print("Computer choosed: ",AI)
print("Player choosed: ",user)

matrix=[
    ["Draw","Win","Lose"],
    ["Lose","Draw","Win"],
    ["Win","Lose","Draw"]
]

select=matrix[AI][user]
print(select)