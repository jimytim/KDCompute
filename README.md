# KDCompute

A simple app with a GUI designed to help managing statistics in FPS video games.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need to set a python environnement with the specifications defined in the provided requirement file. One way of doing this is to use the open source package & environnement management system [Conda](https://docs.conda.io/en/latest/). The fastest way to obtain conda is to install Miniconda, a mini version of Anaconda that includes only conda and its dependencies. You will find the latest version [here](https://docs.conda.io/en/latest/miniconda.html) and the installation instructions [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). You need the python 3 version.

### Installing

Once conda is set up. Run the following commands

```
git clone https://github.com/jimytim/KDCompute.git
cd KDCompute
conda env create -f environment.yml
python scripts/main.py
```