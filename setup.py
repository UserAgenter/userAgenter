import os
from re import findall
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Readme
if os.path.isfile("README.md"):
    with open(("README.md"), encoding="utf-8") as readmeh:
        big_description = readmeh.read()
else:
    big_description = "Generated User Agent and Scrap Proxy [http, socka4, socka5](Auto update)"


setup(name="UserAgenter",
      version="1.3.1",
      description="Generated User Agent and Scrap Proxy [http, socka4, socka5](Auto update)",
      url="https://github.com/UserAgenter",
      author="Mmdrza",
      author_email="PyMmdrza@Gmail.com",
      license="MIT",
      install_requires=["requests"],
      packages=find_packages(),
      keywords=["user-agent", "fake-user-agent", "user agent generator", "free proxy", "proxy"],
      long_description=big_description,
      long_description_content_type="text/markdown",
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Education',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12'
      ],
      )