import random
import time

def dealer_input(input_max):
    sum_value = input_max
    if sum_value >= 6:
        weights = [1] * (sum_value - 1)
        weights[1] = 2.5
        weights[2] = 2.5
        blank = random.choices(range(1, sum_value), weights=weights, k=1)[0]
    else:
        blank = random.randint(1, sum_value - 1)

    live = sum_value - blank
    return sum_value, blank, live


def shoot(all_magazine, blank, live):
    bang = random.choice(['blank'] * blank + ['live'] * live)
    all_magazine -= 1

    if bang == 'blank':
        blank -= 1
        print()
        result = 'Nothing happens. It was blank.'
    else:
        live -= 1
        print()
        result = 'BANG! It was live.'

    return result, bang, all_magazine, blank, live


def error_command():
    print('ERROR! UNAVAILABLE COMMAND.')


def quitter():
    print()
    print('-' * 21)
    print()
    print('GAME OVER!')
    print('Bye, loser')
    print()
    print('-' * 21)
    time.sleep(1.5)
    quit()


def shoot_checkbox(input_value, all_magazine, blank, live, health):
    if input_value in {'shoot', 's', '1'}:
        print()
        print('Enter who will be shooted')
        who_shoot = input('[1] Me, [2] Dealer: ').lower()

        if who_shoot in {'me', 'i', '1'}:
            result, bang, all_magazine, blank, live = shoot(all_magazine, blank, live)
            print(result)
            if bang == 'blank':
                if health > 0 and all_magazine > 0:
                    print()
                    print(f'HP: {health}')
                return all_magazine, blank, live, health
            else:
                health -= 1
                if health > 0:
                    print()
                    print(f'HP: {health}')
                else:
                    print()
                    print('You are dead')
                    print()
                return all_magazine, blank, live, health

        elif who_shoot in {'dealer', 'd', '2'}:
            result, bang, all_magazine, blank, live = shoot(all_magazine, blank, live)
            print(result)
            if bang == 'blank':
                health -= 1
                if health > 0:
                    print()
                    print(f'HP: {health}')
                else:
                    print()
                    print('You are dead')
            else:
                if health > 0 and all_magazine > 0:
                    print()
                    print(f'HP: {health}')
            return all_magazine, blank, live, health
        else:
            error_command()

    elif input_value in {'quit', 'q', '2'}:
        quitter()
        return None, None, None, None

    else:
        error_command()


def main(reload, all_magazine, blank, live, health):
    while health > 0 and all_magazine > 0:
        input_value = input('Enter [1] Shoot or [2] Quit: ').lower()
        all_magazine, blank, live, health = shoot_checkbox(input_value, all_magazine, blank, live, health)
        if all_magazine == 0:
            reload = True
            game_start(reload, health)


def game_start(reload, health):
    if reload:
        all_magazine, blank, live = dealer_input(random.randint(2, 8))
        print()
        print('-' * 5, 'New round', '-' * 5)
        print()
        print(f'HP: {health} | ALL: {all_magazine} | BLANK: {blank} | LIVE: {live}')
        reload = False
    main(reload, all_magazine, blank, live, health)

while True:
    reload = True
    health = 3

    print('██████╗░██╗░░░██╗░██████╗░██████╗██╗░█████╗░███╗░░██╗')
    print('██╔══██╗██║░░░██║██╔════╝██╔════╝██║██╔══██╗████╗░██║')
    print('██████╔╝██║░░░██║╚█████╗░╚█████╗░██║███████║██╔██╗██║')
    print('██╔══██╗██║░░░██║░╚═══██╗░╚═══██╗██║██╔══██║██║╚████║')
    print('██║░░██║╚██████╔╝██████╔╝██████╔╝██║██║░░██║██║░╚███║')
    print('╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝')
    print('')
    print('██████╗░░█████╗░██╗░░░██╗██╗░░░░░███████╗████████╗████████╗███████╗')
    print('██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝')
    print('██████╔╝██║░░██║██║░░░██║██║░░░░░█████╗░░░░░██║░░░░░░██║░░░█████╗░░')
    print('██╔══██╗██║░░██║██║░░░██║██║░░░░░██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░')
    print('██║░░██║╚█████╔╝╚██████╔╝███████╗███████╗░░░██║░░░░░░██║░░░███████╗')
    print('╚═╝░░╚═╝░╚════╝░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝')
    print()
    print('Made by L0stNForgotten')

    print('Rules:', "*If you shoot, you can't go back", '*If you shoot blank on dealer, you get hit', 'Have fun!','', sep='\n')
    input_start = input('Enter [1] Start or [2] Quit: ').lower()

    if input_start in {'start', 's', '1'}:
        game_start(reload, health)
    elif input_start in {'quit', 'q', '2'}:
        quitter()
        break