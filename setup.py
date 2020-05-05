from setuptools import find_packages, setup
import text2img

install_requires = (["Django >= 1.11", "Pillow >= 5.0"],)

setup(
    name="django-text2img",
    author="Chainnews",
    author_email="hi@chainnews.com",
    version=text2img.__version__,
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    keywords=["django", "news2img", "pillow"]
)


