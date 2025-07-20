def ft_filter(function, iterable):
    """
    Retourne un itérateur produisant les éléments de
    iterable pour lesquels
    function(item) est vraie. Si function est None,
    retourne les éléments
    qui sont vrais.
    doc.python function filter() pour toutes infos
    """
    # Si aucune fonction n'est fournie, retourner les éléments "truthy"
    if function is None:
        return [item for item in iterable if item]
    else:
        # Appliquer la fonction à chaque élément et garder
        # ceux qui retournent True
        return [item for item in iterable if function(item)]
