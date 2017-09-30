# how to set up your python environment

the debate between python 2 vs python 3 is over. python 3 is the present and
future and you should download python 3 to you system

this should get you the latest python
```
brew install python
```

by default, using pythons' package installer `pip` will install packages to
your systems package directory. this will cause a ton of problems once you need
to depend on different versions of the same package among all your new
projects. the best way to handle this is to create new environments for each
new project. `virtualenv` is the tool to do this

```
python3 install virtualenv
```

now that you have a global `virtualenv` command, `cd` into your new project
directory.

```
virtualenv env `which python`
```

now you have create a directory called env that will help designate your
preferred python version and will store all your newly installed directories

activate your virtualenv
```
source ./env/bin/activate
```

pip install to your hearts desire
```
pip install numpy
pip install pandas
```

when you want to save the naem and versions of your current packages
```
pip freeze > requirements.txt
```
