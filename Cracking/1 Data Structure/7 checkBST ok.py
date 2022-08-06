min_value = -9999999999
max_value = 9999999999

def checkBST(root):
    return check(root, min_value, max_value)
    

def check(n, mini, maxi):
    if n == null:
        return true
    return (mini < n.data and n.data < maxi) and (check(n.left, mini, n.data) and  check(n.right,n.data, maxi))

