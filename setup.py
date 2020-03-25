from setuptools import setup, find_packages
from locking.requirements_parser import parse
import locking

from os import path

base_dir = path.dirname(path.abspath(__file__))

# Lists of requirements and dependency links which are needed during runtime, testing and setup
install_requires = []
tests_require = []
dependency_links = []

# Inject requirements from requirements.txt into setup.py
requirements, links = parse(path.join(base_dir, 'requirements', 'requirements.txt'),
                            links=True)
install_requires.extend(requirements)
dependency_links.extend(links)

# Inject test requirements from requirements_test.txt into setup.py
requirements, links = parse(path.join(base_dir, 'requirements', 'requirements_test.txt'),
                            links=True)
tests_require.extend(requirements)
dependency_links.extend(links)

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
    extras_require={'celery':  ["celery"] },
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
