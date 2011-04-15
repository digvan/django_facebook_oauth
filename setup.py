# -*- encoding: utf-8 -*-
from setuptools import setup

setup(
    name='django-facebook-oauth',
    version='0.1',
    description="Facebook OAuth authentication for Django.",
    long_description=open('README.markdown').read(),
    author='Jeff Dickey',
    author_email='dickeytk@gmail.com',
    url='https://github.com/Anue/django_facebook_oauth',
    packages=['facebook'],
    package_dir={'facebook': 'facebook'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
