def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    a=0
    while a<len(fruits):
        if fruits[a]=="apple":
            fruits.pop(a)
        else:
            a+=1
    return fruits
print(main(["apple", "banana", "apple", "pear", "apple"]))