#! /opt/homebrew/bin/python3

from Information import *
from Ordering import *


if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Purchase SMS")
        print("3. Check SMS status")
        print("4. Cancel SMS")
        print("5. Information")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            purchase_sms(1, 671)
        elif choice == "2":
            active_orders()
        elif choice == "3":
            order_id = input("Enter Order ID: ")
            check_sms(order_id)
        elif choice == "4":
            order_id = input("Enter Order ID: ")
            cancel_sms(order_id)
        elif choice == "5":
            print("\nChoose an option:")
            print("1. Get Country")
            print("2. Get Service")
            print("3. My active orders endpoint")
            serviceChoice = input("Enter your choice: ")
            if serviceChoice == "1":
                get_countries()
            elif serviceChoice == "2":
                get_services()
            elif choice == "3":
                active_orders()
            else:
                break
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
