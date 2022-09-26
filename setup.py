from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.2'
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
    install_requires=['pysimplegui', 'pydub'],
    keywords=['python', 'data', 'csv', 'visualization', 'data visualization'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)