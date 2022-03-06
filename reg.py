import re
str1="The Congress has time and again accused the government of stalling the hike in fuel prices to gain mileage among voters ahead of elections and raising the prices again soon after the polls come to an end."

def find_all_n_letters(n):
    expression='\s\w{'+str(n)+'}\s'
    l=re.findall(expression,str1)
    if l:
      return list(map(lambda x:x.strip(),l))
    else:
      return ''

def find_word_endingin_dot():
    expression='\s\w+\.'
    l=re.findall(expression,str1)
    return list(map(lambda x:x.strip(),l))

def find_words_starting_the():
    expression='[T,t]he\s\w+\s\w+\s'
    l=re.findall(expression,str1)
    return list(map(lambda x:x.strip(),l))




if __name__=="__main__":
   for i in range(20):
     print(find_all_n_letters(i))
   print(find_word_endingin_dot())
   print(find_words_starting_the())
   