# A8Q2
# Question: Write a Python function that reads a file file1 and displays the number
#           of words and the number of vowels in the file.
# Name: Satyajeet Nayak
# Appl No: 25C200429

def filecount(fl1):
    f1=open(fl1,'w')
    f1.write("My  name is Satyajeet")
    f1.write("My branch is MCA")
    c=0
    cv=0
    f1=open(fl1,'r')
    l=f1.readlines()
    for line in l:
        c+=len(line.split())
        for ch in line:
            if ch.isalpha() and ch in 'aeiouAEIOU':
                cv+=1

            
    print("count of words:",c," ","count of vowels:",cv)
    f1.close()
filecount('file1')