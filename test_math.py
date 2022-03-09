import argparse

def add_nums(a,b):
   return a+b

def mul_nums(c,d):
   return c+d

if __name__=="__main__":
   parse=argparse.ArgumentParser(description="Calculate")
   parse.add_argument('a',type=int,help='first num')
   parse.add_argument('b',type=int,help='second num')
   args=parse.parse_args()
   print(add_nums(args.a,args.b))