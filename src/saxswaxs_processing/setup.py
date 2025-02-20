from setuptools import setup, find_packages

setup(
    name="saxswaxs_processing",  # Package name
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "saxswaxs-processing = saxswaxs_processing.main:main",  # This makes it executable from terminal
        ],
    },
    install_requires=[
        "pandas",     # List your dependencies here (e.g., pandas, numpy, etc.)
        "tkinter",    # If tkinter is a dependency
    ],
    python_requires=">=3.6",    # Specify the minimum Python version
)
