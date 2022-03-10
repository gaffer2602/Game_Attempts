import random
print('Welcome to "Guess The Number"')
print('Choose Your Difficulty')
difficulty_chosen = False
answer = 0
game_active = True
em_streak = 0
hm_streak = 0
gm_streak = 0
im_streak = 0
end_reason = 0
user_guess = 0


while True:
  
  while game_active == True:
    
    while difficulty_chosen == False:
      
      choice = (input('"Easy Mode", "Hard Mode", or "Gambler Mode"? ')).upper()
      user_guess = 0
      
      if choice == 'EASY MODE':
        print("Taking The Easy Route, Are We? Okay. I Guess You Don't Want A Challenge.")
        difficulty_chosen = 'Easy Mode'
        lives = 5
        tries = 1
        
      elif choice == 'EASY':
        print("Taking The Easy Route, Are We? Okay. I Guess You Don't Want A Challenge.")
        difficulty_chosen = 'Easy Mode'
        lives = 5
        tries = 1
        
      elif choice == 'HARD MODE':
        print('Brilliant, Brilliant. This Is Where The Fun Begins')
        difficulty_chosen = 'Hard Mode'
        lives = 5
        tries = 1
        
      elif choice == 'HARD':
        print('Brilliant, Brilliant. This Is Where The Fun Begins')
        difficulty_chosen = 'Hard Mode'
        lives = 5
        tries = 1
        
      elif choice == 'GAMBLER MODE':
        print("You're Gonna Have A Bad Time")
        difficulty_chosen = 'Gambler Mode'
        lives = 2
        tries = 1
        
      elif choice == 'GAMBLER':
        print("You're Gonna Have A Bad Time")
        difficulty_chosen = 'Gambler Mode'
        lives = 2
        tries = 1
        
      else:
        print('Invalid Input')
        difficulty_chosen = 'Impossible Mode'
        print('Difficulty Chosen: ', difficulty_chosen)
        lives = 1
        tries = 1
        
    while difficulty_chosen == 'Easy Mode':
      
      answer = random.randint(1, 10)
      print(answer)

      while user_guess != answer:
      
        if lives == 0:
          print('Game Over')
          game_active = False
          end_reason = 'EM: Loss'
          em_streak = 0
          print(answer)
          difficulty_chosen = 0
          
        else:
          print('Try: ', tries, ';', 'Lives Remaining: ', lives)
          user_guess = int(input('Pick A Number Between 1 & 10: '))
          
        if user_guess > 10:
          print('Invalid. Too High.')
          tries += 1
          
        elif user_guess < 1:
          print('Invalid. Too Low.')
          tries += 1
          
        elif user_guess < answer:
          if lives > 1:
            print('Too Low. Guess Higher')
            tries += 1
            lives -= 1
          elif lives == 1:
            print('Too Low. No Lives Remaining.')
            lives -= 1
            
        elif user_guess > answer:
          if lives > 1:
            print('Too High. Guess Lower.')
            tries += 1
            lives -= 1
          elif lives == 1:
            print('Too High. No Lives Remaining.')
            lives -= 1
            
        elif user_guess == answer:
          if lives > 1:
            print('Correct!')
            em_streak += 1
            print('Easy Mode Streak:', em_streak)
            print('Lives To Spare:', lives)
            game_active = False
            end_reason = 'EM: Win'
            difficulty_chosen = 0
            
          elif lives == 1:
            print('Just In The Nick Of Time. Correct!')
            em_streak += 1
            print('Easy Mode Streak:', em_streak)
            print('Lives To Spare:', lives)
            game_active = False
            end_reason = 'EM: Win'
            difficulty_chosen = 0
          
          
  
    while difficulty_chosen == 'Hard Mode':
      
      answer = random.randint(1, 100)
      print(answer)
      while user_guess != answer:
        
        if lives == 0:
          print('Game Over')
          game_active = False
          end_reason = 'HM: Loss'
          hm_streak = 0
          print(answer)
          difficulty_chosen = 0
          
        
        else:
          print('Try: ', tries, ';', 'Lives Remaining: ', lives)
          user_guess = int(input('Pick A Number Between 1 & 100: '))
          
          if user_guess > 100:
            print('Invalid. Too High.')
            tries += 1
            
          elif user_guess < 1:
            print('Invalid. Too Low.')
            tries += 1
            
          elif user_guess < answer:
            if lives > 1:
              print('Too Low. Guess Higher.')
              tries += 1
              lives -= 1  
            elif lives == 1:
              print('Too Low. No Lives Remaining.')
              lives -= 1
              
          elif user_guess > answer:
            if lives > 1:
              print('Too High. Guess Lower.')
              tries += 1
              lives -= 1
            elif lives == 1:
              print('Too High. No Lives Remaining.')
              lives -= 1
              
          elif user_guess == answer:
            if lives > 1:
              print('Correct!')
              hm_streak += 1
              print('Hard Mode Streak: ', hm_streak)
              print('Lives To Spare: ', lives)
              game_active = False
              end_reason = 'HM: Win'
              difficulty_chosen = 0
            elif lives == 1:
              print('Just About. Correct!')
              hm_streak += 1
              print('Hard Mode Streak: ', hm_streak)
              print('Lives To Spare:', lives)
              game_active = False
              end_reason = 'HM: Win'
              difficulty_chosen = 0
          
    while difficulty_chosen == 'Gambler Mode':

      answer = random.randint(1,100)
      print(answer)
      while user_guess != answer:
      
        if lives == 0:
          print('Game Over')
          game_active = False
          end_reason = 'GM: Loss'
          gm_streak = 0
          print(answer)
          difficulty_chosen = 0
          user_guess = 0
  
        else:
          print('Try:', tries, ';', 'Lives Remaining: ', lives)
          user_guess = int(input('Pick A Number Between 1 & 100: '))
  
          if user_guess > 100:
            print('Invalid. Too High.')
            tries += 1
  
          elif user_guess < 1:
            print('Invalid. Too Low.')
            tries += 1
  
          elif user_guess < answer:
            if lives > 1:
              print('Too Low. Guess Higher.')
              tries += 1
              lives -= 1
            elif lives == 1:
              print('Too Low. No Lives Remaining.')
              lives -= 1
  
          elif user_guess > answer:
            if lives > 1:
              print('Too High. Guess Lower.')
              tries += 1
              lives -= 1
            elif lives == 1:
              print('Too High. No Lives Remaining.')
              lives -= 1
  
          elif user_guess == answer:
            if lives > 1:
              print('Correct!')
              gm_streak += 1
              game_active = False
              end_reason = 'GM: Win'
              print(gm_streak)
              difficulty_chosen = 0
            elif lives == 1:
              print('Lucky! Correct!')
              gm_streak += 1
              game_active = False
              end_reason = 'GM: Win'
              print(gm_streak)
              difficulty_chosen = 0

    while difficulty_chosen == 'Impossible Mode':

      answer = random.randint(1,1000)
      print(answer)
      print('Lives Remaining: ', lives)
      print('Try: ', tries)
      
      while user_guess != answer:
      
        user_guess = int(input('Guess The Number Between 1 & 1000 '))
  
        if user_guess < 1:
          print('Invalid Answer. Too Low.')
          tries += 1
        elif user_guess > 1000:
          print('Invalid Answer. Too High.')
          tries += 1
        elif user_guess < answer:
          print('Too Low. Game Over.', answer)
          im_streak = 0
          game_active = False
          end_reason = 'IM: Loss'
          difficulty_chosen = 0
        elif user_guess > answer:
          print('Too High. Game Over.', answer)
          im_streak = 0
          game_active = False
          end_reason = 'IM: Loss'
          difficulty_chosen = 0
        elif user_guess == answer:
          if im_streak == 0: 
            print('You Got Lucky. Correct!')
            im_streak += 1
            game_active = False
            end_reason = 'IM: Win'
            print(im_streak)
            difficulty_chosen = 0
          else:
            print('Are You Hacking?')
            im_streak += 1
            game_active = False
            end_reason = 'IM: Win'
            print(im_streak)
            difficulty_chosen = 0

  while game_active == False:
    if end_reason == 'EM: Loss':
      retry = (input('You Lost On Easy! Try Again? ')).lower()
      if retry == 'yes':
        print('Very Well, Then.')
        game_active = True
        difficulty_chosen = False
      elif retry == 'no':
        print('Goodbye')
        game_active = 5
      else:
        print("I'll Take That As A Yes.")
        print("I'm Also Going To Reset All Your Scores")
        game_active = True
        difficulty_chosen = False
        em_streak = 0
        hm_streak = 0
        im_streak = 0
        gm_streak = 0

    elif end_reason == 'EM: Win':
      retry = (input('You Won!! On Easy, Though. Try Again? ')).lower()
      if retry == 'yes':
        print('Very Well, Then.')
        game_active = True
        difficulty_chosen = False
      elif retry == 'no':
        print('Goodbye')
        game_active = 5
      else:
        print("I'll Take That As A Yes.")
        print("I'm Also Going To Reset All Your Scores")
        game_active = True
        difficulty_chosen = False
        em_streak = 0
        hm_streak = 0
        im_streak = 0
        gm_streak = 0

    elif end_reason == 'HM: Loss':
      retry = (input('You Lost On Hard. Would You Like Another Chance? ')).lower()
      if retry == 'yes':
        print('Very Well, Then.')
        game_active = True
        difficulty_chosen = False
      elif retry == 'no':
        print('Goodbye')
        game_active = 5
      else:
        print("I'll Take That As A Yes.")
        print("I'm Also Going To Reset All Your Scores")
        game_active = True
        difficulty_chosen = False
        em_streak = 0
        hm_streak = 0
        im_streak = 0
        gm_streak = 0

    elif end_reason == 'HM: Win':
      retry = (input('You Beat Hard. Try Again? ')).lower()
      if retry == 'yes':
        print('Very Well, Then.')
        game_active = True
        difficulty_chosen = False
      elif retry == 'no':
        print('Goodbye')
        game_active = 5
      else:
        print("I'll Take That As A Yes.")
        print("I'm Also Going To Reset All Your Scores")
        game_active = True
        difficulty_chosen = False
        em_streak = 0
        hm_streak = 0
        im_streak = 0
        gm_streak = 0

    elif end_reason == 'GM: Loss':
      retry = (input("You Took A Gamble And It Didn't Pay Off. Do You Want Another Chance? ")).lower()
      if retry == 'yes':
        print('Very Well, Then.')
        game_active = True
        difficulty_chosen = False
      elif retry == 'no':
        print('Goodbye')
        game_active = 5
      else:
        print("I'll Take That As A Yes.")
        print("I'm Also Going To Reset All Your Scores")
        game_active = True
        difficulty_chosen = False
        em_streak = 0
        hm_streak = 0
        im_streak = 0
        gm_streak = 0

    elif end_reason == 'GM: Win':
      retry = (input('Congratulations! Your Gamble Paid Off!! Another Round? ')).lower()
      if retry == 'yes':
        print('Very Well, Then.')
        game_active = True
        difficulty_chosen = False
      elif retry == 'no':
        print('Goodbye')
        game_active = 5
      else:
        print("I'll Take That As A Yes.")
        print("I'm Also Going To Reset All Your Scores")
        game_active = True
        difficulty_chosen = False
        em_streak = 0
        hm_streak = 0
        im_streak = 0
        gm_streak = 0

    elif end_reason == 'IM: Loss':
      retry = (input('That Was To Be Expected. One More Try? ')).lower()
      if retry == 'yes':
        print('Very Well, Then.')
        game_active = True
        difficulty_chosen = False
      elif retry == 'no':
        print('Goodbye')
        game_active = 5
      else:
        print("I'll Take That As A Yes.")
        print("I'm Also Going To Reset All Your Scores")
        game_active = True
        difficulty_chosen = False
        em_streak = 0
        hm_streak = 0
        im_streak = 0
        gm_streak = 0

    elif end_reason == 'IM: Win':
      retry = (input("How? Let Me Guess, You're Going To Try Get That High Again? ")).lower()
      if retry == 'yes':
        print('Very Well, Then.')
        game_active = True
        difficulty_chosen = False
      elif retry == 'no':
        print('Goodbye')
        game_active = 5
      else:
        print("I'll Take That As A Yes.")
        print("I'm Also Going To Reset All Your Scores")
        game_active = True
        difficulty_chosen = False
        em_streak = 0
        hm_streak = 0
        im_streak = 0
        gm_streak = 0
