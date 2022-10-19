def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    a=len(s)//2
    if len(s)%2==0:
        return s[a-1]+s[a]
    elif len(s)%2==1:
        return  s[a]  
print(main('cobnol'))        