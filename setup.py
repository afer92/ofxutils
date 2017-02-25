from setuptools import setup

setup(name = 'ofxutils',
	version = '1.0',
	author = 'afer92',
	author_email = 'ferraro.alain@free.fr',
	
	url = "http://github.com/afer92/ofxutils",
	keywords = 'ofx ofc qif utilities',
	description = 'Provide tools for financial file parsing and conversion.',
	license = 'GNU General Public License (GPL)',
	packages = ['ofxutils'],
	install_requires = ['BeautifulSoup'],
	
	classifiers = [
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: GNU General Public License (GPL)',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
	],
)
