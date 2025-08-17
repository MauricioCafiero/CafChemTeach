# Running FairChem UMA MLIP on RACC2

## Load anaconda and create an environment
First ensure you have enough disk space. You can check with the du command and your user-id:
```
[user-id@racc2]$ du -h /home/users/user-id
```
at the end of the scrolling output it will list your used memory. You have 10GB by default. <br>
Now load anaconda:
```
[user-id@racc2]$ module load anaconda
```
You should now get (base) at the begining of your command line:
```
(base)[user-id@racc2]$
```
Now you can create the new environment (called uma-env):
```
conda create -n uma-env python=3.12
```
It will take a few minutes, and at one point you will have to answer yes:
```
Proceed ([y]/n)?
```
Once you have create the environment, enter is with the following command:
```
(base)[user-id@racc2]$ source activate uma-env
```
your command line will the change to reflect the environment:
```
(uma-env)[user-id@racc2]$
```

## Install packages
You will need to install Fairchem and RDKit
```
(uma-env)[user-id@racc2]$ pip install fairchem-core
```
this make take a while! After it is done:
```
(uma-env)[user-id@racc2]$ pip install rdkit
```
Again, this may take a while!

### Set-up your Huggingface token
You can save your huggingface token to your account by running the following:
```
(uma-env)[user-id@racc2]$ hf auth login
```


