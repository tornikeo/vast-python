from setuptools import setup, find_packages

setup(
    name='vast',
    version='0.1.0',
    install_requires=[
        'requests>=2.0.0'
    ],
    url='https://github.com/vast-ai/vast-python',
    license='MIT',
    author='tornikeo',
    author_email='tornikeonoprishvili@gmail.com',
    description='Vast.ai commandline access',
    packages=find_packages(),
    entry_points={
      'console_scripts': [
          'vast=vast:main',
          ]
      }
)