def merge(list1,list2):
    result= []
    i=0
    j=0
    while i < len(list1)and j < len(list2):
        if list1[i]['delivery_time']<list2[j]['delivery_time']:
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j+=1
    while i<len(list1):
        result.append(list1[i])
        i+=1
    while j<len(list2):
        result.append(list2[j])
        j+=1
    return result
def merge_sort(orders):
    if len(orders)<=1:
       return orders
    mid=len(orders)//2
    left=orders[:mid]
    right=orders[mid:]
    left_sorted=merge_sort(left)
    right_sorted=merge_sort(right)
    return merge(left_sorted,right_sorted)
orders=[]
n=int(input("how many choice?"))
for i in range(n):
    order_id=input("enter id")
    time=int(input("enter delivery_time"))
    orders.append({'order_id':order_id,'delivery_time':time})
    sorted_order=merge_sort(orders)
    print("\n order sorted by delivery time")
    for o in sorted_order:
     print(o['order_id'],"->",o['delivery_time'], "min")