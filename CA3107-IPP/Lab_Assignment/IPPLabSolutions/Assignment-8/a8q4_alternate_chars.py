# A8Q4
# Question: Write a Python function that reads the file file1 and copies only alternative
#           lines to another file file2. Alternative lines copied should be the odd numbered lines.
# Name: Satyajeet Nayak
# Appl No: 25C200429

def filecopy(fl1,fl2):
    f1=open(fl1,'w')
    f1.write("My  name is Satyajeet")
    f1.write("My branch is MCA")
    f1.write("My section is b2")
    f1=open(fl1,'r')
    print("content of file1")
    l=f1.readline()
    print(l)
    f2=open(fl2,'w')
    for i in range(0,len(l),2):
        f2.write(l[i])
    print("\nContent of file2")
    f2=open(fl2)
    for l in f2:
        print(l)
    f1.close()
    f2.close()
filecopy('file1','file2')

