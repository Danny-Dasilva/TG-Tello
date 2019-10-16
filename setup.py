import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TG_Tello",
    version="0.0.1",
    author="Danny Dasilva",
    author_email="dannydasilva.solutions@gmail.com",
    description="Tello Python Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Danny-Dasilva/TG_Tello",
    install_requires=[
        "pygame",
        "av",
        "opencv-python",
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: Linux",
    ],
)