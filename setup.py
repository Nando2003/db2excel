from setuptools import setup, find_packages

def parse_requirements(filename:str) -> list:
    """Reads the requirements.txt file and returns a list of packages."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

setup(
    name='db2excel',
    version='0.2.5',
    packages=find_packages(where='lib'),
    package_dir={'' : 'lib'},
    include_package_data=True,
    license='unlincense',
    description='Extracts data from a db and stores it in sheets in Excel',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Nando2003/db2excel.git',
    install_requires=parse_requirements('requirements.txt'),
    author='Fernando Fontes',
    author_email='nandofontes30@gmail.com',
    entry_points={
        'console_scripts': [
            'db2excel=cli:main',
        ],
    },
)