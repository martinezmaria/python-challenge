# import modules
import csv
import string

file = 'Resources/paragraph_1.txt'

# define variables
characters = 0
word_count = 0
sentence_count = 0
avg_letter_count = 0
avg_sentence_length = 0

# open and read file
with open(file, 'r') as text:
    print(text)

    content = text.read().splitlines()
    print(content)

    lines = len(content)
    print(lines)

    words = content[0].split()
    print(words)
    word_count = len(words)
    print(word_count)

    characters = sum(len(line) for line in content)
    print(characters)

    sentences = content[0].split(".")
    print(sentences)
    sentence_count = len(sentences)
    print(sentence_count)

    avg_sentence_length = round(word_count/sentence_count, 1)
    print(avg_sentence_length)

    avg_letter_count = round(characters/word_count, 1)
    print(avg_letter_count)




output_path = ("Analysis/results.txt")
with open(output_path, "w") as file:
    csvwriter = csv.writer(file, delimiter=",")
    csvwriter.writerow(["Paragraph Analysis"])
    csvwriter.writerow(["-------------------------------------------"])
    csvwriter.writerow([f"Approximate Word Count: {word_count}"])
    csvwriter.writerow([f"Approximate Sentence Count: {sentence_count}"])
    csvwriter.writerow([f"Average Letter Count: {avg_letter_count}"])
    csvwriter.writerow([f"Average Sentence Length: {avg_sentence_length}"])
    



    