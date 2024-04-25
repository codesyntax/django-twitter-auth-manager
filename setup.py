# -*- coding: utf-8 -*-
# /usr/bin/env python

import uuid
from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

def get_requirements(source):
    try:
        install_reqs = parse_requirements(source, session=uuid.uuid1())
    except TypeError:
        # Older version of pip.
        install_reqs = parse_requirements(source)
    try:
        required = [str(ir.req) for ir in install_reqs]
    except:
        required = [str(ir.requirement) for ir in install_reqs]
    return list(required)

version = '1.0'

setup(name='django_twitter_auth_manager',
      version=version,
      description="""Manage Twitter OAuth 2.0 Authorization Code Flow with PKCE (User Context) authentication by an Django app and store necessary token and refresh token for future uses.""",
      long_description=open("README.md").read() + "\n" +
                       open("CHANGELOG.txt").read(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 4.0",
      ],
      keywords='',
      author="Urtzi Odriozola (CodeSyntax http://codesyntax.com)",
      author_email="uodriozola@codesyntax.com",
      url="https://github.com/codesyntax/django-twitter-auth-manager",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=get_requirements('requirements.txt'),
)
