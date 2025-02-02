def merge_sort(unsorted_list):
    if len(unsorted_list)<=1:
      return unsorted_list
    middle=len(unsorted_list)//2
    left_list=unsorted_list[:middle]
    right_list=unsorted_list[middle:]
    return merge(merge_sort(left_list),merge_sort(right_list))
def merge(left_half,right_half):
    res=[]
    while len(left_half)!=0 and len(right_half)!=0:
        if left_half[0]<right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0]) 
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half)==0:
        res=res+right_half
    else:
        res=res+left_half
    return res
unsorted_list = [10, 2, 6, 7, 12, 22]
print(merge_sort(unsorted_list))              