import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="visco2", # 設定する名前
    version="0.0.1", # バージョン設定
    author="marina kanno", # 名前
    author_email="marinasvtmax@gmail.com", # メアド変更
    description='Visualization of co2 emissions from 1990 to 2018 for each country', # 説明文書書き換え
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Marinakanno/vis_co2", # GitHubURL
    project_urls={
        "Bug Tracker": "https://github.com/Marinakanno/vis_co2", #GitHubURL
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['visco2'], # 設定するモジュール名
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'visco2 = visco2:main' # srcの中にある.pyの手前の文字
        ]
    },
)