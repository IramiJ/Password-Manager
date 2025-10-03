import random

def generate_password(u=True, l=True, d=True, s=True, length=12):
 upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 digits = ['0','1','2','3','4','5','6','7','8','9','10']
 symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=']
 chars = []
 password = ""
 if u:
  chars += upper
 if l:
  chars += lower
 if d: 
  chars += digits
 if s:
  chars += symbols
 for i in range(length):
  password += chars[random.randint(0, len(chars)-1)]
 return password