"""Setup.py for Pypi.org"""
from distutils.core import setup

setup(
    name='searchin',
    packages=['searchin'],
    version='0.2.2',
    description='Search anything in a live python object, method or variable',
    author='Nicolas Micaux',

    url='https://github.com/NicolasMICAUX/searchin',
    # download_url='https://github.com/NicolasMICAUX/searchin/archive/refs/tags/v0.1.5.tar.gz',

    install_requires=[],  # None

    keywords=['search', 'debug', 'inspect'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    python_requires='>=2.7',

    # Set README.md as description
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
