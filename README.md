# Context
This is intended to be a short-lived repo that facilitates learning and 
colloboration on how to use KatharaFramework, another opensource project.

## Technical stuff
We're using miniforge to provide the python environment, python 3.13 (also tested with 3.11), and Ubuntu 22.04 LTS.

<https://docs.anaconda.com/miniconda/install/#quick-command-line-install>
A useful minimalist set of instructions to use conda (which miniforge provides) is: 
<https://docs.anaconda.com/miniconda/other-resources/>

```
conda env list
conda create --name kathara-framework
conda activate kathara-framework
conda install python
```

Optional package: `rich` for pretty-printing the output:
```
conda install rich
```

Installing the two python packages:
```
python3 -m pip install git+https://github.com/saghul/pyuv@master#egg=pyuv
python3 -m pip install kathara
```

The code from the [getting started example](https://github.com/KatharaFramework/Kathara-Labs/tree/main/tutorials/python-api/getting-started) on the kathara website is the basis for the `getting_started.pt` file in this repo.

```
vim getting-started.py
python getting-started.py
```


