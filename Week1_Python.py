from Create_Array import create_cus_array
from Create_Array import create_payments_array
from Print_Report import print_report_header
from Print_Report import print_menu
from Print_Report import print_report_bottom
from Print_Report import print_customer_payment_history
from Print_Report import return_account_index

random = [39, 46, 10, 37, 33, 4, 30, 26, 14, 19, 29, 6, 43, 8, 35, 50, 13,
          25, 17, 48, 28, 3, 41, 34, 36, 38, 49, 16, 45, 2, 40, 15, 24, 7,
          5, 9, 20, 1, 42, 44, 21, 47, 12, 22, 18, 31, 11, 32, 27, 23]

correct = False

while not correct:
    num = input("Please enter a number between 1 and 50: ")
    if 0 < int(num) <= 50:
        correct = True

for number in random:
    if int(num) == number:
        index = random.index(int(number))

print("Your number: " + num + " is found in the index: " + str(index) + " of the array.")

customers = create_cus_array()
payments = create_payments_array()

stop1 = False
stop2 = False

while not stop1:
    print_menu()
    user_input = int(input("Enter 1, 2, 3, or 4 here: "))
    if user_input == 1:
        account_number = int(input("Enter the account number: "))
        index = return_account_index(payments, account_number)
        if int(index) == -1:
            print("Account number not found")
        else:
            print_report_header()
            print_customer_payment_history(customers, payments, index)
            print_report_bottom()
    elif user_input == 2:
        contains_zero = False
        index = 0
        print_report_header()
        for row in payments:
            for col in row:
                if col == 0:
                    contains_zero = True
                    break
            if contains_zero:
                print_customer_payment_history(customers, payments, index)
                contains_zero = False
            index += 1
        print_report_bottom()
    elif user_input == 3:
        zero_count = 0
        index = 0
        print_report_header()
        for row in payments:
            for col in row:
                if col == 0:
                    zero_count += 1
                    if zero_count >= 3:
                        break
            if zero_count >= 3:
                print_customer_payment_history(customers, payments, index)
            index += 1
            zero_count = 0
        print_report_bottom()
    elif user_input == 4:
        print("Goodbye.")
        stop1 = True


