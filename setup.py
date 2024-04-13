# setup.py

from setuptools import setup, find_packages

setup(
    name='image-preprocessorpy',
    version='1.0.1',
    description='A package for preprocessing images by resizing and cropping them to a target size.',
    author='Avinrique',
    author_email='avinrique@example.com',
    url='https://github.com/avinrique/image-preprocessor',
    packages=find_packages(),
    install_requires=[
        'Pillow>=8.4.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
