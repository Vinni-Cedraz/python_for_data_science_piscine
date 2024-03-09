from setuptools import setup, find_packages


setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    url="https://github.com/Vinni-Cedraz/python_for_data_science_piscine",
    author="Vinni-Cedraz",
    author_email="planetexpress0101@gmail.com",
    license="MIT",
    packages=find_packages(),  # Finds your 'ft_package' directory
    classifiers=[
        # See https://pypi.org/classifiers for a full list
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
