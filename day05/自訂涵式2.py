# 自訂涵式

def add(x, y):  # 無回傳值方法
    print(x + y)


def get_add(x, y):  # 有回傳值方法
    return x + y


# 主程式
if __name__ == '__main__':
    add(10, 20)
    result = get_add(10, 20)
    print(result)
