'''
Build the aiml Py2/Py3 package
'''

from setuptools import setup
import io

with io.open('aiml/constants.py', encoding='utf-8') as fid:
    for line in fid:
        if line.startswith('VERSION'):
            VERSION = line.strip().split()[-1][1:-1]
            break

setup(name="aiml",
      version=VERSION,
      author="Douglas Blank",
      author_email="doug.blank@gmail.com",
      description="An interpreter package for AIML, the Artificial Intelligence Markup Language",
      long_description="""aiml implements an interpreter for AIML, the Artificial Intelligence
Markup Language developed by Dr. Richard Wallace of the A.L.I.C.E. Foundation.
It can be used to implement a conversational AI program.

Forked from:

* 0.9.1 https://github.com/paulovn/python-aiml
* 0.8.6 https://github.com/cdwfs/pyaiml

PyAIML (c) Cort Stratton
""",
      url="https://github.com/calysto/aiml",
      platforms=["any"],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          "Topic :: Communications :: Chat",
          "Topic :: Scientific/Engineering :: Artificial Intelligence"
      ],
      install_requires = ['setuptools'],
      packages=["aiml", 'aiml.script'],
      include_package_data = True,
      package_data={'aiml': [
          'botdata/standard/*.aiml',
          'botdata/standard/*.xml',
          'botdata/alice/*.aiml',
          'botdata/alice/*.xml',
      ]},
      entry_points = {'console_scripts': [
          'aiml-validate = aiml.script.aimlvalidate:main',
          'aiml-bot = aiml.script.bot:main',
      ]},
      test_suite = 'test.__main__.load_tests',
)
