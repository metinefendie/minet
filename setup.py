from setuptools import setup, find_packages

with open('./README.md', 'r') as f:
    long_description = f.read()

# Version
# Info: https://packaging.python.org/guides/single-sourcing-package-version/
# Example: https://github.com/pypa/warehouse/blob/64ca42e42d5613c8339b3ec5e1cb7765c6b23083/warehouse/__about__.py
meta_package = {}
with open('./minet/__version__.py') as f:
  exec(f.read(), meta_package)


setup(name='minet',
      version=meta_package['__version__'],
      description='A webmining CLI tool & library for python.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/medialab/minet',
      license='MIT',
      author='Jules Farjas, Guillaume Plique',
      keywords='webmining',
      python_requires='>=3',
      packages=find_packages(exclude=['ftest', 'scripts', 'test']),
      install_requires=[
        'beautifulsoup4>=4.7.1',
        'browser-cookie3==0.7.6',
        'casanova==0.5.0',
        'cchardet==2.1.4',
        'cython>=0.29.4',
        'dateparser>=0.7.1',
        'json5>=0.8.5',
        'keyring<19.3',
        'lxml>=4.3.0',
        'ndjson>=0.3.1',
        'numpy>=1.16.1',
        'persist-queue>=0.4.2',
        'pytz>=2019.3',
        'pyyaml',
        'quenouille>=0.6.0',
        'tqdm>=4.31.1',
        'ural>=0.22.1',
        'urllib3[secure]>=1.25.3'
      ],
      entry_points={
        'console_scripts': ['minet=minet.cli.__main__:main']
      },
      zip_safe=True)
