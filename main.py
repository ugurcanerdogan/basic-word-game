import sys

sys.argv = ["alchemist", "ladybug", "squirrel"]
flag = True
if len(sys.argv) != 3:
    exit("Please run with 3 arguments")
if len(sys.argv[0]) == len(sys.argv[1]) or len(sys.argv[0]) == len(sys.argv[2]) or len(sys.argv[1]) == len(sys.argv[2]):
    exit("Arguments should be a different length")
letters = []
for arg in sys.argv:
    for i in arg:
        letters.append(i)
        if not i.isalpha():
            flag = False
            print("Argument {} is not a word. All arguments should be word".format(arg))
            break
letters.sort()

while flag:
    print("Find longest word using letters given below \n", letters)
    a = input("Guess a longest word: ")
    if a == sys.argv[0]:
        print("You found a word from list \n"
              "You won 50 points!")

    elif a == sys.argv[1]:
        print("You found a word from list \n"
              "You won 10 points!")

    elif a == sys.argv[2]:
        print("You found a word from list \n"
              "You won 30 points!")

    else:
        print("The word you guessed is not in the list\n"
              "You lost!")













