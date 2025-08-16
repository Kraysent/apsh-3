def metric(v: float, u1: str, u2: str) -> float:
    norm = 0
    if u1 == "km":
        norm = v * 1000
    elif u1 == "pc":
        norm = v * 3.086 * 10**16
    elif u1 == "in":
        norm = v * 0.0254
    else:
        norm = v

    if u2 == "km":
        return norm / 1000
    elif u2 == "in":
        return norm / 0.0254
    elif u2 == "pc":
        return norm / (3.086 * 10**16)
    else:
        return norm
