from setuptools import setup, find_packages
import codecs
import os

HERE = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(HERE, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.8'
DESCRIPTION = "'Python program that visualizes data from a .csv file.'"
LONG_DESCRIPTION = ""

setup(
    name='data-visualizer',
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=long_description,
    license='MIT',
    author='Asley R.',
    author_email='asleyrobleto@gmail.com',
    url='https://github.com/AsleyR/Data-Visualizer',
    packages=find_packages(exclude=('tests*', 'test*', 'testing*')),
    install_requires=['pysimplegui'],
    keywords=[
        'python', 'data', 'csv',
        'visualization', 'data visualization',
        "data parsing"
        ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts': [
            'data-visualizer=data_visualizer.__main__:main',
            'dvisual=data_visualizer.__main__:main'
        ],
    },
)
