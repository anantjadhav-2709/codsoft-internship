import random

def get_user_choice():
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    user_input = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()
    if user_input not in choices:
        print("Invalid choice, please try again.")
        return get_user_choice()  
    return choices[user_input], user_input

def get_computer_choice():
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    comp_choice = random.choice(list(choices.keys()))
    return choices[comp_choice], comp_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    #  winning rules
    rules = {
        'r': 's',  # Rock beats Scissors
        'p': 'r',  # Paper beats Rock
        's': 'p'   # Scissors beat Paper
    }
    
    if rules[user_choice] == computer_choice:
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    #  choices
    user_choice, user_input = get_user_choice()
    computer_choice, comp_input = get_computer_choice()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    #  winner
    result = determine_winner(user_input, comp_input)
    print("\n" + result)

if __name__ == "__main__":
    main()
