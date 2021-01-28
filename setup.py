import setuptools

setuptools.setup(
    name='youtube-creator-cli',
    version='0.0.0',
    author='Aarav Borthakur',
    author_email='gadhaguy13@gmail.com',
    description='The ultimate Youtube creator\'s CLI',
    long_description='Long desc.',
    long_description_content_type='text/markdown',
    url='https://github.com/gadhagod/Youtube-Creator-CLI',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'click',
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib'
    ],
    scripts=['./yt'],
    python_requires='>=3.6'
)