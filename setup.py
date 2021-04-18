from setuptools import setup, find_packages

with open('requirements.txt', 'r') as file:
    installRequires = file.read().split('\n')
    installRequires = [x for x in installRequires if x != '']

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name='wbo',
    version='0.0.1',
    description='Download and plot worldwide box office data!',
    packages=find_packages(),
    include_package_data=True,
    install_requires=installRequires,
    entry_points='''
        [console_scripts]
        wbo=wbo.cli:cli
    ''',
    py_modules=['cli','main'],
    package_dir={'wbo': ''},
    long_description=long_description,
    long_descriptionn_content_type="text/markdown",
)
