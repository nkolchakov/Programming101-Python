
from collection import Collection

def main():
    c = Collection(1,2,3)
    assert c == c.map(lambda x: x)
    assert Collection(2) == c.filter(lambda x: x % 2 == 0)
    assert 6 == c.reduce(0, lambda x, y: x + y)
    assert Collection(1, 2) == c.take(2)
    assert Collection(3) == c.drop(2)
    assert Collection(0, 0, 0) == Collection(0, 0, 0, 1).take_while(lambda x: x == 0)
    assert Collection(1) == Collection(0, 0, 0, 1).drop_while(lambda x: x == 0)
    assert Collection(1).search(1)
    print('tests passed !')

if __name__ == '__main__':
    main()