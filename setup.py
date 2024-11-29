import setuptools
#
# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="runner-cli-pkg-jsonpoindexter",
    version="0.0.1",
    author="Jason Poindexter",
    author_email="poindexter.json@gmail.com",
    description="Run package scripts",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="https://github.com/jsonpoindexter/uSerialSync",
    # packages=setuptools.find_packages(),
    packages=['runner_cli'],
    scripts=['bin/runner_cli'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Operating System :: Microsoft :: Windows :: Windows NT/2000',
    ],
    entry_points={'console_scripts': [
        'runner-cli = runner_cli:main [runner_cli]',
    ]},
    python_requires='>=3.6',
)
