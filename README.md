# Pypi-Package-Setup
> TODO: add images, fill out 'useful resources' and 'get in touch'

Structure, base code, and instructions for setting up your own pypi package!

### **Table of Contents**
[1. About this Template](#about-this-template)
<br>
[2. Get Started](#get-started)
<br>
[3. Walkthrough](#walkthrough)
<br>
[4. Deploying your Package](#deploying-your-package)
<br>
[5. Useful Resources](#useful-resources)
<br>
[6. Get In Touch](#get-in-touch)

<br>

## **About This Template**
Setting up a `pypi package` can very easily, and _very quickly_, become frustrating--whether it be because of confusing articles, or conflicting Stack Overflow 'correct' answers. All this does is take time away from what you **actually** want to be doing... coding!
<br><br>
So, this template repo is here to lay out all the structural features of your package and give clear stubs for where _your_ code will go! Let's get started.

<br>

## **Get Started**
Getting started is as simple as the following three steps:
1. Click `Use this template` <br>

2. Select `Create a new repository` so you can have an exact copy of this repository<br>

3. Clone your repository to your preffered IDE. If this is new to you, check out [this guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) by GitHub.

With those three steps done, you should now have a copy of this template on your local computer!

<br>

## **Walkthrough**
While it is tempting to get right into the coding aspect, it is definitely useful to first understand what the different files are for, and what to do with them. If you are already familiar with this, skip to [Deploying your Package](#deploying-your-package). Otherwise, let's break it down!


### **Project Structure**
If all went well with cloning, your project structure should look like this:
```
|── .github
|   |── workflows
|   |   |── python-publish.yml
|
|── package-name
|   |── __init__.py
|   |── module_one.py
|   |── module_two.py

|── .gitignore
|── LICENSE
|── pyproject.toml
|── README.md
|── setup.cfg
```


### **What Everything Does**
And, here's what all the different files and directories are for:
| Directory/File     | Purpose                                                                                                                                                                                                                                                                                            |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .github            | This is the folder that houses **everything GitHub-related** in your project. E.g. workflows, issues and pull request templates, etc                                                                                                                                                                   |
| workflows          | Have you ever seen the **Actions** tab on GitHub and wondered what it's for? Well, what it does is run any workflows you have setup for your code. A workflow is "a configurable automated process that will run one or more jobs" - GitHub.                                                       |
| python-publish.yml | This is our workflow file that, whenever you make a new release on GitHub, will **trigger the release/upgrade of your package** on pypi!                                                                                                                                                               |
| package-name       | This is the folder that will hold all the actual code related to your project. Name it what you want your package to be named.                                                                                                                                                                     |
| __init__.py        | This file is essentially just **initialization** code for our package. Here you want to write any imports (e.g. functions or classes) that you define in your modules and want users to be able to import for themselves.                                                                              |
| module_one.py      | A file to define **functionality** of your package. E.g. if your package is about web-scraping, you'd have a webscraper class, or functions, defined in this file.                                                                                                                                     |
| module_two.py      | Same purpose as module_one.py. You can have as many of these as you want!                                                                                                                                                                                                                          |
| .gitignore         | Files that you want GitHub to ignore when you push changes to your repository. For example, you should **always add your `.env` file to the .gitignore** so you don't accidentally share sensitive information! The .gitignore in this repo is the template one that GitHub provides for python files. |
| LICENSE            | The license for your package code--i.e. defining **what people are allowed to do** with your code. Read more [here]("https://choosealicense.com/)                                                                                                                                                      |
| README.md          | Currently, as you can tell, this file is full of instructions that I have provided for you. However, when you're actually going to publish your package, you want to **replace this file** with information about the package. Include things such as what it is, how to install/upgrade, FAQs, etc.   |
| setup.cfg          | This is the file that provides key information **(metadata)** about your package, such as: who made it, where is its source repo, what other pip requirements may be necessary for this code, what python version, etc.      |
| pyproject.toml     | You can think of this as the python **'Settings'** file that is detailing the tools required to build this project. This is typically just **setuptools** and **wheel**. |

<br>

### **Filling in the Blanks**
Alrighty, now it's time to **replace my boilerplate code** with your super awesome code. The files you absolutely want to be changing are:
- `setup.cfg`
- `__init__.py`
- `module_one.py`
- `module_two.py` -- feel free to delete this if you don't want/need multiple package files
- `package-name` -- change the name of this directory to the name of your package

Want an example? Check out the source code for [sreddit](https://github.com/Mandy-cyber/sreddit)--my subreddit scraper package.

<br>

## **Deploying your Package**
Okay, you've written your code, you've setup all your files... what next? Easy: it's time to **build and deploy your package**!

### Build
To build your package, make sure you are in the root folder then run the following commands, one-by-one, in your terminal:
```
# install/upgrade pip
python3 -m pip install -U pip

# install/upgrade setuptools
pip install -U setuptools

# install/upgrade build tool
python -m pip install --upgrade build

# build the project
python -m build
```
If you've followed all the steps above and ran those commands, you should now see: a `dist` folder created, a `package-name.egg-info` folder, and a success message in your terminal that looks like
```
Successfully built package-name-0.0.1.tar.gz and package-name-0.0.1-py3-none-any.whl
```


### Deploy
> [Test PyPi](https://test.pypi.org/) is "a separate instance of the Python Package Index that allows you to try distribution tools and processes without affecting the real index."

Now it's time to _deploy_ your package to PyPi... actually you may want to start by deploying to TestPyPi just to make sure things are actually working as expected. Here are your next steps:
1. Go to [Test PyPi](https://test.pypi.org/), create an account, and verify your email

2. Generate an API token [here](https://test.pypi.org/manage/account/token/) giving it any name and, for the sake of this tutorial, keeping the scope as **"Entire Account"**. Do not forget to _copy the token_ before exiting the page!

3. Install twine
```
python -m pip install --upgrade twine
```

4. Upload your package
```
# to upload to TestPyPi
python -m twine upload --repository testpypi dist/*

# to upload to actual PyPi
python -m twine upload dist/*
```
If all goes well, Twine will ask for your username and password. Your username will be `__token__` and your password the API token from Step 2 _(include the 'pypi-' prefix)_

5. After running the above commands, you'll be provided a link that, when clicked, will bring you to the package you just published!

6. Install and test your package by creating a virtual environment somewhere on your system, downloading your package, and checking if it works as expected!
   
7. In the future, to automate those final couple of steps, you can just 'Create a new release' in your Github repo and your workflow file should do all this for you! 


## **Useful Resources**



## **Get in Touch**
