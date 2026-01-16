# A8Q1
# Question: Write a Python function that takes two file names, datafile1 and datafile2 as
#           input. The function should read the contents of the file datafile1 line by line
#           and should write them to another file datafile2 after adding a newline at the
#           end of each line.
# Name: Satyajeet Nayak
# Appl No: 25C200429

def filecopy(fl1,fl2):
    f1=open(fl1,'w')
    f1.write("My name is Satyajeet\n")
    f1.write("My branch is MCA")
    f1=open(fl1,'r')
    f2=open(fl2,'w')
    print("content of file1")
    for l in f1:
        print(l)
        f2.write(l)

    print("\ncontent of file2")
    f2=open(fl2)
    for l in f2:
        print(l)
    f1.close()
    f2.close()
filecopy('file1','file2')