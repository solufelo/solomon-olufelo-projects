from setuptools import setup, find_packages

setup(
    name="jobscanner",
    version="0.1.0",
    packages=find_packages(where="src", include=["jobscanner*"]),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "beautifulsoup4",
        "pandas",
        "pyyaml",
        "rich"
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-mock",
            "pytest-cov"
        ],
        "dev": [
            "black",
            "flake8",
            "mypy"
        ]
    },
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "jobscanner=jobscanner.main:main",
            "jobscanner-gui=jobscanner.gui.app_tkinter:main"
        ]
    }
) 