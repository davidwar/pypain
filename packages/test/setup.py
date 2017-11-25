from distutils.core import setup
setup(
  name = 'mypackage',
  packages = ['mypackage'], # this must be the same as the name above
  version = '0.1',
  description = 'test package',
  author = 'umm0n',
  author_email = 'bla',
  url = 'https://github.com/davidwar/pypain', # use the URL to the github repo
  download_url = 'https://github.com/davidwar/pypain/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)