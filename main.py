from pet import Pet

def display_menu(pet):

 print(f"\nWhat would you like to do with {pet.name}?")

 print(f"1. 🍽️   Feed {pet.name}")

 print(f"2. 😪  Let {pet.name} sleep")

 print(f"3. ⚽  Play with {pet.name}")

 print(f"4. 🏆  Train a new trick with {pet.name}")

 print("5. ✨  Show learned tricks")

 print(f"6. 📊  Check {pet.name}'s status")

 print("7. ❌  Exit")

def get_valid_choice():

while True:

    choice = input("Enter a number (1-7): ")

    if choice in [str(i) for i in range(1, 8)]:

        return choice

    print("⚠️ Invalid option. Please choose a number from 1 to 7.")

def main():

 print("🐶 Welcome to the Virtual Pet Game")

 name = input("What would you like to name your pet? ")

 pet = Pet(name)



 print(f"\n🎉 Awesome! You've adopted {name}. Let's take care of them!")



while True:

    display_menu(pet)  # Pass the pet object here

    choice = get_valid_choice()



    if choice == "1":

        pet.eat()

    elif choice == "2":

        pet.sleep()

    elif choice == "3":

        pet.play()

    elif choice == "4":

        while True:

            trick = input("What trick do you want to teach? ").strip()

            if trick:

                pet.train(trick)

                break

            print("⚠️ Trick name cannot be empty. Please try again.")

    elif choice == "5":

        pet.show_tricks()

    elif choice == "6":

        pet.get_status()

    elif choice == "7":

        if pet.happiness > 7:

            print(f"👋 Goodbye! {pet.name} had a great time with you! 🥰")

        elif pet.happiness > 4:

            print(f"👋 Goodbye! {pet.name} will miss you! 😊")

        else:

            print(f"👋 Goodbye! {pet.name} looks a bit sad to see you go. 😢")

        break

if __name__ == "__main__":

  main()
