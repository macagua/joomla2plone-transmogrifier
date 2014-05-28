from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='joomla2plone.migration',
      version=version,
      description="Migrate from Joomla to Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Other Scripting Engines",
        "Programming Language :: Python",
        "Programming Language :: SQL",
        "Topic :: Database",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone joomla data migration',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/macagua/joomla2plone.migration',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['joomla2plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.transmogrifier',
          'transmogrify.sqlalchemy',
          'plone.app.transmogrifier',
#          'transmogrify.nitf',
          'transmogrify.dexterity',
          'transmogrify.filesystem',
          'transmogrify.print',
          'collective.blueprint.pdb',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
