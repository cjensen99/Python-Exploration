def print_report_header():
    print("\n---------------------------------------------------------------------------------------\n"
          + "Customer Payment History\n"
          + "---------------------------------------------------------------------------------------")


def return_standing(count):
    if count == 0:
        return "Good"
    if count == 1:
        return "Fair"
    if count == 2:
        return "Poor"
    else:
        return "Closed"


def print_customer_payment_history(customers, payments, index):
    count0 = 0
    counter = 1
    print("%-*s" % (18, customers[index]), end='')
    print(" %s" % (payments[index][0]), end='')
    while counter < 13:
        print(" " + str(payments[index][counter]), end='')
        if payments[index][counter] == 0:
            count0 += 1
        counter += 1
    print(" " + return_standing(count0))


def print_report_bottom():
    print("---------------------------------------------------------------------------------------")


def return_account_index(payments, account_number):
    count = 0
    for num in payments:
        if num[0] == account_number:
            index = count
            return int(index)
        count += 1
    return -1


def print_menu():
    print("\n-------------------------------------------------\nCustomer Menu\n"
          + "1. Find customer by account number.\n"
          + "2. Report customers with any missed payments\n"
          + "3. Report customers with \"Closed\" status.\n"
          + "4. Exit\n"
          + "-------------------------------------------------\n")
