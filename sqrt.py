

def mySqrt(x):
    if x == 0 or x == 1:
        return x

    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return right


x = 10
print(mySqrt(x))