from setuptools import setup
setup(
    name="hooks",
    py_modules=["walrus_ast",],
    entry_points={
        'console_scripts': [
            "walrus-ast=walrus_ast:main",
        ],
    },
)