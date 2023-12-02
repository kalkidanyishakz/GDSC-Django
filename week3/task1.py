for i in range(100):    
    print(("0" if len(str(i))==1 else "") +str(i),end= "\n" if i==99 else ", ")
    
