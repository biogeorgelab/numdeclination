from setuptools import setup, find_packages

setup(
    name = "numdeclination",
    version = "0.0.1.0",
    description = "Средство для склонения слов по числам",
    packages = find_packages(),
    package_data = {'cases': ['cases.py']},
    include_package_data = True
)