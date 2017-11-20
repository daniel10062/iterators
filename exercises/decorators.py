"""Övningar på decorators."""

from functools import wraps  # NoQA


def memoize(F):
    """Implementera memoization (cache).

    Detta är den enklaste typen av cache som helt enkelt lagrar alla
    returvärden för de anropsvärden som används.
    """
    pass


def rovarsprak(F):
    """Översätt utdata till rövarspråket.

    Funktionen som dekoreras kan antas returnera textsträngar. Dessa översätts
    av decoratorn till rövarspråket.
    """
    @wraps(F)
    def dec_rovar(*args, **kwargs):
        result = ""
        consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                      "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
        # consonants = "bcdfghjklmnpqrstvwxy"
        data = F(*args, **kwargs)
        for letter in data:
            if letter in consonants:
                result = result + letter + "o" + letter
            else:
                result = result + letter

        return result
    return dec_rovar
