from setuptools import setup, find_packages

setup(
    name='iso639lookup',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "iso639lookup": ["resources/*.csv"]
    },
    install_requires=[
        'pandas'
    ],
    author='Gurmay Malvai',
    description='ISO 639 language code lookup utility',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/GMZone16/iso639lookup/',  # replace with your GitHub repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.9',
)
