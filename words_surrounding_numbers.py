import os
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter


def find_words_around_numbers(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Regular expression pattern to match a words before and after a number
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
    wordcloud = WordCloud(width=1200, height=800, background_color ='white',
                          min_font_size = 14).generate_from_frequencies(words)
    plt.figure(figsize=(30, 20))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


def search_directory(directory):
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



word_list = []
list_of_words = search_directory("txt")

for sublist in list_of_words:
    word_list += sublist

top_20_words = dict(Counter(word_list).most_common(20))
print(top_20_words)
plot_wordcloud(top_20_words)