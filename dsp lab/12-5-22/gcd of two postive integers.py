def gcd(p,q):
     while q!=0:
          p,q=q,p%q
     return p
def is_coprime(x,y):
     return gcd(x,y)==1
print(is_coprime(2,3))
print(is_coprime(17,21))
print( is_coprime(15,21))
print( is_coprime(25,45))
