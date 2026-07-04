import re
from collections import Counter

with open("newsArticle.txt", "r", encoding="utf-8") as file:
    article = file.read()

#function to count specific word
def count_specific_word(text, search_word):

    words = re.findall(r"\b\w+\b", text)

    count = 0

    for word in words:

        if word.lower() == search_word.lower():
            count += 1

    return count

# function to find the most common word
def identify_most_common_word(text):

    if text.strip() == "":
        return None

    words = re.findall(r"\b\w+\b", text.lower())

    word_counter = Counter(words)

    return word_counter.most_common(1)[0][0]
# function to Calculate average word length
def calculate_average_word_length(text):

    if text.strip() == "":
        return 0

    words = re.findall(r"\b\w+\b", text)

    total_letters = 0

    for word in words:
        total_letters += len(word)

    return total_letters / len(words)
# function to Count paragraphs
def count_paragraphs(text):

    if text.strip() == "":
        return 1

    paragraphs = text.split("\n\n")

    paragraphs = [p for p in paragraphs if p.strip()]

    return len(paragraphs)
# function to Count sentences
def count_sentences(text):

    if text.strip() == "":
        return 1
    else:
        sentences = re.findall(r"[.!?]+", text)

        if len(sentences) == 0:
            return 1
        else:
            return len(sentences)
        
if __name__ == "__main__":

    search_word = ""

    while search_word == "":
        search_word = input("Enter a word to search for: ").strip()

        if search_word == "":
            print("Please enter a word.")

    result = count_specific_word(article, search_word)
    print("Word count:", result)

    most_common = identify_most_common_word(article)
    print("Most common word:", most_common)

    average_length = calculate_average_word_length(article)
    print("Average word length:", average_length)

    paragraphs = count_paragraphs(article)
    sentences = count_sentences(article)

    print("Sentences:", sentences)
    print("Paragraphs:", paragraphs)