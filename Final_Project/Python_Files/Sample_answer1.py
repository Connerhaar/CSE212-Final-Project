def undo_example():
    print("To continue writing hit enter twice, to undo hit enter and then type (u)")
    sentence = (input('Please start writing: '))
    stack = sentence.split()
    while True:
        choice = input("")

        if choice == '':
            phrase = " ".join(stack)
            new = input(f'{phrase} ').split()
            stack.extend(new)

        elif choice == 'u':
            stack.pop()
            print(*stack)
        else:
            return False


undo_example()



        

