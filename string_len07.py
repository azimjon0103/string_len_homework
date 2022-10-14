def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    a=len(s1)
    b=len(s2)
    c=len(s3)
    answer = ''
    if a%2==1:
        answer += s1+", "
    if b%2==1:
        answer += s2+", "
    if c%2==1:
        answer += s3
    return  '['+answer+']'                                                               
print(main('example ','pytho n','cod er'))        