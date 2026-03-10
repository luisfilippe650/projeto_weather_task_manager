from setuptools import setup, find_packages

setup(
    name="weather-cli",
    version="1.0",

    packages=find_packages(include=["app", "app.*"]),

    install_requires=[
        "requests"
    ],

    entry_points={
        "console_scripts": [
            "weather=app.main:main"
        ]
    },

    author="Luis Filippe",
    description="CLI para consultar clima e gerenciar cidades",
)