
def is_numeric(string):
    'Return value of numeric literal string or ValueError exception'
 
    try:
        float(string)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(string)
        return True
    except (TypeError, ValueError):
        pass
 
    return False