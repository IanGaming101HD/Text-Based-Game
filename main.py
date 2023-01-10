import time
import timeit
import random

health = 100
start = timeit.default_timer()

def seconds_timer():
    print(str(int(timeit.default_timer() - start)) + ' seconds elapsed')

def continue_prompt():
    while True:
        answer = str(input('Would you like to continue? [Yes/No] > '))
        if(answer.lower() == 'no'):
            quit()
        elif(answer.lower() == 'yes'):
            time.sleep(2)
            break
        print('Try again!')

def intro():
    while True:
        answer = input('Would you like to start the game? [Yes/No] > ').lower()
        if(answer == 'no'):
            quit()
        elif(answer == 'yes'):
            time.sleep(2)
            break
        print('Try again!')
    intro_2()

def intro_2():
    username = input('First what is your name? > ')

    while True:
        time.sleep(2)
        print('Right...')
        time.sleep(2)
        confirmation = input('So your name is ' + username.upper() + '. [Yes/No] > ').lower()

        if(confirmation == 'yes'):
            time.sleep(2)
            print('Your very own adventure is about to unfold!')
            time.sleep(2)
            print('A world with infinite possibilities, Lets go!')
            time.sleep(2)
            continue_prompt()
            break
        elif(confirmation == 'no'):
            time.sleep(2)
            intro_2()
        else:
            print('Please state a valid answer!')
            continue
        return username

def play_again():
    while True:
        answer = input('Would you like to play again? [Yes/No] > ').lower()
        if(answer == 'yes'):
            time.sleep(2)
            start()
        elif(answer == 'no'):
            time.sleep(2)
            quit()
        print('Try again!')

def game_over(reason):
    print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
''')
    time.sleep(3)
    play_again()

def win(reason):
    print('''__     ______  _    _  __          ______  _   _   _
\ \   / / __ \| |  | | \ \        / / __ \| \ | | | |
 \ \_/ / |  | | |  | |  \ \  /\  / / |  | |  \| | | |
  \   /| |  | | |  | |   \ \/  \/ /| |  | | . ` | | |
   | | | |__| | |__| |    \  /\  / | |__| | |\  | |_|
   |_|  \____/ \____/      \/  \/   \____/|_| \_| (_)
                                                     ''')
    time.sleep(3)
    play_again()

def path():
    global health
    print('You have found your way through a path with lots of trees!')

    time.sleep(3)

    num = random.randint(1, 2)
    if(num == 1):
        print('You have continued across safely!')
        time.sleep(3)
        win('You have won!')
    elif(num == 2):
        print('You have stumbled yourself onto a nest of snakes!')
        time.sleep(3)
        while True:
            choice = input('What are you going to do? Fight the snakes, stay still, or run away from the snakes. [Fight, Stand, Run] > ').lower()
            if(choice != 'fight' and choice != 'stand' and choice != 'run'):
                print('Please state a valid option!')
                continue
            break

        if(choice == 'fight'):
            num = random.randint(1, 2)

            if(num == 1):
                health -= 75
                time.sleep(3)
                print('You have successfully killed all the snakes! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                win('You have won!')

            elif(num == 2):
                health -= 100
                time.sleep(3)
                print('You got poisoned by the snakes and slowly died, you currently have ' + str(health) + ' Health!')
                time.sleep(3)
                game_over('You have died!')

        elif(choice == 'stand'):
            num = random.randint(1, 2)

            if(num == 1):
                time.sleep(3)
                print('You successfully made no contact with all the snakes! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                time.sleep(2)
                win('You have won!')

            elif(num == 2):
                health -= 65
                time.sleep(3)
                print('The snakes have noticed you and bit you! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                time.sleep(2)
                win('You have won!')

        elif(choice == 'run'):
            num = random.randint(1, 2)

            if(num == 1):
                time.sleep(3)
                print('You successfully ran away from the snakes! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                time.sleep(2)
                win('You have won!')

            elif(num == 2):
                health -= 35
                time.sleep(3)
                print('The snakes have chased you and made contact with you! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                time.sleep(2)
                win('You have won!')

def path_2():
    global health
    print('You have went along a very narrow trail!')

    time.sleep(3)

    num = random.randint(1, 2)
    if(num == 1):
        print('You have continued across safely!')
        time.sleep(3)
        win('You have won!')
    elif(num == 2):
        print('You have spot a lion!')
        time.sleep(3)
        while True:
            choice = input('What do you do? Fight the lion, stay still, or run away from the lion. [Fight, Stand, Run] > ').lower()
            if(choice != 'fight' and choice != 'stand' and choice != 'run'):
                print('Please state a valid option!')
                continue
            break

        if(choice == 'fight'):
            num = random.randint(1, 2)

            if(num == 1):
                health -= 65
                time.sleep(3)
                print('You have successfully killed the lion! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                time.sleep(2)
                win('You have won!')

            elif(num == 2):
                health -= 100
                time.sleep(3)
                print('The lion has killed you! You currently have ' + str(health) + ' Health!')
                time.sleep(3)
                game_over('You have died!')

        elif(choice == 'stand'):
            num = random.randint(1, 2)

            if(num == 1):
                time.sleep(3)
                print('The lion did not notice you! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                time.sleep(2)
                win('You have won!')

            elif(num == 2):
                health -= 25
                time.sleep(3)
                print('The lion has noticed you and attacked you! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                time.sleep(2)
                win('You have won!')

        elif(choice == 'run'):
            num = random.randint(1, 2)

            if(num == 1):
                time.sleep(3)
                print('You successfully ran away from the lion! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                time.sleep(2)
                win('You have won!')

            elif(num == 2):
                health -= 75
                time.sleep(3)
                print('The lion has chased you and made contact with you! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                time.sleep(2)
                win('You have won!')

def path_3():
    global health
    print('You have found your way through a path with lots of trees!')

    time.sleep(3)

    num = random.randint(1, 2)
    if(num == 1):
        print('You have continued across safely!')
        time.sleep(3)
        win('You have won!')
    elif(num == 2):
        print('You have set your eyes on a huge bear!')
        time.sleep(3)
        while True:
            choice = input('What are you going to do? Fight the bear, stay still, or run away from the bear. [Fight, Stand, Run] > ').lower()
            if(choice != 'fight' and choice != 'stand' and choice != 'run'):
                print('Please state a valid option!')
                continue
            break

        if(choice == 'fight'):
            num = random.randint(1, 2)

            if(num == 1):
                health -= 50
                time.sleep(3)
                print('You have successfully killed the bear! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                win('You have won!')

            elif(num == 2):
                health -= 100
                time.sleep(3)
                print('You currently have ' + str(health) + ' Health!')
                time.sleep(3)
                game_over('You have died!')

        elif(choice == 'stand'):
            num = random.randint(1, 2)

            if(num == 1):
                time.sleep(3)
                print('You successfully made no contact with the bear! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                win('You have won!')

            elif(num == 2):
                health -= 25
                time.sleep(3)
                print('The bear has noticed you and attacked you! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                time.sleep(2)
                win('You have won!')

        elif(choice == 'run'):
            num = random.randint(1, 2)

            if(num == 1):
                time.sleep(3)
                print('You successfully ran away from the bear! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                win('You have won!')

            elif(num == 2):
                health -= 75
                time.sleep(3)
                print('The bear has chased you and made contact with you! You currently have ' + str(health) + ' health!')
                time.sleep(3)
                print('You have escaped the forest!')
                time.sleep(2)
                win('You have won!')

def random_path():
    num = random.randint(1, 3)
    time.sleep(2)

    if(num == 1):
        path()
    elif(num == 2):
        path_2()
    elif(num == 3):
        path_3()
    else:
        print('Error has occured!')

def start():
    intro()
    print('You are lost in a gloomy forest.')
    time.sleep(2)
    print('There are 3 unusual exits that leads out of the forest.')
    time.sleep(2)

    while True:
        try:
            choice = int(input('Which exit will you take? [1, 2, 3] > '))
            if(choice < 1 or choice > 3):
                print('Please state a valid number!')
                continue
        except ValueError:
            print('Please state a number!')
            continue
        else:
            break

    if(choice == 1):
        random_path()
    elif(choice == 2):
        random_path()
    elif(choice == 3):
        random_path()

start()

if(health == 0):
    game_over('You have died!')
