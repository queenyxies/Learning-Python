
from collections import Counter

def character_count(s):
    # Convert the string to lowercase
    s = s.lower()
    
    # Count occurrences of each character
    counts = Counter(s)
    
    # Create a sorted list of characters
    sorted_characters = sorted(counts.keys())
    
    # Build the result string
    result = ''.join(f'{char}{counts[char]}' for char in sorted_characters)
    
    return result

print(character_count("hello"))