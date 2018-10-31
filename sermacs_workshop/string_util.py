"""
string_util.py
Sample repository for MolSSI Workshop at SERMACS

Misc. string processing functions
"""

def title_case(sentence):
    """
    Convert string to title case

    Parameters
    --------------
    sentence: string
        Sentence to be converted to title case

    Returns:
    --------------
    ret: string
        Input string in title case

    Example
    --------------
    >>> title_case('ThIs iS a StrIng tO be ConVerted')
        This Is A String To Be Converted
    """
    if not isinstance(sentence, str):
        raise TypeError('Input must be type string')
    capitalized = ' '.join([s[0].upper()+s[1:].lower() for s in sentence.strip().split()])
    return capitalized

if __name__ == "__main__":
    this = "ThIs IS my sENtencE"
    print(title_case(this))
