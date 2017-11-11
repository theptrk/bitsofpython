# bits of python (3)

Install homebrew: [https://brew.sh/]

Install Python3:
```brew install python3```

Install virtualenv:
```brew install virtualenv```

Create a virtualenv called "env"
```
virtualenv -p `which python3`
```

Activate your new environment
```source ./env/bin/activate```

Install from a dependency file
```pip install -r foo.txt```

If needed, add your current directory to your python search path in
```.bash_profile```
```export PYTHONPATH=.:$PYTHONPATH```
