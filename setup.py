from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="beepy",
    version="1.0.9",
    description="Play notification sounds.",
    long_description=readme(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    keywords="beep notification sound beepr beeper",
    url="https://github.com/prabeshdhakal/beepy/",
    author="Prabesh Dhakal",
    license="MIT",
    packages=["beepy"],
    package_data={"beepy": ["audio_data/*.wav"]},
    python_requires=">=3.0",
    install_requires=["simpleaudio"],
    include_package_data=True,
    zip_safe=False,
)
