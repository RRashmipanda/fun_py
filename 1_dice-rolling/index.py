# ask: roll the dice?
# if users enter y
#      generate two random numbers
#      print them
# if users enter n
#      print thank you msg
#      Terminate
# else      
#    print invalid choice
import random

while True:
 choice = input("Roll the dice? (y/n): ").lower()
 if choice == 'y':
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print(f"{d1}, {d2}")

 elif choice == 'n':
    print('Thanks for playing')
    break
 else:
   print('Invalid choice...')
