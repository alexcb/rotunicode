# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from sys import version_info
from setuptools import setup, find_packages
from os.path import dirname, join


def main():
    base_dir = dirname(__file__)
    test_requirements = []
    test_suite = 'test'
    if version_info[0] == 2 and version_info[1] == 6:
        test_requirements.append('unittest2')
        test_suite = 'unittest2.collector'
    setup(
        name='rotunicode',
        version='1.0.2',
        description='Python codec for converting between a string of ASCII '
                    'and Unicode chars maintaining readability',
        long_description=open(join(base_dir, 'README.rst')).read(),
        author='Kunal Parmar',
        author_email='oss@box.com',
        url='https://github.com/box/rotunicode',
        license=open(join(base_dir, 'LICENSE')).read(),
        packages=find_packages(exclude=['test']),
        namespace_packages=['box'],
        tests_require=test_requirements,
        test_suite=test_suite,
        zip_safe=False,
    )


if __name__ == '__main__':
    main()
