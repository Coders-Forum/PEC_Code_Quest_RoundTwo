def bonAppetit(bill, k, b):
    half= sum(bill) / 2
    bill.pop(k)
    anna= sum(bill) / 2
    
    if b == anna:
        print('Bon Appetit')
    else:
        print(int(half - anna))
