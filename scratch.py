stock_list = []

print(stock_list)

number_added = int(input("How many item you want to add? : "))

for add in range(number_added):
    name_added = str(input("Item name : "))
    stock_list.append(name_added)

print("Item in stock is")
for show in stock_list:
    print(,show)

print("End Program")
