#Question 6: Count Vowels
#Write a program that counts the number of vowels in a sentence.
#eg " Hello World " => returns 2



def count_vowels(sentence):
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert the sentence to lowercase to handle both uppercase and lowercase vowels
    sentence = sentence.lower()
    
    # Initialize a set to store unique vowels encountered
    unique_vowels = set()
    
    # Iterate through each character in the sentence
    for char in sentence:
        # If the character is a vowel, add it to the set of unique vowels
        if char in vowels:
            unique_vowels.add(char)
    
    # Return the count of unique vowels
    return len(unique_vowels)

# Example usage:
sentence = input("Enter a sentence: ")
print("Number of unique vowels:", count_vowels(sentence))
