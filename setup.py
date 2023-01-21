from setuptools import setup

setup(
    name='chatgpt',
    version='0.1.0',
    py_modules=['chatgpt'],
    install_requires=[
        'Click',
        'Openai'
    ],
    entry_points={
        'console_scripts': [
            'chatgpt = chatgpt:cli',
        ],
    },
)