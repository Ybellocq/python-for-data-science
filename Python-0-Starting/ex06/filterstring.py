import sys
from ft_filter import ft_filter


def filter_words(text, min_length):
    """
    Filtre les mots d'un texte selon leur longueur minimale.
    Args:
    text (str): Le texte contenant les mots à filtrer
    min_length (int): La longueur minimale des mots à conserver
    Returns:
    list: Liste des mots ayant une longueur supérieure à min_length
    """
    # Séparer le texte en mots (par défaut sur les espaces)
    words = text.split()
    # Utilisation d'une lambda et de ft_filter avec list comprehension
    filtered_words = ft_filter(lambda word: len(word) > min_length, words)
    return filtered_words


def validate_arguments():
    """
    Valide les arguments de ligne de commande.
    Returns:
        tuple: (string, integer) si les arguments sont valides
    Raises:
        AssertionError: Si les arguments ne sont pas valides
    """
    # Vérifier qu'il y a exactement 2 arguments (+ nom du script)
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    string_arg = sys.argv[1]
    number_arg = sys.argv[2]
    # Vérifier que le premier argument est une chaîne de caractères
    if not isinstance(string_arg, str):
        raise AssertionError("the arguments are bad")
    # Vérifier que le second argument peut être converti en entier
    try:
        number_value = int(number_arg)
    except ValueError:
        raise AssertionError("the arguments are bad")
    return string_arg, number_value


def main():
    """
    Fonction principale qui gère le filtrage des mots selon leur longueur.
    """
    try:
        text, min_length = validate_arguments()
        result = filter_words(text, min_length)
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Une erreur est survenue: {e}")


if __name__ == "__main__":
    main()
