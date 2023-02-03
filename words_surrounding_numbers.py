import os
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter


def find_words_around_numbers(file_path):
    # Function that will open a .txt file and search for a pattern of a
    # number followed by a word, or a word followed by a number. Using pythons
    # re library it defines the patterns and searches the .txt file
    # for matches. If a match is found then the word will be appended to the
    # result list.
    #
    # file_path : String -> string representation of the file path to be searched
    # results : list -> result list of words found within the pattern matches

    with open(file_path, 'r') as file:
        text = file.read()

    # Regular expression pattern to match all words before or after a number
    pattern1 = "\s*\w+ \d+"
    pattern2 = "\s*\d+ \w+"

    pattern = re.compile(f"(?i){pattern1}|{pattern2}")
    matches = re.findall(pattern, text)

    results = []

    for match in matches:
        result = match.strip()
        result = result.split()
        if result[0].isdigit():
            results.append(result[1])
        else:
            results.append(result[0])

    return results


def find_words_before_numbers(file_path):
    # Function that will open a .txt file and search for a pattern of
    # a word followed by a number. Using pythons re library it defines
    # the pattern and searches the .txt file for matches. If a match
    # is found then the word will be appended to the result list.
    #
    # file_path : String -> string representation of the file path to be searched
    # results : list -> result list of words found within the pattern matches

    with open(file_path, 'r') as file:
        text = file.read()

    # Regular expression pattern to match a word followed by a number
    pattern1 = "\s*\w+ \d+"

    pattern = re.compile(f"(?i){pattern1}")
    matches = re.findall(pattern, text)

    results = []

    for match in matches:
        result = match.strip()
        result = result.split()
        if result[0].isdigit():
            results.append(result[1])
        else:
            results.append(result[0])

    return results


def find_words_after_numbers(file_path):
    # Function that will open a .txt file and search for a pattern of
    # a number followed by a word. Using pythons re library it defines
    # the pattern and searches the .txt file for matches. If a match
    # is found then the word will be appended to the result list.
    #
    # file_path : String -> string representation of the file path to be searched
    # results : list -> result list of words found within the pattern matches
    with open(file_path, 'r') as file:
        text = file.read()

    # Regular expression pattern to match a word following a number
    pattern1 = "\s*\d+ \w+"

    pattern = re.compile(f"(?i){pattern1}")
    matches = re.findall(pattern, text)

    results = []

    for match in matches:
        result = match.strip()
        result = result.split()
        if result[0].isdigit():
            results.append(result[1])
        else:
            results.append(result[0])

    return results


def plot_wordcloud(words):
    # Function to generate a word cloud using pythons word cloud generator.
    # It takes a dictionary of the top 20 found words and their frequencies.
    # It then uses matplotlib library to plot the generated word cloud.
    #
    # words : dictionary -> dictionary of the 20 most frequent words and their
    #         frequencies
    wordcloud = WordCloud(width=1200, height=800, background_color ='white',
                          min_font_size = 14).generate_from_frequencies(words)
    plt.figure(figsize=(30, 20))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


def search_directory(directory):
    # Function acts as a directory crawler to first locate the subdirectory
    # labeled "input_dir" which is where the .txt files we were told to
    # focus on are located. It then keeps searching until it finds .txt files.
    # It acheives this using pythons os library. Once the file is found it is
    # then passed through the find_words_around_numbers function.
    #
    # directory: file directory -> dircetory structure that holds all of the .txt
    #            files(dataset)
    results = []
    for subdir, dirs, files in os.walk(directory):
        for sdir in dirs:
            if sdir == "input_docs":
                input_dir = os.path.join(subdir, sdir)
                for subdir, dirs, files in os.walk(input_dir):
                    for file in files:
                        if file.endswith(".txt"):
                            file_path = os.path.join(subdir, file)
                            # matches = find_words_after_numbers(file_path)
                            # matches = find_words_before_numbers(file_path)
                            matches = find_words_around_numbers(file_path)
                            results.append(matches)
    return results


# List to store list of lists that is returned by search_directory as single list
# to pass to Counter
word_list = []
# The result of the search_directory function call
list_of_words = search_directory("txt")

# Iterate over the list of lists to convert into a single list of strings
for sublist in list_of_words:
    word_list += sublist

# Resulting dictionary of the top 20 most frequently found words and their frequencies
# after passing the list of words to the Counter.most_common(20)
top_20_words = dict(Counter(word_list).most_common(20))
print(top_20_words)
# Pass dictionary to the plot_wordcloud function to generate the word cloud
plot_wordcloud(top_20_words)