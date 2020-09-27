deadline = {'j1': 7, 'j2': 2, 'j3': 5, 'j4': 3, 'j5': 4, 'j6': 5,'j7': 2,'j8': 7,'j9': 3}
profit = {'j1': 15, 'j2': 20, 'j3': 30, 'j4': 18, 'j5': 18, 'j6': 10,'j7': 23,'j8': 16,'j9': 25}
sortprofit ={}
chart = []
totalprofit = 0
it = 0
def jobsequence(deadline,profit,sortprofit,totalprofit):
    for i in sorted(profit.items(), key=lambda x: x[1], reverse=True):
        sortprofit[i[0]] = i[1]

    for j in range(max(deadline.values())):
        chart.append(0)

    for k in sortprofit:
        if chart[deadline[k]-1] == 0:
            chart[deadline[k]-1] = k
        else:
            for a in range(deadline[k]-1,-1,-1):
                if chart[a] == 0:
                    chart[a] = k

    for n in chart:
        totalprofit = totalprofit + profit.get(n)


    return totalprofit,chart

print(jobsequence(deadline,profit,sortprofit,totalprofit))
