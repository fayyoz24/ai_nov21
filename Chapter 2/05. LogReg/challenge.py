class Challenge:
    def pyramids1(self, n):
        for i in range(n+1):
            return (i * '# ') # space is added to separate
    
    def pyramids2(self, n):
        hash = 0
        line = 1
        while(line <= n ):
    
            if (hash < line):
                print("# ", end = "")
                hash += 1
                continue
        
            if (hash == line):
                print("")
                line += 1
                hash = 0

    def pyramids3(self, n):
        space = n-1
        hash = 1
        for i in range(n):
            print(space*' '+ hash*'# ')
            space -=1
            hash +=1

    def strive(self, list_):
        b = list()
        for i in list_:
            if (i%3 == 0) and (i%5 == 0):
                b.append('Strive School')
                continue
            elif i % 3 == 0:
                b.append('Strive')
            elif i % 5 == 0:
                b.append('School')
            else:
                b.append(i)
        return b

    def non_duplic(self, list_):
        return [i for i in list_ if list_.count(i) < 2]

    def sec_agent(self, arr):
        num_lists = len(arr)
        list_ = []
        for i in range(num_lists):

            if len(arr[i]) != 2:
                return -1
            for j in arr[i]:
                list_.append(j)
        non_dup_names = list(dict.fromkeys(list_))
        if len(non_dup_names) != num_lists:
            return -1

        eve_sec_name_in_peop = [list_[j] for j in range(len(list_)) if j%2==0]
        for sec_ag_name in eve_sec_name_in_peop:
            if eve_sec_name_in_peop.count(sec_ag_name)==2:
                return sec_ag_name
        return 0

