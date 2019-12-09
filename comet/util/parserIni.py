# coding=utf-8

"""
@作者: Angst
@邮箱: jiqialin@163.com
@开发工具: PyCharm
@创建时间: 2019/12/6 10:24
"""
import configparser
import os


def getIniPath():
    file_path = os.path.join(os.getcwd(), 'properties.ini')
    parser = configparser.ConfigParser()
    parser.read(file_path, encoding="utf-8-sig")
    return parser


def getConfigValue(section, key):
    """
        Reads the value of the configuration file field and returns it.
    :param section:
    :param key:
    :return:
    """
    return getIniPath().get(section, key)
