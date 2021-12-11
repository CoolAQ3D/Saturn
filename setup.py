from setuptools import setup, find_packages

setup(
  name="Saturn",
  version="1.0.0",
  py_modules="cli",
  packages=find_packages(),
  install_requires=[
    'click',
    'rich',
  ],
  entry_points='''
  [console_scripts]
  tb=cli:cli_commands
  '''
)