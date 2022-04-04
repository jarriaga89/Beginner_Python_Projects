print('''
***************************************************
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-
***************************************************
''')
print("Hello. Welcome to Josh's Cat Treasure Island. \n")
print("Your mission is to find the treasure your cat wants the most. You can find your way through by typing the marked word (Just the word!) to take an action. Good luck! \n")

q1 = input("There's a giant cat house with two hallways; -left- and -right-. Which one will you choose? \n")
if q1.lower() == "right":
  print("This hallway leads to a room filled with dog toys your cat doesn't like. Game over.")
elif q1.lower() == "left":
  q2 = input("Deeper in the hallway, there's a pool of water in between you and the cat toy storage room. The water is evaporating, so you don't have much time to cross. What will you do? -swim- or -wait-? \n")
  if q2.lower() == "swim":
    print("You swim across the pool and the entrance has a sign that reads 'No wet shoes allowed' and won't let you in. Game over.")
  elif q2.lower() == "wait":
    q3 = input("The pool was drained and you find a ladder to climb up and don't get wet. You enter the door and find 3 more doors. A -red- door, a -blue- door, and a -yellow- door. Which one will you choose? \n")
    if q3.lower() == "red":
      print("This room has transported you to Africa and there are no cat toys or treasures around. Game over.")
    elif q3.lower() == "blue":
     print("You find an empty room with a giant poster of a cat mocking you with a HA-HA gesture. Game over.")
    elif q3.lower() == "yellow":
      print(''' \n
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_) 
            \n
You find your cat sitting in a Queen Throne, and she runs toward you as soon as she notices you. Turns out that YOU are her favorite treasure! Congratulations!
            ''')
    else:
      print("That's not one of the options available. Try again, don't add punctuation or spaces.")
  else:
   print("That's not one of the options available. Try again, don't add punctuation or spaces.")
else:
  print("That's not one of the options available. Try again, don't add punctuation or spaces.")