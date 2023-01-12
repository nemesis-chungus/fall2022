import webbrowser as wb
wb.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
print("now we got that out of the way, here is the real program")
score = 0
answer = input("what function goes with else? ")
if answer == "if":
    score = score + 1
    print("Yes!")
else:
    print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
answer = input("what is the name of the truck driver? ")
if answer == "joe":
    print("Good.")
    score = score + 1
else:
    print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
answer = input("what was the longest program on the handouts? ")
if answer == "boggle":
    score = score + 1
    print("Oh, you are smart!")
else:
    print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    score = score + 1
answer = input("how many handouts have there been? ")
if answer == "12":
        score = score + 1
        print("You are a smart cookie.")
else:
    print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
answer = input("will you click this? ")
if answer == "no":
    score = score - 1
    print("JUST DO IT")
else:
    print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    score = score + 1
print("Your score is", score)
print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
