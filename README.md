# Password Generator

## Project Information
- **Developer**: Lakshitpythondevloper

## Overview
A interactive Python-based password generator that creates customized passwords based on user preferences and provides friendly feedback.

## Features
- Customizable password length and composition
- Random character selection from letters, numbers, and symbols
- Interactive user feedback system
- Audio feedback support
- Friendly, conversational interface

## Requirements
```python
import random
import pygame
```

## Code Structure

### 1. Imports and Initial Setup
```python
import random as rd
import pygame 

print("Welcome to password genrator")
```
- Utilizes random module for generating selections
- Implements pygame for audio playback
- Displays welcome message

### 2. Character Sets
```python
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Numbers = [1,2,3,4,5,6,7,8,9,10]
Symbols = ['$','*','^','*','$','@','!','&','#','/']
```
Defines three main character sets:
- Lowercase letters (a-z)
- Numbers (1-10)
- Special symbols for enhanced security

### 3. User Input Collection
```python
input_Letters = int(input("Alright buddy, tell me how many letters you want in your password: "))
input_Symbols = int(input("Okay cool! Now tell me how many symbols you want in your password: "))
input_Numbers = int(input("Alright then, lastly, how many digits do you want in your password: "))
```
Collects user preferences for:
- Number of letters
- Number of symbols
- Number of numbers

### 4. Password Generation Process
```python
passowrd = []
for pa in range(0,input_Letters):
    passowrd+=rd.choice(Letters)
for pa in range(0,input_Numbers):
    passowrd+=str(rd.choice(Numbers))
for pa in range(0,input_Symbols):
    passowrd+=rd.choice(Symbols)

rd.shuffle(passowrd)
```
Password generation includes:
1. Creating an empty list
2. Adding random characters based on user specifications
3. Shuffling characters for randomization

### 5. User Feedback System
The program includes an interactive feedback system with:
- Positive response handling
- Negative response handling
- Audio feedback for unrecognized inputs

## Response Handling
```python
user_response = [
    "No bro, I didn't like it", 
    "No", 
    "No bro", 
    "No bro, I don't like your password"
]

user_Good_response = [
    "It's fine, bro", 
    "It's great", 
    "It's good, bro", 
    "It's good", 
    "It's okay", 
    "Good", 
    "Very good", 
    "Excellent"
]
```
## Usage
1. Run the script
2. Input desired number of letters, symbols, and numbers
3. Review generated password
4. Provide feedback
5. Restart if needed

## Note
Make sure to have the required audio file ('s.mp3') in the same directory for the feedback sound to work properly. You can download it form github which I uploaded in github file.
