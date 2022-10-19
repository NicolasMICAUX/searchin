"""Setup.py for Pypi.org"""
from distutils.core import setup

setup(
    name='searchin',
    packages=['searchin'],
    version='0.1',
    description='Search anything in a live python object/method/variable!',
    author='Nicolas Micaux',  # Type in your name
    author_email='your.email@domain.com',  # Type in your E-Mail
    url='Search anything in a live python object/method/variable!',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',  # I explain this later on
    keywords=['SEARCH', 'DEBUG'],
    install_requires=[],  # None
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)