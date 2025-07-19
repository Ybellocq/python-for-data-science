import sys
import string


def count_characters(text):
    """
    Compte les différents types de caractères dans un texte donné.
    Args:
    text (str): Le texte à analyser
    Returns:
    tuple: Un tuple contenant (nb_majuscules, nb_minuscules, nb_ponctuation,
    nb_espaces, nb_chiffres)
    """
    upper_count = 0
    lower_count = 0
    punct_count = 0
    space_count = 0
    digit_count = 0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in string.punctuation:
            punct_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1
    return upper_count, lower_count, punct_count, space_count, digit_count


def display_analysis(text):
    """
    Affiche l'analyse des caractères du texte donné.
    Args:
    text (str): Le texte à analyser et dont afficher les résultats
    """
    upper, lower, punct, space, digit = count_characters(text)
    total = len(text)
    print(f"Debug: text repr = {repr(text)}")
    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def get_user_input():
    """
    Demande à l'utilisateur de saisir un texte.
    Returns:
    str: Le texte saisi par l'utilisateur
    """
    try:
        text = input("What is the text to count?\n")
        return text.rstrip('\n')
    except EOFError:
        return ""


def main():
    """
    Fonction principale qui gère les arguments de ligne de commande et
    l'analyse de texte.
    """
    try:
        if len(sys.argv) == 1:
            text = get_user_input()
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("AssertionError: more than one argument is provided")
            return
        display_analysis(text)
    except Exception as e:
        print(f"Une erreur est survenue: {e}")


if __name__ == "__main__":
    main()
