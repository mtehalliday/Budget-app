#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:49:06 2023

@author: matthewhalliday
"""


class Category:
    
    def __init__(self, name):
        self.ledger = []
        self.name = name
        
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        total = 0
        total = sum(item["amount"] for item in self.ledger)
        return (total-amount) >= 0
              

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": (-1)*amount, "description": description})
            return True
        else:
            return False           
        
    def get_balance(self):
        total = 0
        total = sum(item["amount"] for item in self.ledger)
        return total
    
    def transfer(self, amount, cat):
        transfer_note1 = "Transfer to " + cat.name
        transfer_note2 = "Transfer from " + self.name
        if self.check_funds(amount):
            self.withdraw(amount, transfer_note1)
            cat.deposit(amount, transfer_note2)
            return True
        else:
            return False
        
    def __str__(self):
        #get length of category name, then calculate numberes of starts required on each side
        name_length = len(self.name)
        stars_number = int((30 - name_length)/2)
        header = stars_number * "*" + self.name + stars_number * "*" + "\n"
        return_string =""
        for items in self.ledger:
            return_string += f'{items.get("description")[:23]:23}' + f'{items.get("amount"):7.2f}' + "\n"
        footer = f"Total: {self.get_balance():.2f}"
        return header + return_string + footer
    
    
def create_spend_chart(cat_list):
    withdrawals = [sum(i.get("amount") for i in cat.ledger if i.get("amount") < 0) for cat in cat_list]
#    print(withdrawals)
    percent_withdrawal = [round(100*i/sum(withdrawals)) for i in withdrawals]
    names = [cat.name for cat in cat_list]
    chart = "Percentage spent by category\n"
    for num in range(100, -10, -10):
        chart += str(num).rjust(3) + "| " 
        for j in range(len(percent_withdrawal)):
            if percent_withdrawal[j] >= num:
                chart += ('o  ')
            else:
                chart += ("   ")
        chart += "\n"
    chart += 4*" " + 2*"-"*len(percent_withdrawal)+2*"-" +2*"-" + "\n"
    name_lengths = [len(i) for i in names]
    length_para = max(name_lengths)
    names_w_spaces = [i.ljust(length_para) for i in names]
    for j in range(length_para):
        chart += 5*" "
        for i in range(len(percent_withdrawal)):
            chart += names_w_spaces[i][j] + "  " 
        chart += "\n"
    
#    print(percent_withdrawal[1])
    return chart[:-1]
   
    
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")


food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])


expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
print(actual)
print(expected)
""" The below seems to work perfectly
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))
"""

