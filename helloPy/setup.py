from setuptools import setup

setup(
    name="hello",
    version="0.0.1",
    description="Meu pacote hello",
    author="Fabio Marturano",
    author_email="fabiocmjor@gmail.com",
    packages=["hello"],
    # caso o pacote não estaja instalado ele sujere a instalação no diretorio do ambiente do projeto
    # install_requires=["numpy"]
)
