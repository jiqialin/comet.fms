# coding=utf-8

"""
@作者: Angst
@邮箱: zhouqing@yunjiglobal.com
@开发工具: PyCharm
@创建时间: 2019/12/5 14:35
"""

import os
from setuptools import setup, find_packages


VERSION = '0.1.1'
DESCRIPTION = """
    Used to integrate the httpRunner framework, join up CI/CD to the platform, and upload the results to the platform
    """
PROJECTS = 'https://github.com/jiqialin/comet.fms'
HERE = os.path.abspath(os.path.dirname(__file__))

__version__ = None
with open("comet/models/version.py", 'rb') as f:
    exec(f.read())

# Get the long description from the README file
with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name='comet.fms',
    version=VERSION,
    description=DESCRIPTION,
    long_description=f'Just Enjoy:{long_description}',
    classifiers=[
        # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        # supported python versions
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
      ],
    keywords='python httpRunner jenkins comet.fms terminal CI/CD',
    author='Angst',
    author_email='281491920@qq.com',
    url=PROJECTS,
    license='Angst 1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
          'requests',
          'httprunner',
          'pymysql',
          'requests-toolbelt'
      ],
    entry_points={
        'console_scripts': [
            'comet.fms = comet.comet:MainRun'
        ]
      },
)

print("\nWelcome to Comet!")
print("If you have any questions, please visit our documentation page: {}\n".format(PROJECTS))



