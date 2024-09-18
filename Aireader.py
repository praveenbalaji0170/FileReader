from heapq import nlargest
from collections import Counter
import re

# Function to summarize content
def summarize_content(content, max_chars):
    # Tokenizing the content into words and filtering out non-alphabetic characters
    words = re.findall(r'\b\w+\b', content.lower())
    
    # Counting word frequencies
    word_freq = Counter(words)

    # Finding the most common words to include in the summary
    most_common_words = nlargest(max_chars, word_freq, key=word_freq.get)

    # Creating a summary using most common words, limiting by max_chars
    summary = ' '.join(most_common_words[:max_chars])

    # Trimming to ensure the character limit is respected
    return summary[:max_chars]

# Function to get file input and print summarized content
def print_summarized_content():
    # Asking user to input the file path
    file_path = input("Enter the path of the file you want to summarize: ")
    
    try:
        # Opening the file in read mode
        with open(file_path, 'r') as file:
            # Reading file content
            content = file.read()
            
            # Asking user for the number of characters they want in the summary
            max_chars = int(input("Enter the maximum number of characters for the summary: "))

            # Summarizing the content
            summary = summarize_content(content, max_chars)
            
            # Printing the summarized content
            print("\nSummarized Content:\n")
            print(summary)
    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Calling the function
print_summarized_content()
