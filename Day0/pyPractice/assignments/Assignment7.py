def count_words(sentence):
    """Count words separated by spaces, ignoring empty parts."""
    return len([word for word in sentence.split(" ") if word != ""])


if __name__ == "__main__":
    print(count_words("Python is fun"))  # 3
