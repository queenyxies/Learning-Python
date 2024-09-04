# 1 Bunny's Favorite Word Length 🐰📏
def getLength(str):
    return len(str)

print(getLength("Carrots")) 

# 2 Bunny's Greeting Composer 
def repeatWord(str, num):
    return str * num

print(repeatWord("La", 3))

#3 Bunny's Favorite Letters 💖🔤
def count_letter(word, letter):
    counter = 0
    for char in word:
        if char == letter:
            counter += 1
    return counter

print("Count letter: ", count_letter("carrot", "r"))

#4. Bunny's Secret Word Comparison 🔍
def compare_words(word1, word2):
    return word1.lower() == word2.lower()

print(compare_words("Hop", "hop"))

#5 Bunny's Anagram Check 🐇🔄
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print("Anagram? ", is_anagram("listen", "silent"))


#6 Bunny's Word Scramble 🎲🐰
import random

def scramble_word(word: str) -> str:
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

# Example usage
print("Random carrot", scramble_word("carrot"))  

#7 Bunny's Sentence Capitalizer 🌟
def capitalize_words(sentence):
    return ' '.join([char.capitalize() for char in sentence.split()])

print(capitalize_words("the bunny hops quickly"))

# 8 Bunny's Word Frequency Counter 📊
def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

# Example usage
print(word_frequency("hop hop hop jump hop"))  # Output: {"hop": 4, "jump": 1}



