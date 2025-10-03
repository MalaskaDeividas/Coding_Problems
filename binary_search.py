

def ok(x): 
    # return True/False if x is feasible
    return True
lo, hi = -1, 10**18
while hi-lo>1:
    mid=(lo+hi)//2
    if ok(mid): hi=mid
    else: lo=mid
print(hi)
