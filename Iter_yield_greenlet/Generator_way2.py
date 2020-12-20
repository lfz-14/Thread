def create_num(all_num):
    # print("----1---")
    # a = 0
    # b = 1
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # print("----2---")
        # print(a)
        yield a  # 如果一个函数中有yield语句 那么这个就不再是函数，而是一个生成器的模板
        # print("----3---")
        a, b = b, a + b
        current_num += 1
        # print("----4---")
    return "ok...."


obj2 = create_num(20)

# 通过异常捕获判断生成器已经结束
while True:
    try:
        ret = next(obj2)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break

# print(dir(create_num))