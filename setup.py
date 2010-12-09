from setuptools import setup, find_packages
import os

version = '0.4'

setup(name='isaw.theme',
      version=version,
      description="An installable theme for Plone 4",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme',
      author='Six Feet Up, Inc.',
      author_email='info@sixfeetup.com',
      url='http://www.sixfeetup.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['isaw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'sixfeetup.utils',
          'collective.addthis',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

