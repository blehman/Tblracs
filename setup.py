from distutils.core import setup

setup(
    name='tblracs',
    version='0.1.0',
    author='Scott Hendrickson',
    author_email='scott@drskippy.net',
    packages=['tblracscsv'],
    scripts=['tblracs.py','tblracs-prettifier.py'],
    url='http://pypi.python.org/pypi/tblracs/',
    license='LICENSE.txt',
    description='Gnip normalized Tumblr JSON activity to csv parser.',
    long_description=open('README.txt').read(),
    install_requires=[
        "ujson >= 1.2",
    ],
)
