profit = [25,24,15]
weight = [18,15,10]
cap = 20
pr = 0
prwe = {}
sortdic = {}
def knapsack(profit,weight,cap,pr):
    for i in range(len(profit)):
        prwe[i] = profit[i]/weight[i]

    for j in sorted(prwe.items(), key=lambda x: x[1], reverse=True):
        sortdic[j[0]] = j[1]

    for k in sortdic.keys():
        if cap > 0 and weight[k] <= cap:
            cap = cap - weight[k]
            pr = pr + profit[k]
        else:
            break
    if cap > 0:
        pr = pr + profit[k]*(cap/weight[k])

    return pr


print(knapsack(profit, weight, cap, pr))