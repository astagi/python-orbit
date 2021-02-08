from setuptools import setup, find_packages

setup(
    name='orbit',
    version='0.0.1',
    url='',
    install_requires=["requests==2.23.0"],
    description="Orbit API Python wrapper",
    long_description=open('README.rst', 'r').read(),
    license="MIT",
    author="Andrea Stagi",
    author_email="stagi.andrea@gmail.com",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
