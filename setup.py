from setuptools import setup

def parse_requirements(filename:str) -> list:
    """Reads the requirements.txt file and returns a list of packages."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

setup(
    name='db2excel',
    version='0.1.1',
    packages=['db2excel'],
    license='unlincense',
    description='Extracts data from a db and stores it in sheets in Excel',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Nando2003/db2excel.git',
    install_requires=parse_requirements('requirements.txt'),
    author='Fernando Fontes',
    author_email='nandofontes30@gmail.com'
)