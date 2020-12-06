tupleList1=[('parent', 'Amina', 'Rakib', 'female', 'male'),
            ('parent', 'Hasib', 'Rakib', 'male', 'male'),
            ('parent', 'Rakib', 'Sohel', 'male', 'male'),
            ('parent', 'Rakib', 'Rebeka', 'male', 'female'),
            ('parent', 'Rakib', 'Priya', 'male', 'female'),
            ('parent', 'Rebeka', 'Jamal', 'female', 'male'),
            ('parent', 'Rebeka', 'Mina', 'female', 'female')]

X=str(input("\nChild:"))
print('Grandparent:', end=' ')
i=0
while(i<=6):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(7):
            if ((tupleList1[j][0] == 'parent') & ( tupleList1[i][1] == tupleList1[j][2])):
                print(tupleList1[j][1], end=' \n')   
    i=i+1 

print('Sister:', end=' ')
i=0
while(i<=6):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(7):
            if ((tupleList1[j][0] == 'parent') & ( tupleList1[i][1] == tupleList1[j][1]) & (i!=j) & (tupleList1[j][4]=='female')):
                print(tupleList1[j][2], end=' \n')   
    i=i+1

print('Brother:', end=' ')
i=0
while(i<=6):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(7):
            if ((tupleList1[j][0] == 'parent') & ( tupleList1[i][1] == tupleList1[j][1]) & (i!=j) & (tupleList1[j][4]=='male')):
                print(tupleList1[j][2], end=' \n')   
    i=i+1  

print('Aunt:', end=' ')
i=0
while(i<=6):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(7):
            if ((tupleList1[j][0] == 'parent') & ( tupleList1[j][2] == tupleList1[i][1])):
                for k in range(7):
                    if((tupleList1[k][0] == 'parent') & (tupleList1[j][1] == tupleList1[k][1]) & (j!=k)& (tupleList1[k][4] == 'female') ):
                        print(tupleList1[k][2], end=' \n')   
    i=i+1

print('Uncle:', end=' ')
i=0
while(i<=6):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(7):
            if ((tupleList1[j][0] == 'parent') & ( tupleList1[j][2] == tupleList1[i][1])):
                for k in range(7):
                    if((tupleList1[k][0] == 'parent') & (tupleList1[j][1] == tupleList1[k][1]) & (j!=k)& (tupleList1[k][4] == 'male') ):
                        print(tupleList1[k][2], end=' \n')   
    i=i+1 
