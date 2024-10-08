#!/usr/bin/env python
# -*- coding: utf-8 -*-

import versiontools_support
from setuptools import setup, find_packages

setup(
    name = 'taiga-contrib-google-sso',
    version = "1.1.0",
    description = "The Taiga plugin for google authentication",
    long_description = "",
    keywords = 'taiga, google, auth, plugin',
    author = 'Ahmed Faraz',
    author_email = 'ahmed.faraz0046@gmail.com',
    url = 'https://github.com/ahmed-faraz46/taiga-contrib-google-sso',
    license = 'AGPL',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[],
    setup_requires = [
        'versiontools >= 1.9',
    ],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
