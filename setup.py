from setuptools import setup, find_packages

setup(name='my_friend',
      version='0.1',
      description="Python library to make my days better",
      long_description='just 4 lulz',
      classifiers=[],
      keywords='',
      author='Daniel Kanzel',
      author_email='danersow@gmail.com',
      url='',
      license='FUCK', # or any license you think is relevant
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          # add here any tool that you need to install via pip 
          # to have this package working
          'setuptools',
          'todoist-python',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      todo = my_friend.src.hooks.todo:main
      tasks = my_friend.src.hooks.tasks:main
      """,
)