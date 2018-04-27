setup(name='pypinindia',
      description='Indian Pincodes and related Information',
      long_description=long_description,
      version='0.1.0',
      url='https://github.com/rajacsp/pypinindia',
      author='Raja CSP Raman',
      author_email='raja.csp@gmail.com',
      license='Apache2',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3'
      ],
      packages=['pypinindia'],
      install_requires=[          
          'pypandoc=>1.4'
      ],
      entry_points={
          'console_scripts': [
              'encrypt=pypinindia.main:run'
          ]
      }
)