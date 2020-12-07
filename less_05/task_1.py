with open("text_task1.txt", 'w') as out_f:
    while True:
        text = input('Enter text or "Enter" for exit: ')
        if text == '':
            break
        print(text, file=out_f)
