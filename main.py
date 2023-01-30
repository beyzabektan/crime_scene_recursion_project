file_open=open("crime_scene.txt", "r")
str1=str(file_open.read())
file_open.close()
lst1=str1.split("\n")
while "" in lst1:
    lst1.pop(lst1.index(""))
first_line=lst1[0].split(" ")
max_weight=int(first_line[0])
max_time=int(first_line[1])
n=int(lst1[1])

bubble_count=0
def my_bubble_sort(lst):
    global bubble_count
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if (lst[j]>lst[j+1]):
                #swap lst[j] with lst[j+1]
                lst[j],lst[j+1] = lst[j+1],lst[j]
                bubble_count += 1
    return lst

weight=dict()
for i in lst1[2:]:
    weight[i.split()[0]]=i.split()[1]

time=dict()
for i in lst1[2:]:
    time[i.split()[0]]=i.split()[2]

value=dict()
for i in lst1[2:]:
    value[i.split()[0]]=i.split()[3]


def f1(limit_left,i):
    if i==n:
        return 0,[]
    if limit_left- int(list(weight.values())[i])>=0:
        collected, collectedlist1=f1(limit_left-int(list(weight.values())[i]),i+1)
        collected+=int(list(value.values())[i])
        collectedlist1.append(list(value.keys())[i])
    else:
        collected=0
        collectedlist1=[]

    uncollected, uncollectedlist1=f1(limit_left,i+1)
    if collected>uncollected:
        return collected, collectedlist1
    else:
        return uncollected, uncollectedlist1

sorted1=[]
for i in f1(max_weight,0)[1]:
    sorted1.append(int(i))
sorted11=my_bubble_sort(sorted1)

file1 = open("solution_part1.txt", "w")
file1.write(str(f1(max_weight,0)[0])+"\n")
for i in range(len(sorted11)):
    file1.write(str(sorted11[i])+" ")
file1.close()

def f2(limit_left,i):
    if i==n:
        return 0,[]
    if limit_left- int(list(time.values())[i])>=0:
        collected, collectedlist2 = f2(limit_left-int(list(time.values())[i]),i+1)
        collected+=int(list(value.values())[i])
        collectedlist2.append(list(value.keys())[i])
    else:
        collected=0
        collectedlist2=[]

    uncollected, uncollectedlist2 = f2(limit_left,i+1)
    if collected>uncollected:
        return collected, collectedlist2
    else:
        return uncollected, uncollectedlist2

sorted2=[]
for i in f2(max_time,0)[1]:
    sorted2.append(int(i))
sorted22=my_bubble_sort(sorted2)
file2 = open("solution_part2.txt", "w")
file2.write(str(f2(max_time,0)[0])+"\n")
for i in range(len(sorted22)):
    file2.write(str(sorted22[i])+" ")
file2.close()

def f3(limit_left1,limit_left2,i):
    if i==n:
        return 0,[]
    if limit_left1- int(list(weight.values())[i])>=0 and limit_left2-int(list(time.values())[i])>=0:
        collected, collectedlist3=f3(limit_left1-int(list(weight.values())[i]),limit_left2-int(list(time.values())[i]),i+1)
        collected+=int(list(value.values())[i])
        collectedlist3.append(list(value.keys())[i])
    else:
        collected=0
        collectedlist3=[]

    uncollected, uncollectedlist3=f3(limit_left1,limit_left2,i+1)
    if collected>uncollected:
        return collected, collectedlist3
    else:
        return uncollected, uncollectedlist3

sorted3=[]
for i in f3(max_weight,max_time,0)[1]:
    sorted3.append(int(i))
sorted33=my_bubble_sort(sorted3)
file3 = open("solution_part3.txt", "w")
file3.write(str(f3(max_weight,max_time,0)[0])+"\n")
for i in range(len(sorted33)):
    file3.write(str(sorted33[i])+" ")
file3.close()
