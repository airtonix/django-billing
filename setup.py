from setuptools import setup

setup(
    name='django-billing',
    version='0.1.5',
    author='Gabriel Grant',
    packages=[
        'billing',
        'billing.processor',
        'billing.processor.simple_account',
        'billing.templatetags',
        'billing.tests',
        'billing_management',
        'billing_management.management',
        'billing_management.management.commands',
    ],
    namespace_packages=['billing', 'billing.processor'],
    license='AGPL',
    long_description=open('README').read(),
    install_requires=[
        'git+git://github.com/airtonix/python-pricing.git',
        'django-annoying',
        'django-model-utils',
        'South',
        'django-jsonfield',
        'ordereddict',
    ],
    dependency_links = [
    	'http://github.com/airtonix/python-pricing/tarball/master#egg=python-pricing',
    ]
)
