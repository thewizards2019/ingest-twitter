import setuptools

setuptools.setup(
    name="ingest-twitter",
    version="0.0.1",
    packages=setuptools.find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        'Flask',
        'tweepy',
        'python-twitter',
        'confluent_kafka',
    ],
    extras_require={
        'dev': [
            'pytest',
            'flake8',
            'pytest-cov',
            'bandit',
            'black',
        ]
    },
    entry_points={
        'console_scripts': [
            'app = app.cli:cli'
        ]
    },
)
