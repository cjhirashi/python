def no_space(text):
    new_text = ''
    for char in text:
        if char != ' ':
            new_text += char
    return new_text

def reverse(text):
    reverse_text = ''
    for char in text:
        reverse_text = char + reverse_text
    return reverse_text
    
def es_palindromo(text):
    text_space = no_space(text)
    revese_text = reverse(text_space)
    return text_space.lower() == revese_text.lower()
    
print(es_palindromo('Carlos Jiménez Hirashi'))
print(es_palindromo('somos'))
print(es_palindromo('Abba'))
print(es_palindromo('Reconocer'))