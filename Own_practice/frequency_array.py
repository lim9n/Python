n,m=map(int,input().split())
a=list(map(int, input().split()))

freq={}

for i in a:
      if i in freq:
            freq[i]+=1
      else:
            freq[i]=1

z
for i in range(1, m+1):

    if i in freq:
        print(freq[i])
    else:
      print(0)