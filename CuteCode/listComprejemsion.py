def sum_even_numbers(numbers):
    return sum([number for number in numbers if number % 2 == 0])

print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def filter_words(words):
    return [word for word in words if "a" not in word]

print(filter_words(["hat", "carrot", "bunny", "rabbit"]))

def squared(numbers):
    return [number ** 2 for number in numbers]

print(squared([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def to_uppercase(strings):
    return [word.capitalize() for word in strings]

print(to_uppercase(["hat", "carrot", "bunny", "rabbit"]))

def count_vowels_consonants(str):
    vowels = 'AEIOUaeiou'
    vowel_count = 0
    consonant_count = 0
    
    for char in str:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    return f"Vowels {vowel_count} Consonants: {consonant_count}"
print(count_vowels_consonants("hello"))



