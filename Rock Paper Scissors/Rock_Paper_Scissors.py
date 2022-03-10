import random
game_active = True
weapons = ['Rock', 'Paper', 'Scissors']
invalid_else_quips = ["Ha, Ha. Yes. Die Trash.", "We're No Strangers To Love", "You're Trash", "Get Dunked On", "One Does Not Simply 'Nyeh, Heh, Heh'"]
computer_score = 0
user_score = 0
print('Welcome To Rock, Paper, Scissors')
while True:
    while game_active == True:
        computer_choice = random.choice(weapons)

        user_choice = 0
        retry = 0
        end_reason = 0
        validity_check = 'Active'
        invalid_attempts = 0

        while validity_check == 'Active':
            if invalid_attempts == 5:
                print('Could Not Validate Answers. You Shall Now Be Ejected')
                validity_check = 'Inactive, Failed'
            else:
                user_choice = (input('Rock, Paper, or Scissors. ')).upper()
                if user_choice == 'ROCK':
                    user_choice = 'Rock'
                    validity_check = 'Inactive, Passed'
                elif user_choice == 'PAPER':
                    user_choice = 'Paper'
                    validity_check = 'Inactive, Passed'
                elif user_choice == 'SCISSORS':
                    user_choice = 'Scissors'
                    validity_check = 'Inactive, Passed'
                else:
                    print('Invalid Choice')
                    invalid_attempts += 1


        if validity_check == 'Inactive, Failed':
            print('I Find Your Lack of Faith Disturbing')
            game_active = False
            end_reason = 'Invalid'
            break
        elif validity_check == 'Inactive, Passed':
            print('It Is... Acceptable')


        while user_choice == 'Rock':
            print('You Have Chosen: "Rock"')
            if computer_choice == 'Rock':
                print('Tie')
                game_active = False
                end_reason = 'Tie'
                break
            elif computer_choice == 'Paper':
                print('Paper Covers Rock. You Have Lost.')
                game_active = False
                end_reason = 'Loss'
                break
            elif computer_choice == 'Scissors':
                print('Rock Smashes Scissors. You Have Won.')
                game_active = False
                end_reason = 'Win'
                break

        while user_choice == 'Paper':
            print('You Have Chosen: Paper')
            if computer_choice == 'Rock':
                print('Paper Covers Rock. You Have Won.')
                game_active = False
                end_reason = 'Win'
                break
            elif computer_choice == 'Paper':
                print('Tie')
                game_active = False
                end_reason = 'Tie'
                break
            elif computer_choice == 'Scissors':
                print('Scissors Cuts Paper. You Have Lost.')
                game_active = False
                end_reason = 'Loss'
                break

        while user_choice == 'Scissors':
            print('You Have Chosen: Scissors')
            if computer_choice == 'Rock':
                print('Rock Smashes Scissors. You Have Lost.')
                game_active = False
                end_reason = 'Loss'
                break
            elif computer_choice == 'Paper':
                print('Scissors Cuts Paper. You Have Won.')
                game_active = False
                end_reason = 'Win'
                break
            elif computer_choice == 'Scissors':
                print('Tie')
                game_active = False
                end_reason = 'Tie'
                break

    while game_active == False:
        print(user_score, computer_score)
        if end_reason == 'Tie':
            retry = (input('There Is No Winner. Try Again? ')).lower()
            if retry == 'yes':
                print('Very Well')
                game_active = True
                end_reason = 0
            elif retry == 'no':
                print("Well That's A Shame. Goodbye, Then")
                end_reason = 0
            else:
                print("It's Treason, Then")
                end_reason = 0
        elif end_reason == 'Win':
            user_score += 1
            retry = (input('Congratulations! You Have Won. Try Again? ')).lower()
            if retry == 'yes':
                print('Do You Just Want To Keep Going?')
                game_active = True
                end_reason = 0
            elif retry == 'no':
                print("I Get It. You Want To Quit While You're Ahead.")
                end_reason = 0
            else:
                print("Why Won't You Answer Me?")
                end_reason = 0
        elif end_reason == 'Loss':
            computer_score += 1
            retry = (input("Stings, Doesn't It? You Have Lost. Try Again? ")).lower()
            if retry == 'yes':
                print("You'll Get Your Win When You Fix Your Damn Skill!")
                game_active = True
                end_reason = 0
            elif retry == 'no':
                print('Look At Little Goblin Junior. Gonna Cry?')
                end_reason = 0
            else:
                print("I'm gonna put some dirt in your eye!")
                end_reason = 0
        elif end_reason == 'Invalid':
            retry = (input('Are You Going To Behave If I Let You Try Again? ' )).lower()
            if retry == 'yes':
                print('Good')
                game_active = True
                end_reason = 0
            elif retry == 'no':
                print('Puny Child')
                end_reason = 0
            else:
                print(random.choice(invalid_else_quips))
                end_reason = 0
