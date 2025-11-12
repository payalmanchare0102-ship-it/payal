profit=[60,100,120]
weight=[10,20,30]
capacity=50
ratio=[]
for i in range(len(profit)):
    ratio.append(profit[i]/weight[i])
    items=list(zip(profit,weight,ratio))
    items.sort(key=lambda x:x[2],reverse=True)
    total_profit=0
    current_weight=0
    for profit,weight,r in items:
        if current_weight + weight<=capacity:
            current_weight+=weight
            total_profit+=profit
        else:
            ramain=caapacity-current_weight
            total_profit+=profit*(remain/weight)
            break
            print("maximum profit=",total_profit)