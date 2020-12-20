# nums = [x*2 for x in range(10)]  #
#
#
# nums = (x*2 for x in range(10))  # 节省空间  返回值是一个 generator object


def create_num(all_num):
    # a = 0
    # b = 1
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # print(a)
        yield a  # 如果一个函数中有yield语句 那么这个就不再是函数，而是一个生成器的模板
        a, b = b, a + b
        current_num += 1


# 如果在调用create_num的时候，发现这个函数中有yield 那么此时，不是调用函数，而是创建一个生成器（generator）对象 yield 可以记录状态
# 在yield处暂停，把yield处的值取出来
# print(create_num(10))

obj = create_num(10)
for num in obj:
    print(num)
