from setuptools import setup,find_packages
from pip.req import parse_requirements
#reqs = list(parse_requirements("requirements.txt",session=False))
#reqs = [str(ir.req) for ir in reqs]
#print(reqs)
setup(
    name="scholar",
    version="1.0",
    description="scholar",
    author="ckreibich=>proboscis",
    author_email="nameissoap@gmail.com",
    packages=find_packages(),
    install_requires=[beautifulsoup4],
    entry_points="""
    [console_scripts]
    scholar=scholar.scholar:main
    """
    )
