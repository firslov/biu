from setuptools import setup, find_packages

with open("readme.org", "r") as f:
    readme = f.read()

BIUSRC = ['**.hy']

setup(
    name='pybiu',
    version='0.1.00',
    description='Biu, just like that',
    long_description=readme,
    packages=find_packages(include=['biu']),
    url='https://github.com/firslov/biu',
    author='firslov',
    author_email='345989060@qq.com',
    license='GPLv3+',
    keywords='quick commands',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'],
    install_requires=[],
    entry_points={'console_scripts': [
        'biu=biu.biu:main',
    ]}
)

