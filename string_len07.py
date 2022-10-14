from turtle import clear


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
    a=int(len(s1))
    b=int(len(s2))
    c=int(len(s3))
    ans=[]  
    if a%2==1:
        if b%2==1:
            if c%2==1:
                answer=[s1,s2,s3]
    if a%2==1:
        if b%2==1:
            if c%2==0:
                answer=[s1,s2]
    if a%2==1:
        if b%2==0:
            if c%2==1:
                answer=[s1,s3]
    if a%2==0:
        if b%2==1:
            if c%2==1:
                answer=[s2,s3]
    if a%2==1:
        if b%2==0:
            if c%2==0:
                answer=[s1]   
    if a%2==0:
        if b%2==1:
            if c%2==0:
                answer=[s2]
    if a%2==0:
        if b%2==0:
            if c%2==1:
                answer=[s3] 
    if a%2==0:
        if b%2==0:
            if c%2==0:
                answer=[]                                           
    return str(answer)                                                                        
print(main('example','python','coder'))        