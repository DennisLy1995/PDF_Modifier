import Tools.PDF_Modifier as modifier

breaker = False
mod = modifier.PDF_Modifier()

def cut_PDF():
    mod.cutPDF()
    return True


def join_PDF():
    mod.joinPDF()
    return True


def copy_PDF():
    mod.copyPDF()
    return True


def selector(x):
    if x == '1':
        cut_PDF()
    elif x == '2':
        join_PDF()
    elif x == '3':
        copy_PDF()
    elif x == '4':
        print('      Thanks for using the tool')
    else:
        print('Please enter one option from the menu!!!')

"""Here starts the menu process"""

while not breaker:
    print("""
PDF MODIFIER
    1. Cut PDF
    2. Join PDF
    3. Copy PDF
    4. Exit
""")
    urd = input()
    selector(urd)
    if urd == "4":
        breaker = True
