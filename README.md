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

Currently two instances of routers are configured with `bird` for routing using static routes over logical network `C` between the `pc` instances in logical network `A` and a `webserver` in logical network `B`. the bird configurations are configured and started as part of the `getting-started.py` script. Run `birdc show route` on each instance of the router to check.

## Troubleshooting
If/when the python script crashes or fails to complete, various orphaned resources remain in kathara's microcosm locally. These can be removed using the following command: `kathara wipe` and then enter `y` when asked `[y/n]`.

## Interactive testing
First start bird on both router instances. Then you can run `wget 100.1.3.90` from any running instance on the kathara network to request the default web page from the `webserver`. Running this command should download a copy of `index.html` from the `webserver` to the local folder on the machine you're currently connected to.

There are lots of networking-related commands available to check routing, etc. Some examples will be added shortly.

