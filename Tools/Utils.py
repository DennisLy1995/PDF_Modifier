def ask(message):
    x = False
    answer = False
    while not x:
        rd = input(message)
        if rd == '1' or rd.lower() == 'yes':
            answer = True
            x = True
        elif rd == '2' or rd.lower() == 'no':
            answer = False
            x = True
        else:
            print('WARN: Invalid option.')
    return answer

