def main(a):
    """
    A string type variable is given. Return True if its length is even. Return False if its length is odd.
    Args:
        a: string
    Returns:
        True or False
    """
    b=len(a)
    if b%2==0:
        return True
    elif b%2==1:
        return False    
print(main(' code'))        