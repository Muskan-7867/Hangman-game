import random
f = open("word.txt","r")
data=f.readline()
words=data.split()
word=random.choice(words)
word=word.upper()

total_chances=7
guessed_word='-'*len(word)
while total_chances!=0:    
    print(guessed_word)
    letter=input("Guess a letter:  ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
               guessed_word=guessed_word[:index]+letter+guessed_word[index+1:]
            #    print(guessed_word)

        if guessed_word==word:
            print("Congratulations you won!!!!")
            break
    else:
            total_chances-=1
            print("incorrect guess")
            print('The remaining chances are: ',total_chances)
print("GAME OVER")
print("You Lose")
print("All the chances are exhausted")
print("The actual word is",word)