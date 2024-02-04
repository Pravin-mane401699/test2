def find_highest_frequency_word_length(s):
    # Removing punctuation and converting to lowercase
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum() or char.isspace())
    
    # Splitting the string into words
    words = s.split()
    
    # Counting the frequency of each word
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Finding the highest frequency
    max_freq = max(word_freq.values()) if word_freq else 0
    
    # Finding the length of the word with the highest frequency
    max_freq_word_length = max(len(word) for word, freq in word_freq.items() if freq == max_freq)
    
    return max_freq_word_length

# Example usage:
input_string = input("Enter a string : ")
result = find_highest_frequency_word_length(input_string)
print("Length of the highest-frequency word:", result)