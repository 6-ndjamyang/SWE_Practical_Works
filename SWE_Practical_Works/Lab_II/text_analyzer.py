#Step 1: Open and Read a Text File
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters


#Step 2: Count the Number of Lines
def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")


#Step 3: Count Words
def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")


#Step 4: Find the Most Common Word
from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")


#Step 5: Calculate Average Word Length
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")


# Step 6: Count Unique Words
def count_unique_words(content):
    words = content.lower().split()
    unique_words = set(words)
    return len(unique_words)


# Step 7: Find the Longest Word
def find_longest_word(content):
    words = content.split()
    longest_word = ""
    longest_word_length = 0
    for word in words:
        if len(word) > longest_word_length:
            longest_word = word
            longest_word_length = len(word)
    return longest_word, longest_word_length


# Step 8: Count Occurrences of a Specific Word
def count_specific_word(content, target_word):
    words = content.lower().split()
    target_word = target_word.lower()
    return words.count(target_word)



# Step 9: Calculate Percentage of Words Longer Than Average Length (Simpler Version)
def percentage_words(content):
    words = content.split()
    avg_length = average_word_length(content)
    
    # Count words longer than the average length
    longer_than_avg_count = 0
    for word in words:
        if len(word) > avg_length:
            longer_than_avg_count += 1
    
    # Calculate and return the percentage
    percentage = (longer_than_avg_count / len(words)) * 100
    return percentage



#Step 10: Combine Everything into a Main Function
def analyze_text(filename, specific_word=None):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    num_unique_words = count_unique_words(content)
    avg_length = average_word_length(content)
    longest_word, longest_word_length = find_longest_word(content)
    percentage_avg = percentage_words(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Longest word: '{longest_word}' ({longest_word_length} characters)")
    print(f"Percentage of words longer than average length: {percentage_avg:.2f}%")

    # Count and display the specific word occurrences if specified
    if specific_word:
        specific_word_count = count_specific_word(content, specific_word)
        print(f"Occurrences of '{specific_word}': {specific_word_count}")

# Run the analysis with a specific word
analyze_text('sample.txt', specific_word='software')