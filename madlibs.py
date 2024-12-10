# Read the story from the file
with open('story.txt', 'r', encoding='utf-8') as f:
    story = f.read()

print('Here is the Original Story,\n',story)

# List to store placeholders in the order they appear
words = []
start_of_word = -1

# Define the target characters
target_start = '<'
target_end = '>'

# Extract placeholders enclosed in '<' and '>'
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word:i+1]
        if word not in words:  # Avoid duplicates while preserving order
            words.append(word)
        start_of_word = -1  # Reset for the next word

# Dictionary to store user inputs
answers = {}

# Ask the user to provide words for each placeholder
for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

# Replace all placeholders in the story with user inputs
for word, answer in answers.items():
    story = story.replace(word, answer)

# Print the final story with the replacements
print("\nYour Mad Libs story:")
print(story)
