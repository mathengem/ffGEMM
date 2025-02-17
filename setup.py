from setuptools import setup, find_packages

setup(
    name='ffGEMM',
    version='0.1.0', 
    packages=find_packages(),
    install_requires=[
        'gmpy2',  # Add gmpy2 as a dependency
        'safetensors',  # Add safetensors as a dependency
        # Add any other necessary dependencies here
    ],
)
