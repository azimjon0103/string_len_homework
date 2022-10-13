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
    ans=[]  
    if a%2==1:
        asnwer=[s1]
    if a%2==0:
        answer=[]
    if b%2==1:
        answer=[s1,s2]
    if b%2==0:
        answer=[s1]
    if c%2==1:
        answer=[s1,s2,s3]
    if c%2==0:
        answer=[s1,s2]
    if b%2==0:
        answer=[s1,s3]
    return answer                                                                        
print(main('example','python ','coder'))        