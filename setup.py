import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="insightface-extractor",
    version="0.0.1",
    description="Face identity extraction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dniku/insightface",
    packages=setuptools.find_packages(),
    package_data={'insightface': ['mtcnn-model/*']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
