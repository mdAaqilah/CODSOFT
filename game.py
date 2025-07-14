import random

print("\n🎮 Welcome to Rock, Paper, Scissors!")
print("Let’s see if luck is on your side today.\n")

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
round_number = 1

while True:
    print(f"\n🔁 Round {round_number}")
    user_choice = input("👉 What's your move? (rock/paper/scissors): ").strip().lower()

    if user_choice not in choices:
        print("❌ That doesn't seem right. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"\n🧑 You choose: {user_choice}")
    print(f"🤖 Computer choose: {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("🎉 You win this round!")
        user_score += 1
    else:
        print("💻 Computer wins this round.")
        computer_score += 1

    print(f"\n📊 Current Score → You: {user_score} | Computer: {computer_score}")

    play_again = input("\n🔁 Would you like to play another round? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("\n🏁 Final Scoreboard:")
        print(f"🧑 You: {user_score} | 🤖 Computer: {computer_score}")

        if user_score > computer_score:
            print("🎊 Congratulations! You outsmarted the computer!")
        elif user_score < computer_score:
            print("😅 The computer wins today. Better luck next time!")
        else:
            print("⚖️ It's a tie overall! Well played!")

        print("\n🙏 Thanks for playing Rock, Paper, Scissors.")
        
        break

    round_number += 1
