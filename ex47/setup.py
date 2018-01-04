try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = [
	'description': 'My Project',
	'author': 'Rohith Sreeramdas',
	'url': 'url to get it at',
	'download_url': 'url to download from',
	'author_email': 'rohith.iitb@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],	
	'name': 'projectname'
]

setup(**config)
