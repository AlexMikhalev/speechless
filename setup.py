from distutils.core import setup

with open("requirements.txt") as reqs_file:
    reqs = reqs_file.readlines()

setup(
    name='speechless',
    version='0.1.1',
    packages=['speechless'],
    url='https://github.com/JuliusKunze/speechless',
    license='MIT License',
    author='Julius Kunze',
    author_email='juliuskunze@gmail.com',
    description='',
    install_requires=[str(r.req) for r in reqs]
)
