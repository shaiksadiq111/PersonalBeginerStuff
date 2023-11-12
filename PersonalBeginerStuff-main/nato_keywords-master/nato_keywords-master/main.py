word_entered = input("enter the word you want nato alphabets for\n")
alphabets = list(word_entered)
alphabets = [alphabet.upper() for alphabet in alphabets]
import pandas
df = pandas.read_csv("data.csv")
words = []
for alphabet in alphabets:
    word = df[df["alphabet"] == alphabet].word.tolist()
    words.append(word)
print(words)