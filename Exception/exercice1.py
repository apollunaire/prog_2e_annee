def divEntier(x: int, y: int) -> int:
    print("divEntier from exercice 1")
    if y < 0 or x < 0:
        raise ValueError("nombre")
    if y == 0:
        raise ValueError("nul")
    if x < y:
        return 0
    else:
        x = x - y
        return divEntier(x, y) + 1