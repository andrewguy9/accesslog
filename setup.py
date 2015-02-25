from setuptools import setup

tests_require = []

setup(name='accesslog',
      version='0.2',
      description='Tool which helps parse access logs into useful blobs.',
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
