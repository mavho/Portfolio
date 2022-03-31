from setuptools import setup

setup(
    name='portfolio',
    packages=['server'],
    include_package_data=True,
    install_requires=[
        'flask'
    ]
)