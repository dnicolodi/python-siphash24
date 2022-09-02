from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="siphash24",
            sources=[
                "siphash24.pyx",
                "c-siphash.c"],
        )
    ])
