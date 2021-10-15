expenses = [10.50,8,5, 15, 20, 5, 3]
Sum = 0
del expenses[3]
print(expenses)

for each_expense in expenses:
    Sum = Sum + each_expense

print("You spend  $", Sum, sep='')


expenses_list = []
for i in range(2):
    expenses_list.append(int(input("Enter the expense on each day of the week")))

total = sum(expenses_list)
print("You spend $", total, sep='')
