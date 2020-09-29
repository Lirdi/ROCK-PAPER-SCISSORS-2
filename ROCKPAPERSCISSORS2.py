#Refined version
import random
#Users input
while True:
    choice = input("Alright lets play rock paper scissors : ")
    choice = choice.lower()
    print("You chose", choice)

    # Computers Turn
    choices = ["rock", "paper", "scissors"]
    cc = choices[random.randint(0, len(choices) - 1)]
    print("Computer has chosen", cc)

    choice_dict = {"rock": 0, "paper": 1, "scissors": 2}

    choice_index = choice_dict.get(choice, 3)
    cc_index = choice_dict.get(cc)

    resultm = [[0,2,1] , [1,0,2] , [2,1,0] ,[3,3,3]]

    result_index = resultm[choice_index][cc_index]
    resultmessages = ["You Drew", "You Won", "You Lost"]
    results = resultmessages[result_index]

    print(results)


