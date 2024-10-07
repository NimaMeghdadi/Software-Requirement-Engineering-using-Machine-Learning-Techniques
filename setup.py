from setuptools import setup, find_packages
import os

# Read the contents of requirements.txt
def parse_requirements(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line and not line.startswith("#")]

setup(
    name="bert_classification",
    version="0.1.0",
    author="Nima Meghdadi",
    author_email="meghdadi.nima@gmail.com",  # Update with your email
    description="A text classification project using a BERT model",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NimaMeghdadi/Software-Requirement-Engineering-using-Machine-Learning-Techniques",  # Link to your project repository
    packages=find_packages(),
    install_requires=parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12.7',
)
