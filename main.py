# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

T_count = str(name1 + name2).lower().count('t')
R_count = str(name1 + name2).lower().count('r')
U_count = str(name1 + name2).lower().count('u')
E_count = str(name1 + name2).lower().count('e')
true_count = int(T_count)+int(R_count)+int(U_count)+int(E_count)
L_count = str(name1 + name2).lower().count('l')
O_count = str(name1 + name2).lower().count('o')
V_count = str(name1 + name2).lower().count('v')
E_count = str(name1 + name2).lower().count('e')
love_count = int(L_count)+int(O_count)+int(V_count)+int(E_count)

total = str(true_count) + str(love_count)

if int(total) < 10 or int(total) > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif int(total) >=40 and int(total) <=50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")

