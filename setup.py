from setuptools import setup, find_packages

setup(
    name='iso-lookup',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas'
    ],
    author='Gurmay Malvai',
    description='ISO 639 language code lookup utility',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/iso-lookup',  # replace with your GitHub repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
