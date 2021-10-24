#coding: utf-8
import random


print('Welcome to Your Password Generator')

chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('Amount of Passwords to Generate: ')
number = int(number)

length = input('Input your Password lenght: ')
length = int(length)


print('\n Here is Your Password: ')


for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
print(passwords)
 