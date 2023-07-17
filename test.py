def count_letters(text):
    str(text)
    for letters in text:
        no_of_letters = text.count(letters)
        print(letters, '-', no_of_letters)

text = 'aaa bbb ccc'
count_letters(text)