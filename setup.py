import setuptools

with open('ReadMe.md', 'r') as f:
    long_description = f.read()
    
with open('requirements.txt', 'r', encoding='UTF-16') as f:
    required = f.readlines()


setuptools.setup(
    name="rmdirs",
    version="1.0.0",
    description="Util from removing all directories from the file structure while keeping all the files.",
    long_description=long_description,
    author="A-Bak",
    author_email="adam.bak753@gmail.com",
    packages=["rmdirs"],
    install_requires=required,
)