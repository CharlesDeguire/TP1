def count_word(phrase):
    nombre_mots = len(phrase.split())
    return nombre_mots

phrase = input("Quelle est ta phrase?")
print(count_word(phrase))
