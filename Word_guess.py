import random

four_letter_words=['down','word','acid',"bold","easy","bike",'cake','door','game','jump']
five_letter_words=['apple','table','steal','plant','shine','ghost','trend','court','fruit','angel']
six_letter_words=['banana','bottle','change','device','energy','family','animal','bottom','follow','camera']
while True:

    try:
        choose_letter=int(input("Which letter word do you want? "))
        if choose_letter<4 or choose_letter>6:
            print("Please choose a letter between 4 and 6 ")
            continue
        break
    except Exception:
        print("Please enter a valid number ")
        continue

lives=['❤','❤','❤','❤','❤']
chosen_word=""
if choose_letter==4:
    chosen_word=random.choice(four_letter_words)
elif choose_letter==5:
    chosen_word=random.choice(five_letter_words)
else:
    chosen_word=random.choice(six_letter_words)


word=""
underscore=[]
a='y'
guessed_letter=[]
wrong_guess=[]


for i in range(choose_letter):
    underscore.append("_")
print("Your total lives: ",lives)


while a=='y':
    print(underscore)


    if word!=chosen_word:
        try:
            user_input = input("Enter your guess: ").lower()

            if len(user_input)==0:
                print("Please enter one letter")
                continue

            elif len(user_input)>1:
                print("Please enter only one letter")
                continue
                
            elif user_input in guessed_letter:
                print("You guessed this letter already")
                continue

        except Exception:
            print("Please enter a valid letter")
            continue
    elif word==chosen_word:
        a='n'


    for j in range(choose_letter):

        if user_input==chosen_word[j] and user_input!="":
               underscore[j]=user_input
               guessed_letter.append(user_input)
               word="".join(underscore)


    if user_input not in chosen_word:
        wrong_guess.append(user_input)
        lives.remove("❤")
        print("Your remaining lives: ", lives)
        if len(lives) == 0:
            a = 'n'



wrong_guessed=set(wrong_guess)
print(f"Wrong guesses: {wrong_guessed}")


if word==chosen_word:
    print("You win!")
    print(f"You guessed the word: {chosen_word}")
    print("Your remaining lives: ",lives)
else:
    print("You lose!")
