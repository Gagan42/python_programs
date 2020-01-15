

test_str = 'ad poipo kmlv djfjdk fskdj flkd sdfkoepsdsd gsgdfdsjcz cggga'
cnt=0
gag=0
res=''
i=0
# print(len(test_str))
for i in test_str:
    cnt=cnt+1
    gag=gag+1
    res =res + i
    if (i==' ' or cnt==len(test_str)) and (((gag/10)>=1) or cnt==len(test_str)):
        print(res.lstrip())
        gag=0
        res=''    


    # ((cnt>=10) or (cnt==len(test_str)))
          



      
    
    
    
 



    