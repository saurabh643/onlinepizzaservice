# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 21:26:15 2020

@author: Saurabh
"""
print("WELCOME TO MY ONLINE PIZZA DILEVERY SERVICE")
print("\nFOR NOW WE ONLY HAVE TWO TOPPINGS:")
print("\nmushrooms \ extra cheese")
requested_toppings = ['mushrooms','extra cheese']
# =============================================================================
# for topping in requested_toppings: 
#     topping=input()
# =============================================================================
requested_toppings=input()
if'mushrooms'in requested_toppings:
     print("Adding mushrooms.")
elif'extra cheese'in requested_toppings:
    print('Adding extra cheese.')
print("\nFinished ,thanks for purchasing!")