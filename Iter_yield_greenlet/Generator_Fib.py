def create_num(all_num):
    print("----1---")
    # a = 0
    # b = 1
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("----2---")
        # print(a)
        yield a  # 如果一个函数中有yield语句 那么这个就不再是函数，而是一个生成器的模板
        print("----3---")
        a, b = b, a + b
        current_num += 1
        print("----4---")


# 如果在调用create_num的时候，发现这个函数中有yield 那么此时，不是调用函数，而是创建一个生成器（generator）对象 yield 可以记录状态
# 用 next()方法时，在yield处暂停，把yield处的值取出来
obj = create_num(10)
obj2 = create_num(2)

ret = next(obj)
print("obj:", ret)

ret = next(obj)
print("obj:", ret)

ret = next(obj2)
print("obj2:", ret)

ret = next(obj)
print(ret)

ret = next(obj2)
print("obj:", ret)
# for num in obj:
#     print(num)
