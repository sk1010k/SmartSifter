"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='smartsifter',  # Required
    version='0.1.1.dev1',  # Required
    description='Python implementation of SmartSifter',  # Required
    long_description=long_description,  # Optional
    url='https://github.com/sk1010k/SmartSifter',  # Optional
    author='sk1010k',  # Optional
    license='MIT', # optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='SmartSifter',  # Optional
    install_requires=['scikit-learn>=0.18',
                      'numpy>=1.11',
                      'matplotlib>=2.1'],  # Optional
    python_requires='>=3',
    py_modules=["smartsifter"],
)
