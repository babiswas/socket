import re
str1="The Congress has time and again accused the government of stalling the hike in fuel prices to gain mileage among voters ahead of elections and raising the prices again soon after the polls come to an end."
str2="Hey, I’m Dan! Obsessed with exploring the world, meeting new people and getting as lost as possible with my camera. I was on the road for 1467 days between 2014 – 2018, taking a chance on changing my career from restaurant manager to capturing the world and somehow it all worked out… I’m now starting a new chapter living in Portugal."

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

def find_words_starting(ch):
    expression='\s['+ch+ch.upper()+']'+'\w+\s'
    l=re.findall(expression,str1)
    return list(map(lambda x:x.strip(),l))

def get_words_ending_in_comma():
    expression='\w+[,.]'
    l=re.findall(expression,str2)
    return list(map(lambda x:x[:-1].strip(),l))

def get_all_words():
    expression='\w+[,.]\s\w+\s'
    l=re.findall(expression,str2)
    return list(map(lambda x:x.strip(),l))

def get_all_digits():
    expression='\d{4}'
    l=re.findall(expression,str2)
    return l

def get_all_word_ended(str1):
    expression='[\sA-Za-z]\w+'+str1+'\s'
    l=re.findall(expression,str2)
    return list(map(lambda x:x.strip(),l))





if __name__=="__main__":
   for i in range(20):
     print(find_all_n_letters(i))
   print(find_word_endingin_dot())
   print(find_words_starting_the())
   for ch in ['a','b','c','d','p','q','e','f','g','h','i','j','k','l','m','n','o','t','u','v','w','x','y','z']:
      print(find_words_starting(ch))
   print(get_words_ending_in_comma())
   print(get_all_words())
   print(get_all_digits())
   print(re.findall('\d{4}\s.\s\d{4}',str2))
   print(get_all_word_ended("ing"))
   print(get_all_word_ended("ed"))
   print(get_all_word_ended("l"))
   print(get_all_word_ended("e"))
   print(get_all_word_ended("y"))
   print(get_all_word_ended("d"))
   print(get_all_word_ended("h"))
   

   