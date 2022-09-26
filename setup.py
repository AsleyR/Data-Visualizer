from setuptools import setup, find_packages

setup(
    name='data-visualizer',
    version='0.1.1',
    description='Python program that visualizes data from a .csv file.',
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