def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Ajouter les majuscules pour ne pas les laisser intactes
    full_alphabet = alphabet + alphabet.upper()
    full_shifted = shifted_alphabet + shifted_alphabet.upper()

    translation_table = str.maketrans(full_alphabet, full_shifted)
    encrypted_text = text.translate(translation_table)
    return encrypted_text

# Demande d'entrée utilisateur
text_input = input("Entrez le texte à chiffrer : ")
shift_input = int(input("Entrez le décalage (shift) : "))

result = caesar(text_input, shift_input)
print("Texte chiffré :", result)
