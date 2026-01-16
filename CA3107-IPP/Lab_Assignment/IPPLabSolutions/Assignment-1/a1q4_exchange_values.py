# A1Q4
# Question: Write a python program to exchange the value of 4 variables W,G,K,A such that
#           the value of W will move to A, A to K, K to G and finally G to W.
#           Exchange using with and without using extra variables.
# Name: Satyajeet Nayak
# Appl No: 25C200429

A = 10
K = 20
G = 30
W = 40
print("The values of A,K,G,W:", A, K, G, W)
A, K, G, W = W, G, K, A
print("After exchange the values W,G,K,A:", W, G, K, A)
