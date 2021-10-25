def grid_travel_brute(x, y):
    """
    x: width of grid
    y: height of griad

    Time: O(2^(x+y))
    Space: O(x + y)
    """

    if x == 0 or y == 0:
        return 0

    if x == 1 and y == 1:
        return 1

    return grid_travel_brute(x - 1, y) + grid_travel_brute(x, y - 1)


def grid_travel_w_memo(x,y,memo):
    if (x,y) in memo:
        return memo[(x,y)]

    if x == 0 or y == 0:
        return 0

    if x == 1 and y == 1:
        return 1

    memo[(x,y)] = grid_travel_w_memo(x - 1, y, memo) + grid_travel_w_memo(x, y - 1, memo)
    return memo[(x,y)] 


if __name__ == "__main__":
    # print(grid_travel_brute(0, 1))
    # print(grid_travel_brute(1, 1))
    # print(grid_travel_brute(2, 3))
    # print(grid_travel_brute(3, 3))

    print(grid_travel_w_memo(0, 1, {}))
    print(grid_travel_w_memo(1, 1, {}))
    print(grid_travel_w_memo(2, 3, {}))
    print(grid_travel_w_memo(3, 3, {}))
    print(grid_travel_w_memo(18, 18, {}))
