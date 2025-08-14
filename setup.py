from setuptools import setup, find_packages

setup(
    name="vi",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "datetime",
        "asyncio",
        "fake_useragent",
        "websockets",
        "requests",
        "requests_toolbelt",
        "filetype",
        "Pillow",
        "typing"
    ],
)
