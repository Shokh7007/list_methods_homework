def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    a=list1.count(0)
    b=list1.count(1)
    lst=[a,b]
    return lst 
print(main([1, 0, 0, 0, 1, 0, 1, 0]))