profits=[60,100,120]
weights=[10,20,30]
capacity=50
ratio=[]
for i in range(len(profits)):
    ratio.append(profits[i]/weights[i])
items=list(zip(profits,weights,ratio))
items.sort(key=lambda x:x[2],reverse=True)
total_profit=0
current_weight=0
for profit,weight,r in items:
    if current_weight + weight<=capacity:
        total_profit+=profit
        current_weight+=weight
    else:
        remain=capacity-current_weight
        total_profit+=profit*(remain/weight)
        break
print("maximum_profit:",total_profit)