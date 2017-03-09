from setuptools import setup

setup(name='wec_athena',
      version='0.1',
      description='Testing first package',
      url='https://github.com/moone009/wec_athena',
      author='Christopher Mooney',
      author_email='mooneychristopher1@gmail.com',
      license='MIT',
      packages=['wec_athena','wec_athena.process','wec_athena.upload'],
      package_dir={'wec_athena': ''},
      zip_safe=False)