def print_dashes():
    print('------------------------------')


def print_head():
    print('CASH RECEIPT')
    print_dashes()


def print_body():
    print('Charged to____________________')
    print('Received by___________________')


def print_footer():
    print_dashes()
    print('© SoftUni')


def print_cash():
    print_head()
    print_body()
    print_footer()


print_cash()
