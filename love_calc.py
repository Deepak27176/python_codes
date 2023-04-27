# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name1.lower()
name2=name2.lower()
T=name1.count('t')+name2.count('t')
R=name1.count('r')+name2.count('r')
U=name1.count('u')+name2.count('u')
E=name1.count('e')+name2.count('e')
T=T+R+U+E
L=name1.count('l')+name2.count('l')
O=name1.count('o')+name2.count('o')
V=name1.count('v')+name2.count('v')
E=name1.count('e')+name2.count('e')
L=L+O+V+E
score=T*10+L
if score<10 or score>90:
  print(f" love score  is:{score}you go together like coke and mentos")
elif score>40 and score<50:
  print(f" love score is:{score} you are alright together")
else:
  print(f" love score is:{score}")
