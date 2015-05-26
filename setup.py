from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(name='pythonjamaica.profile',
      version=version,
      description="PythonJamaica Profile for Exam Platform",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://pythonjam.org.jm',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pythonjamaica'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.cover',
          'collective.workspace',
          'tutorate.contenttypes',
          'wildcard.foldercontents',
          'Products.PloneFormGen',
          # -*- Extra requirements: -*-
      ],
      extras_require={
        'test': [
             'plone.app.robotframework',
         ],
       },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      #setup_requires=["PasteScript"],
      #paster_plugins=["ZopeSkel"],
      )
