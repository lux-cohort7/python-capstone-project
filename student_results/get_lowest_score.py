def get_lowest_score(scores):
    """ Finds minimum value inside the passed list
        
        Args: 
            scores (list) : A list of the scores are passed as the input

        Returns:
            int - the output is the minimum from the passed list
    """
    min_value = scores[0]

    for score in scores:
        if  score < min_value :
            min_value = score

    return min_value

if __name__ =="__main__" :
    print(get_lowest_score([55, 90, 73, 88]))