"""
molsii_math.py
sermacs workshop

Handles the primary functions
"""


def mean(num_list):
    """
    This function calculates the mean of a list
    
    Parameters
    ___________________
    num_list: list
       list to calculate mean of
    Returns
    __________________
    mean: float
         calculated mean
    """
    mean = 0
    if not isinstance(num_list, list):
        raise TypeError('Input must be list of ints or float')
    if len(num_list) < 1:
        raise TypeError('Empty list')
    for entry in num_list:
        if isinstance(entry, int) or isinstance(entry, float):
           mean += entry
        else:
           raise TypeError('Entry not int or float')
    mean = mean / len(num_list)

    return mean

if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
