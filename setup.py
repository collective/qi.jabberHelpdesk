from setuptools import setup, find_packages
from os.path import join

version = '0.22'
readme = open('README.txt').read()
history = open(join('docs', 'HISTORY.txt')).read()

setup(name='qi.jabberHelpdesk',
      version=version,
      description="An online helpdesk product for plone",
      long_description=readme[readme.find('\n\n'):] + '\n' + history,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
      'Environment :: Web Environment',
      'Framework :: Plone',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Software Development :: Libraries :: Python Modules',      
        ],
      keywords='plone jabber helpdesk',
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
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
