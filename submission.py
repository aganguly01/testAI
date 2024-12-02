def __isBulky(width, height, length):
    if max(width, height, length) >= 150 or width*height*length >= 1000000 :
        return True
    return False

def __isHeavy(mass):
    if mass >=20:
        return True
    return False

def sort(width, height, length, mass):
    for ele in [width, height, length, mass]:
        if ele < 0:
            return f'INVALID INPUT {ele}'

    isHeavy = __isHeavy(mass)
    isBulky = __isBulky(width, height, length)
    if not isHeavy and not isBulky:
        return 'STANDARD'

    if isHeavy and  isBulky:
        return 'REJECTED'

    if isHeavy or isBulky:
        return 'SPECIAL'

def main():
        assert(sort(10, 10, 10, 5)=='STANDARD')
        assert(sort(150, 10, 10, 5)=='SPECIAL')
        assert(sort(140, 10, 10, 20)=='SPECIAL')
        assert(sort(100, 100, 100, 20)=='REJECTED')
        assert('INVALID INPUT' in sort(10, 10, 10, -5))

if __name__=="__main__":
    main()
