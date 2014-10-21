# -*- coding: utf-8 -*-
"""Installer for the ploneintranet.attachments package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('docs', 'CHANGELOG.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='ploneintranet.attachments',
    version='0.1',
    description="Attachment storage for the Plone intranet suite",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='attachment,upload,storage',
    author='Plone Intranet Consortium',
    author_email='',
    url='http://pypi.python.org/pypi/ploneintranet.attachments',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['ploneintranet'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.grok',
        'five.pt',
        'Pillow',
        'Plone',
        'plone.api',
        'setuptools',
        'z3c.jbot',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing',
            'plone.app.discussion',
            'slc.underflow',
            'unittest2',
        ],
        'develop': [
            'coverage',
            'flake8',
            'jarn.mkrelease',
            'niteoweb.loginas',
            'plone.app.debugtoolbar',
            'plone.reload',
            'Products.Clouseau',
            'Products.DocFinderTab',
            'Products.PDBDebugMode',
            'Products.PrintingMailHost',
            'Sphinx',
            'zest.releaser',
            'zptlint',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
