from setuptools import setup

setup(
	name='stock-ticker',
	version='1.0',
	packages=find_packages(),
	url='https://jackokeeffe.me/',
	license='MIT License',
	author='Jack OKeeffe',
    	description = 'A program to display stock information on LED Matrices',
	install_requires=['pyserial', 'beautifulsoup4'])
