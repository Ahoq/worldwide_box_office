from setuptools import setup, find_packages

with open('requirements.txt', 'r') as file:
    installRequires = file.read().split('\n')
    installRequires = [x for x in installRequires if x != '']

setup(
    name='bom',
    version='0.001',
    packages=find_packages(),
    include_package_data=True,
    install_requires=installRequires,
    entry_points='''
        [console_scripts]
        bom=bom.cli:cli
    ''',
)
