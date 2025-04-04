def reverse_vowels(s):
    # Define the set of vowels
    vowels = "aeiouAEIOU"
    
    # Extract the vowels from the string
    vowel_list = [char for char in s if char in vowels]
    
    # Reverse the list of vowels
    vowel_list.reverse()
    
    # Replace the vowels in the string with reversed vowels
    result = []
    vowel_index = 0
    for char in s:
        if char in vowels:
            result.append(vowel_list[vowel_index])  # Use reversed vowel
            vowel_index += 1
        else:
            result.append(char)  # Non-vowel characters remain unchanged
    
    return ''.join(result)

# Example Usage
string = "hello world"
print("String with reversed vowels:", reverse_vowels(string))
