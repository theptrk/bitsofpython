# bits of python (3)

## how to set up python on a dev environment

- [ ] Install homebrew: [https://brew.sh/]
- [ ] Install Python3: `$ brew install python3`
- [ ] Install virtualenv: `$ brew install virtualenv`
- [ ] Create a virtualenv called "env" `` virtualenv env -p `which python3` ``
- [ ] Activate your new environment `$ source ./env/bin/activate`
- [ ] Install from a dependency file `$ pip install -r foo.txt`
- [ ] (optional) If needed, add the python search path to your bash profile???
```
# TODO fact check this code block
# f: .bash_profile
export PYTHONPATH=.:$PYTHONPATH
```
