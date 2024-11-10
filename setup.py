from setuptools import find_packages, setup

setup(
    name = "math_quiz",
    version = "1.0.0",
    description="A math quiz",
    packages = find_packages(),
    include_package_data = True,
    install_requires = [],
    entry_points = {
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',
        ],
    },
    license = 'MIT License',
    long_description = open('README.md').read(),
    author = 'Bibhu Prasad Bhanja',
    author_email = 'bibhupbhanja@gmail.com / bibhu.p.bhanja@fau.de',
    url = 'https://github.com/Bibhu-007/dsss_Homework_2.git', 
    )