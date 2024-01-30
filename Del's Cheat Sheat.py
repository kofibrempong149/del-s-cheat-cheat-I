#!/usr/bin/env python
# coding: utf-8

# ## PSEUOCODE

# In[ ]:


num = int(input("number")) 
if num % 15 == 0:
    print("Fizz Buzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print("error")


# ## CONTROL FLOW LOOPS (if elif and else condition)

# In[ ]:


a = int (input("exam score "))
if a > 80:
    print("A")
elif (a < 80) and (a > 75):
    print("B+")
elif (a < 75) and (a > 70):
    print("B")
elif (a < 70) and (a > 65):
    print("C+")
elif (a < 65) and (a > 60):
    print("C")
elif (a < 60) and (a > 55):
    print("D+")
elif (a < 55) and (a > 50):
    print("D")
else:
    print("E")


# ## CONTROL FLOW LOOPS (for and if conditions)

# In[ ]:


balance = 50000

for transaction in range(1, 11):
    print(f"Transaction {transaction}")
    withdrawal_amount = int(input("Enter withdrawal amount: "))
    service_charges = 0.10 
    total_withdrawal = withdrawal_amount + withdrawal_amount * service_charges
    if total_withdrawal > balance:
        print("Insufficient funds. Please try again.")
        continue
    remaining_balance = balance - total_withdrawal
    if remaining_balance < 0:
        remaining_balance = 0
    print(f"Withdrawal successful. Remaining balance: {remaining_balance}. THANK YOU FOR USING UMB")   
    break


# ## CONTROL FLOW LOOPS (NESTED if condition)

# In[ ]:


""""grouping customers < 18years into gender(male and female)"""
x = int(input("age"))
y = str(input("gender"))
if x < 18:
    if y == 'male':
        print("young male")
    elif y == 'female':
        print("young female")


# ## LISTS

# In[ ]:


My_list = ["apples", "oranges", "peach"]
My_list 


# In[ ]:


My_list.append("grapes")
My_list


# In[ ]:


My_list = ["apples", "oranges", "peach"]
My_list.extend(["eggs", "meat", "pepper"])
print(My_list)


# In[ ]:


My_list.insert(0, "ink")
My_list


# In[ ]:


My_list.remove("ink")
My_list


# In[ ]:




