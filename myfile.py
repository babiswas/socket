import csv

def create_read_csv(filename):
    with open(filename,'w') as file:
        column=['column1','column2','column3']
        new_file=csv.DictWriter(file,fieldnames=column)
        new_file.writeheader()
        new_file.writerow({'column1':"hello",'column2':"bello",'column3':"mello"})
        new_file.writerow({'column1':"tello1",'column2':"tello2",'column3':"tello3"})
    with open(filename,'r') as file:
        new_file=csv.DictReader(file)
        for row in new_file:
           print(row)

if __name__=="__main__":
   create_read_csv("test1.csv")
   