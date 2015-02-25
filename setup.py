from setuptools import setup

tests_require = ['tox', 'pytest']

setup(name='accesslog',
      version='0.1',
      description='tool which de-duplicates files in a filesystem by checksum.',
      url='http://github.com/andrewguy9/accesslog',
      author='andrew thomson',
      author_email='athomsonguy@gmail.com',
      license='MIT',
      packages=['accesslog'],
      install_requires = [],
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points = {
        'console_scripts': [
            'log2dict = accesslog.ui:main'
          ],
      },
      zip_safe=False)
