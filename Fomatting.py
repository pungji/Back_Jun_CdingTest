def cal(a,b,c):
   
 return(a+b+c)
  
a,b,c = map(int,input().split())

d =cal(a,b,c)
e = d
e=e/3
print('{0}'' ''{1:0.2f}'.format(d,e)) #포메팅 {0}은 합 {1}은 평균(소수점 3자리에서 올림)