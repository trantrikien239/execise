a = 'My name is Michele'
def reverse_words(text):
    return ' '.join(reversed(a.split()))
print(reverse_words(a))