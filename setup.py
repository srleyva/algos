import re
from setuptools import setup, find_packages


required = [
    requirement.strip() for requirement in open('requirements.txt')
    if re.match('^[a-z]', requirement)
]


setup(
    name='algo_practice',
    version='0.1.0',
    packages=find_packages(exclude=('tests')),
    requires=required,
    install_requires=required,
    author='Stephen Leyva',
    author_email='sleyva1297@gmail.com',
    license='MIT',
    zip_safe=True,
)
