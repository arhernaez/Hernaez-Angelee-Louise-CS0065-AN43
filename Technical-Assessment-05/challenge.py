import nltk
import re
from nltk.corpus import opinion_lexicon

# Download the public dataset
nltk.download('opinion_lexicon')

# Get happy and sad word datasets
happy_words = set(opinion_lexicon.positive())
sad_words = set(opinion_lexicon.negative())

# count happy words
def number_happy(sentence):
    words = re.findall(r"[a-zA-Z']+", sentence.lower())
    count = 0

    for word in words:
        if word in happy_words:
            count += 1

    return count

# count sad words
def number_sad(sentence):
    words = re.findall(r"[a-zA-Z']+", sentence.lower())
    count = 0

    for word in words:
        if word in sad_words:
            count += 1

    return count

# Ask user to enter a sentence
sentence = input("Enter a sentence: ")

# Calculate happiness and sadness levels
happy = number_happy(sentence)
sad = number_sad(sentence)

# Display results
print("\n===== SENTIMENT ANALYSIS =====")
print("Number of happy words:", happy)
print("Number of sad words:", sad)

# Determine the tone of the sentence
if happy > sad:
    print("Tone of the sentence: HAPPY")
elif sad > happy:
    print("Tone of the sentence: SAD")
else:
    print("Tone of the sentence: NEUTRAL")


