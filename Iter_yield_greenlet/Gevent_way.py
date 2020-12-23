# gevent_img_downloader
# import urllib.request
from urllib.request import urlopen
import gevent
from gevent import monkey

monkey.patch_all()


# <img class="mimg" style="color: rgb(36, 83, 167);" height="180" width="312" src="https://th.bing.com/th/id/OIP.1iK94Nu4m1olgGN5hLa3mgHaEK?w=312&amp;h=180&amp;c=7&amp;o=5&amp;pid=1.7" alt="zard 的图像结果" data-thhnrepbd="1" data-bm="181">
def downloader(img_name, img_url):
    req = urlopen(img_url)

    img_content = req.read()
    with open(img_name, "wb") as f:
        f.write(img_content)
    print("---1---")


# <img src="https://cdn-ak.f.st-hatena.com/images/fotolife/u/uyskun/20171204/20171204165835.jpg" alt="查看源图像" class=" nofocus" tabindex="0" aria-label="查看源图像" data-bm="6">
def main():
    gevent.joinall([
        gevent.spawn(downloader, "C:/Users/LFZ/Pictures/zard/1.jpg",
                     "https://cdn-ak.f.st-hatena.com/images/fotolife/u/uyskun/20171204/20171204165835.jpg"),
        gevent.spawn(downloader, "C:/Users/LFZ/Pictures/zard/2.jpg", "https://zardnet.com/wp-content/uploads/2018/03/29.jpg")
    ])


if __name__ == "__main__":
    main()
