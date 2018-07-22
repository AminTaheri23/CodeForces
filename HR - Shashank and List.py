# https://www.hackerrank.com/challenges/shashank-and-list/problem

n = int ( input ( ) )
lst = [ ]
for i in range ( n ):
    lst.append ( int ( input ( ) ) )
bb=0
for i in range(n):
    size=n
    item=0
    result = [sublist for sublist in
            (lst[x:x+size] for x in range(len(lst) - size + 1))
            if item not in sublist
        ]
    sublist=[]
    x=0
    for j in range(len(result)):
        bb += 2**sum(result[j])
print(bb)
