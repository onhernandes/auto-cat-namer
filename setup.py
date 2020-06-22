from setuptools import find_packages, setup

setup(
    name="auto_cat_namer",
    version="1.0",
    description="Automagically writes names to some images",
    author="Hernandes",
    packages=find_packages(),
    install_requires=["opencv-contrib-python"],  # external packages as dependencies
    entry_points={"console_scripts": ["auto-cat-namer = auto_cat_namer.__main__:main"]},
)
