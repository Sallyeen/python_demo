# 设计一个函数返回给定文件名的后缀名

def last_name(seq):
    seq = input("请输入文件名：").split(".")
    return seq[-1]

def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.') # rfind 最后一次出现的位置
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


