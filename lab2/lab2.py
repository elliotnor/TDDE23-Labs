def check_pnr(lst):
    """The main function"""
    check_num = round_up(summarize(mult(lst)))
    return lst[-1] == check_num

def mult(lst):
    """Executes multiplication with 1 / 2"""
    mult_lst = lst[:-1]
    for i in range(0, len(lst), 2):
        mult_lst[i] = lst[i] * 2
    return mult_lst

def summarize(lst):
    """Summarizes the individual numbers"""
    result = []
    for n in lst:
        the_sum = sum(int(digit) for digit in str(n))
        result.append(the_sum)
    return sum(result)

def round_up(n):
    return abs(round(n+1,-1) - n)

assert check_pnr([7,2,0,1,2,3,1,2,3,5]) == True
assert check_pnr([0,1,0,9,2,5,7,7,3,3]) == True
assert check_pnr([0,1,0,9,2,5,7,7,3,9]) == False
assert check_pnr([0,1,0,1,1,1,0,5,0,0]) == True
assert check_pnr([0,1,0,1,1,1,0,5,0,1]) == False
