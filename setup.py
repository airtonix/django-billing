from setuptools import setup, find_packages
import billing as app
setup(
    name='django-billing',
    version=app.__version__,
    author='Gabriel Grant',
    packages=find_packages(),
    namespace_packages=['billing', 'billing.processor'],
    license='AGPL',
    long_description=open('README').read(),
    install_requires=[
        'django-annoying',
        'django-model-utils',
        'South',
        'django-jsonfield',
        'ordereddict',
    ],
)
