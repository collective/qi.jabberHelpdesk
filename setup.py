from setuptools import setup, find_packages
import os

version = '0.40'

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
      download_url = 'http://pypi.python.org/pypi/qi.jabberHelpdesk/',
      license='GPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['qi'],
      include_package_data=True,
      platforms = 'Any',
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
