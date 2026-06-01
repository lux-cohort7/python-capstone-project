"""
Write is_valid_score(score) — validate input #13
Task description
Write a function that takes a score and returns True if it is a number between 0 and 100, and False otherwise.
print(is_valid_score(105))
print(is_valid_score(75))
False
True
"""

# creating a function 

def is_valid_score(score:float)-> bool:
    """
    This function takes one float or numeric value and returns a boolean value
    The function validates if the student score is True if score is a figure between 0 and 100 
    and False is otherwise.
    """
    try:
        num_score = float(score)
        return num_score >=0 and num_score <= 100
    except Exception as e:
        return False


# Test score 105,75 and "one"

print(is_valid_score(105))

print(is_valid_score(75))

print(is_valid_score("one"))

# help(is_valid_score)
