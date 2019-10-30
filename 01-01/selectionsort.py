def selection(lis):
    iterasi = 0
    for i in range(len(lis)-1):
        minimal = i
        for j in range(i+1,len(lis)):
            if lis[j] < lis[minimal]:
                minimal = j
        iterasi += 1
        lis[minimal],lis[i]= lis[i],lis[minimal]
        print(iterasi,lis)
lis=[54,26,93,17,77,31,44,55,20,21,34,65,70]
selection(lis)