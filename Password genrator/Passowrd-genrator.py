
import random as rd
import pygame 

print("Welcome to password genrator")
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Numbers = [1,2,3,4,5,6,7,8,9,10]
Symbols = ['$','*','^','*','$','@','!','&','#','/']

input_Letters = int(input("Alright buddy, tell me how many letters you want in your password: "))
input_Symbols = int(input("Okay cool! Now tell me how many symbols you want in your password: "))
input_Numbers = int(input("Alright then, lastly, how many digits do you want in your password: "))
passowrd = []
for pa in range(0,input_Letters):
    passowrd+=rd.choice(Letters)
for pa in range(0,input_Numbers):
    passowrd+=str(rd.choice(Numbers))
for pa in range(0,input_Symbols):
    passowrd+=rd.choice(Symbols)

rd.shuffle(passowrd)

final_passowrd = ""
for char in passowrd:
    final_passowrd+=char


print("Your passowrd is ready brother😎: -")
print("Your passowrd password:",final_passowrd)
user_input = input("Hey buddy, the password is made correctly, right? ").capitalize()
user_response = [
    "No bro, I didn't like it", 
    "No", 
    "No", 
    "No bro", 
    "No bro", 
    "No bro, I don’t like your password"
]

user_Good_response = [
    "It’s fine, bro", 
    "It’s great", 
    "It’s good, bro", 
    "It’s good", 
    "It’s okay", 
    "Good", 
    "Very good", 
    "Excellent"
]

if user_input == user_response[0]:
    print("No worries, bro. You can restart the game, I’ll create a new password!")
elif user_input == user_response[1]:
    print("No worries, bro. You can restart the game, I’ll create a new password!")
elif user_input  == user_response[2]:
    print("No worries, bro. You can restart the game, I’ll create a new password!")
elif user_input  == user_response[3]:
  print("No worries, bro. You can restart the game, I’ll create a new password!")
elif user_input  == user_response[4]:
    print("No worries, bro. You can restart the game, I’ll create a new password!")
elif user_input  == user_response[5]:
    print("No worries, bro. You can restart the game, I’ll create a new password!")
elif user_input == user_Good_response[0]:
    print("Told you, right? My passwords are always top-notch—hope that’s clear now ✨")
elif user_input == user_Good_response[1]:
    print("Told you, right? My passwords are always top-notch—hope that’s clear now ✨")
elif user_input == user_Good_response[2]:
    print("Told you, right? My passwords are always top-notch—hope that’s clear now ✨")
elif user_input == user_Good_response[3]:
   print("Told you, right? My passwords are always top-notch—hope that’s clear now ✨")
elif user_input == user_Good_response[4]:
    print("Told you, right? My passwords are always top-notch—hope that’s clear now ✨")
elif user_input == user_Good_response[5]:
   print("Told you, right? My passwords are always top-notch—hope that’s clear now ✨")
elif user_input == user_Good_response[6]:
    print("Told you, right? My passwords are always top-notch—hope that’s clear now ✨")
elif user_input == user_Good_response[7]:
   print("Told you, right? My passwords are always top-notch—hope that’s clear now ✨")
else:
    print("I’m not getting it—speak clearly!")
    pygame.mixer.init()

    # Load and play
    pygame.mixer.music.load("Password genrator/s.mp3")
    pygame.mixer.music.play()

    # Keep the script running while music plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
