stu_rank = {"shweta" : "a1", "rishu" :"a2"}
print(stu_rank["shweta"])
for x in stu_rank:
    print(x, stu_rank[x])
stu_rank.pop("rishu")    
print(stu_rank)
stu_rankcopy = dict.fromkeys(stu_rank, stu_rank)
print(stu_rankcopy)


