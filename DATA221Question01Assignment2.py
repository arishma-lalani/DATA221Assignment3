# Question 1
# Open and read the text file that you want to use. In this case, "sample-file.txt".
text_file = open("sample-file.txt", "r")
text_inside_file = text_file.read()

# Split all the text into individual words (tokens)
tokens = text_inside_file.split()

# Create an empty list to store all the valid tokens that fit the criteria
valid_tokens = []

# Account for each token in the file
for token in tokens:
    token = token.lower()  # Change all uppercase letters to lowercase

    # Remove all characters which are not alphabets from the BEGINNING of the token
    while len(token) > 0 and not ("a" <= token[0] <= "z"):
        token = token[1:]

    # Remove all characters which are not alphabets from the END of the token
    while len(token) > 0 and not ("a" <= token[-1] <= "z"):
        token = token[:-1]

    # Use a for loop to count the number of alphabets in the token
    number_of_alphabets = 0
    for characters in token:
        if "a" <= characters<= "z":
            number_of_alphabets = number_of_alphabets + 1  # Add for each number of alphabet

    # Only keep the token if it has at least 2 alphabets
    if number_of_alphabets >= 2:
        valid_tokens.append(token)

# Create an empty dictionary to store the frequencies of the words. Then, use a for loop to add count how many times the valid token appears in the file
number_of_words = {}
for token in valid_tokens:
    if token in number_of_words:
        number_of_words[token] = number_of_words[token] + 1
    else:
        number_of_words[token] = 1

# Create a counter to count how many words are printed. This ensures that the next line stops printing when it reaches 10 words
top_ten_most_frequent_words = 0
while top_ten_most_frequent_words < 10 and len(number_of_words) > 0:
    word_with_largest_frequency = list(number_of_words.keys())[0]  # The first word that is printed will be the most frequent one

    for word in number_of_words:
        if number_of_words[word] > number_of_words[word_with_largest_frequency]:
            word_with_largest_frequency = word
    # Print the word along with its frequency
    print(f"{word_with_largest_frequency} -> {number_of_words[word_with_largest_frequency]}")

    # Remove the printed word so that the word that is next most frequent can be detected
    del number_of_words[word_with_largest_frequency]

    # Add to the counter
    top_ten_most_frequent_words = top_ten_most_frequent_words + 1

text_file.close()