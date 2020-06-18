from os import path

from setuptools import setup, find_packages

import locking

base_dir = path.dirname(path.abspath(__file__))

# Lists of requirements and dependency links which are needed during runtime, testing and setup
install_requires = ['Django<2.2']
tests_require = [
    'celery',
    # freeze time
    'freezegun',
    # pytest
    'pytest',
    'pytest-django',
    # coverage
    'pytest-cov'
    'coverage'
    'coveralls'
    # flake8
    'flake8'
    'pep8'
    'pyflakes'
    'mccabe'
    'pep8-naming'
    'flake8-print'
    'flake8-debugger'
]
dependency_links = []

setup(
    name="django-db-locking",
    version=locking.__version__,
    url='https://github.com/vikingco/django-db-locking/',
    license='BSD',
    description='Database locking',
    long_description=open('README.rst', 'r').read(),
    author='VikingCo',
    author_email='operations@unleashed.be',
    packages=find_packages('.'),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={'celery': ["celery"]},
    tests_require=tests_require,
    dependency_links=dependency_links,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
