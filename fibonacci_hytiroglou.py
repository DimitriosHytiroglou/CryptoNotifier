def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibo(n-1)+fibo(n-2)
print(fibo(int(input("Give a number to get its Fibonacci sequence: "))))

# Exercise 2

word1 = input("Give the first word: ")
word2 = input("Give the second word: ")

letterlist=[]

[letterlist.append(letter) for letter2 in word1 for letter in word2 if letter==letter2]

print("Here are the common letters of the two words:")
print(sorted(letterlist))
print("\n")





#Exercise 3
#a)

numbers=[]

[numbers.append(x**2) for x in range(100) if ((x**2)%3 == 1 & x**2<100)]

print("Here are the numbers: ")
print(numbers)
print('\n')

#b)
text = """A new, a vast, and a powerful language is developed for the future use of analysis,
          in which to wield its truths so that these may become of more speedy and accurate 
          practical application for the purposes of mankind than the means hitherto in our 
          possession have rendered possible."""

wordlist=text.split()

first_letters=[]
[first_letters.append(x[0]) for x in wordlist]

print("Here are the first letters of every word in the snippet: ")
print(first_letters)
print("\n")

#c)
pythagorean=[]
[pythagorean.append((x,y,int((x**2+y**2)**(1/2)))) for x in range(1,25) for y in range(1,25) if ((x**2 + y**2)<=25 and x < y and ((x**2+y**2)**(1/2)-int((x**2+y**2)**(1/2)))==0)]

print("The pythagorean triples (x,y,z) below 25 are: ")
print(pythagorean)
print("\n")

#d)
word="welcomed"
variants=[]
[variants.append(word[:i]+word[i+1:]) for i in range(len(word))]
print("the variants of welcome by removing one letter are: ")
print(variants)

#e)
import random
vowels="aeiou"
#vowels=['a','e','i','o','u']
word2="Booted"
variants2=[]
[variants2.append(word2.replace(word2[i],random.choice(vowels.replace(word2[i],"")))) for i in range(len(word2)) if word2[i] in vowels]
print("\nThe variants of Booted if a vowel is replaced by a random other vowel are: ")
print(variants2)
print("\n")

#Exercise 4

def initiate_board():
    n = int(input("Enter a board size: "))
    board=[0]*n
    for i in range(n):
        board[i] = [0]*n
    return(board)

def calculate_moves():
    board = initiate_board()
    side = len(board[0])

    for i in range(side):
        board[i][0]=1
        for j in range(side-1):
            if j <= i:
                board[i][j+1]=i-j
            else:
                board[i][j] = 0
        print(board[i])

calculate_moves()



##############
#for x in range(1,25):
#    for y in range(1,25):
#        if ((x**2 + y**2)<=25 and x<y and ):
#            print(x)
#            print(y)
