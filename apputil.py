import numpy as np


# update/add code below ...


def ways(n):
    """Return the number of ways to make n cents using pennies and nickels."""
    count = 0

    for nickels in range(n // 5 + 1):
        pennies = n - (nickels * 5)

        if pennies >= 0:
            count += 1

    return count


def lowest_score(names, scores):
    """Return the name of the student with the lowest score."""
    index = np.argmin(scores)
    return names[index]


def sort_names(names, scores):
    """Return student names ordered from highest to lowest score."""
    indices = np.argsort(scores)[::-1]
    return names[indices]
