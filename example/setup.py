from setuptools import setup
setup(
    name="hooks",
    py_modules=["example",],
    entry_points={
        'console_scripts': [
            "example=example:main",
        ],
    },
)