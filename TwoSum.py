class ts:
    def sol(self,mlist,target):
        l=[(v,i) for i,v in enumerate(mlist)]
        print(l)
        mlist.sort()
        begin=0
        end=len(mlist)-1

        while begin<end:
            sum=l[begin][0]+l[end][0]
            if sum==target:
                return [l[begin][1],l[end][1]]
            elif sum>target:
                end = end -1
            else:
                begin = begin + 1
ob = ts()
print(ob.sol([4,5,3,7,8],11))
