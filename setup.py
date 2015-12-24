# coding: utf-8

from __future__ import print_function, unicode_literals

import sys

from setuptools import setup

install_requires = []
if sys.version_info[0] == 2:
    install_requires.append('statistics')

setup(
    name='scrapy-slotstats',
    version='0.1',
    license='MIT License',
    description='Scrapy extension to show statistics of downloader slots',
    author='orangain',
    author_email='orangain@gmail.com',
    url='https://github.com/orangain/scrapy-slotstats',
    keywords="scrapy downloader slot stats",
    py_modules=['scrapy_slotstats'],
    platforms=['Any'],
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Scrapy',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ]
)
