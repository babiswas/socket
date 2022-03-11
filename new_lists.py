from itertools import islice

def convert_list_nested(l):
    it=iter(l)
    master_list=list()
    while True:
       k=list(islice(it,3))
       if k:
          master_list.append(k)
       else:
         break
    return master_list

if __name__=="__main__":
   print(convert_list_nested([1,2,3,4,5,6,6,6,6,9]))
   
   