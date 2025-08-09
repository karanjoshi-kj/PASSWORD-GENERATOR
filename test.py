# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 15:40:18 2023

@author: sidhu
"""

def maincode():
    print("Hello to main Code!!")

print("\n")
while True:
    print('*' * 60)
    print(
        "Password must fulfill the given Criteria!!!\n\n"
        "1. Password length should not be less than 8 characters\n\n"
        "2. Password must contain one uppercase letter and one lowercase letter\n\n"
        "3. Password must contain at least one number from 0-9\n\n"
        "4. Special characters allowed: @ $ _ ! ."
    )
    print('*' * 60 + "\n")

    enterenedpassword = input("Create your Password : ")
    lowercase, uppercase, specialchar, digit = 0, 0, 0, 0
    allowed_specials = ['@', '$', '_', '!', '.']

    if len(enterenedpassword) >= 8:
        for i in enterenedpassword:
            if i.islower():
                lowercase += 1
            elif i.isupper():
                uppercase += 1
            elif i.isdigit():
                digit += 1
            elif i in allowed_specials:
                specialchar += 1

    # Only allowed characters check
    total_count = lowercase + uppercase + digit + specialchar
    if (lowercase >= 1 and uppercase >= 1 and specialchar >= 1 and digit >= 1 and total_count == len(enterenedpassword)):
        confirmpassword = input("Confirm Password: ")
        if enterenedpassword == confirmpassword:
            try:
                print("Password accepted successfully!\n")
                maincode()
            except Exception as e:
                print(f"Error !! {e}")
        else:
            print("Error!! Confirm password does not match with the Password.\nPlease Try again.")
    else:
        print("Sorry !! Your password does not match our given criteria!!\n")