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

    if len(num_list) > 0:
        mean = sum(num_list) / len(num_list)

    return mean

if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
