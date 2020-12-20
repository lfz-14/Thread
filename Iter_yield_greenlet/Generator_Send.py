def create_num(all_num):
    a, b = 0, 1
    current_num = 0   #
    while current_num < all_num:
        ret = yield a  # 如果一个函数中有yield语句 那么这个就不再是函数，而是一个生成器的模板  yield最大特点：可以让这个函数先暂停执行
        print(">>>ret>>>", ret)
        a, b = b, a + b
        current_num += 1

obj = create_num(10)

# 生成器特点：让一个函数暂停执行
# obj.send(None) 一般不会放到第一次启动生成器，如果非要这样做 那么传递None
ret = next(obj)
print(ret)

# send里面的数据会 传递给第5行，当做yield a 的结果，然后ret保存这个结果，，，
# send的结果是下一次调用yield时 yield后面的值
ret = obj.send('hahahah')  # yield 的值给ret    即 ret = yield a (分两步走，先执行等号右边，再做赋值)
print(ret)