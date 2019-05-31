secret_number = 9
guess_number = 0
guess_limit = 2
while guess_number < guess_limit:
    guess = input("Enter number to guess :")
    guess_number +=1
    if guess == secret_number:
        print("Bingo you are win!!!")
        break
else:
    print("So sad you are lost!!")