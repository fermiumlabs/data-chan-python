from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='data_chan',
      version='0.1.13',
      description='Python bindings for Data-Chan',
      long_description=readme(),
      url='https://github.com/fermiumlabs/data-chan-python/',
      author='Fermium LABS',
      author_email='info@fermiumlabs.com',
      license='Apache 2',
      packages=['data_chan'],
      zip_safe=False,
      include_package_data=True,
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',

          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: Apache Software License',

          'Programming Language :: Python :: 3',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS',
          'Operating System :: POSIX :: Linux',
          'Operating System :: Unix'
      ]
      )