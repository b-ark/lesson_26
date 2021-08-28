# Implement binary search using recursion.


def binary_search(data: list, bottom, top, x):
    if top > bottom:
        middle = (top + bottom) // 2

        if data[middle] == x:
            return middle

        elif data[middle] < x:
            return binary_search(data, middle + 1, top, x)

        elif data[middle] > x:
            return binary_search(data, bottom, middle - 1, x)

    else:
        raise IndexError(f'Element {x} is not found in list {data}')


def main():
    arr = list(range(0, 101))
    print(binary_search(arr, 0, len(arr), 150))


if __name__ == '__main__':
    try:
        main()
    except IndexError as massage:
        print(massage)
