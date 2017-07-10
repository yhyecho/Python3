# 安装第三方模块
# 在Python中，安装第三方模块，是通过包管理工具pip完成的。

# 现在，让我们来安装一个第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库

# pip install Pillow

from PIL import Image
im = Image.open('dog.jpg')
print(im.format, im.size, im.mode)

im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')

# 其他常用的第三方库还有MySQL的驱动：mysql-connector-python，用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2，等等。

# 模块搜索路径
# 当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：

# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

import sys
print(sys.path)

# 如果我们要添加自己的搜索目录，有两种方法：

# 一是直接修改sys.path，添加要搜索的目录：

# sys.path.append('/Users/yuhuayang/my_py_scripts')

# 这种方法是在运行时修改，运行结束后失效。

# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
# 设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。
