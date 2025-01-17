from setuptools import setup, find_packages

setup(
    name='crispy-forms-bootstrap2',
    version='0.1',
    packages=find_packages(),
    url='',
    license='MIT',
    author='',
    author_email='',
    description='Django-crispy-forms bootstrap2 templates',
    install_requires=['django-crispy-forms >= 1.8'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=False
)
