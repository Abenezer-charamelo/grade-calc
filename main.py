convertion = {"a":4,"b":3,"c":2,"d":1,"f":0}
subj = [("A",5),("B",5),("C",5),("D",5),("F",5)]
#tuple = (grade,cr_hr)
#lst = [(grade,cr_hr),(grade,cr_hr),(grade,cr_hr),(grade,cr_hr),.......]

def gpa_calc(lst):
    average = 0
    total_cr = 0
    for i in lst:
        average += ((convertion[i[0].lower()])*i[1])
        total_cr += i[1]
    return float(average/total_cr)

#lst = [("A",5),("A",5),("A",5),("A",5),("B",5),("B",5)]

#gpa = gpa_calc(lst)

#print(gpa)
 
"""def posib():
    possible_v=[]
    for a in range(7):
        for b in range(7):
            for c in range(7):
                for d in range(7):
                    for f in range(7):
                        if a+b+c+d+f == 6 :
                            possible_v.append((a,b,c,d,f))
    return possible_v
val = posib()
def main():
    for i in val:
        lst = []
        for j in range(i[0]):
            lst.append(subj[0])
        for j in range(i[1]):
            lst.append(subj[1])
        for j in range(i[2]):
            lst.append(subj[2])
        for j in range(i[3]):
            lst.append(subj[3])
        for j in range(i[4]):
            lst.append(subj[4])
        print(lst)
#main()
#print(len(val))
#print(val)        
"""           
def main():
    lst = []
    count = 0
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for f in range(5):
                        lst.append(subj[a])
                        lst.append(subj[b])
                        lst.append(subj[c])
                        lst.append(subj[d])
                        lst.append(subj[f])
                        print("{}-----------{}".format(lst,gpa_calc(lst)))
                        count += 1
                        lst.clear()
    print(count)
main()
                        
                        
                        
    
    
    
