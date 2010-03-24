from setuptools import setup, find_packages
import os

version = '0.30'

setup(name='qi.jabberHelpdesk',
      version=version,
      description="An online helpdesk product for plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
      'Environment :: Web Environment',
      'Framework :: Plone',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Software Development :: Libraries :: Python Modules',      
        ],
      keywords='plone,jabber,helpdesk',
      author='G. Gozadinos',
      author_email='ggozad@qiweb.net',
      url='http://github.com/ggozad/qi.jabberHelpdesk',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['qi'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
