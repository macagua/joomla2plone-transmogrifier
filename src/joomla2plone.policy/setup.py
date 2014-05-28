from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='joomla2plone.policy',
      version=version,
      description="A policy package to manage a Plone installation",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Other Scripting Engines",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='policy joomla migration zope plone',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/macagua/joomla2plone.policy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['joomla2plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Products.CMFPlacefulWorkflow',
          'joomla2plone.migration',
#          'transmogrify.joomla2nitf',
#          'collective.nitf',
#          'collective.upload==1.0b2',
#          'collective.upload==1.0b5',
#          'collective.polls==1.0.1',
#          'collective.polls==1.4',
#          'collective.flowplayer',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
