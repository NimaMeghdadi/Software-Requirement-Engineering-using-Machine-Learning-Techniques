from setuptools import setup, find_packages

setup(
    name="bert_classification",
    version="0.1.0",
    author="Nima Meghdadi",
    author_email="nima@example.com",  # Update with your email
    description="A text classification project using a BERT model",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nima/bert_classification",  # Link to your project repository
    packages=find_packages(),
    install_requires=[
        # "transformers>=4.0.0",  # For BERT model
        # "torch>=1.7.0",  # PyTorch for training the model
        # "scikit-learn>=0.24.0",  # For evaluation metrics
        # "pandas>=1.1.0",  # Data manipulation
        # "numpy>=1.19.0",  # For numerical computations
        # "tqdm>=4.41.1",  # Progress bar during training
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
