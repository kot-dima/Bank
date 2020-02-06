# class Person:
#     name = "Bill"
#     def Show_Person(self):
#         print("Hello", self.name)

# Bill = Person()
# Bill.Show_Person()

# Tom = Person()
# Tom.Show_Person()

# Tom.name = "Tom"
# Tom.Show_Person()


# class Person:
#     def __init__(self, name):
#         self.__name = name
#         print("Person constructor -", self.__name)
#     def Show_Person(self):
#         print("Hello", self.__name)
#     def __del__(self):
#         print("Person destructor -", self.__name)
        
# Jack = Person("Jack")
# Jack.Show_Person()
# Bobik = Person("Bobik")
# Bobik.Show_Person()

# print(Jack.__name)


# class Person:
#     def __init__ (self, name):
#         self.__name = name
#     def set_name(self, new_name):
#         if self.__name == new_name:
#             print("The same name")
#         else:
#             self.__name = new_name
#     def get_name(self):
#         return self.__name

# Bill = Person("Bill")
# print(Bill.get_name())
# print(Bill.set_name("John"))



from random import randint

class Account:
    def __init__(self, card_number, amount, currency, minus):
        self.__card_number = card_number
        self.__amount = amount
        self.__currency = currency
        self.__minus = minus
        self.__add_money = add_money
        print("Account constructor")

    def show_info(self):
        print("Card number: ", self.__card_number, "\nAmount: ", self.__amount, "\nCurrancy: ", self.__currency, "\nMinus: ", self.__minus, "\nAdd Money: ", self.__add_money)

card_number = randint(537500000000, 537599999999)
amount = int(input("Enter money : "))
currancy = input("Enter currancy: UAH USD EUR - ")
minus = int(input("Enter how many maney : "))
add_money = int(input("Enter how many add : "))

credit_card = Account(card_number, amount, currancy, minus, add_money)
credit_card.show_info()

# def yourMoney = amount - minus
# print(card_number, yourMoney, )




