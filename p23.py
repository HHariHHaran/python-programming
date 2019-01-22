def main():
    n,m=map(int,input().split())
    l=[]
    l=list(map(int,input().split()))
    k=map(int,input().split())
    for i in m:
if i not in l:
   l.append(i)
    print(n,len(l))
if __name__ == '__main__':
   
   main()
