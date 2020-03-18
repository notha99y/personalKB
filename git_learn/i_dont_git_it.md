# I dont git it

## Cloning a project with submodule
1. Clone the main repo. By default, you will get the directories that contain submodules, but none of the files within them yet.
1. Run `git submodule init` to initialize your local configuration file and `git submodule update` to fetech all the data from that project.


## Managing Multiple GitHub Accounts
[more info](https://mherman.org/blog/managing-multiple-github-accounts/) <br>
Essentially, it a matter of balancing both your git and ssh configuratins. 

### SSH Keys
Let's assume you have two github accounts `githubWork` `githubPersonal`. 
1. Create two SSH keys, saving each to a seperate file:
```bash
cd ~/.shh
ssh-keygen -t rsa -C "githubPersonal@example.com"
# when prompted, name the file that saves the key
ssh-keygen -t rsa -C "githubWork@example.com"
# same here
``` 
1. Add the keys to your Github accounts
```bash
pbcopy < ~/.ssh/id_rsa_personal.pub
``` 
to install `pbcopy` follow [this](https://garywoodfine.com/use-pbcopy-on-ubuntu/) <br>
1. Create a config gile to manage the sperate key
```bash
cd ~/.ssh
touch config
```
edit the file as such
```
# githubPersonal
Host personal
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa_personal

# githubWork
Host work
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa_work
```

1. Update stored identities

clear current stored identities
```bash
ssh-add -D
```
add new keys
```bash
ssh-add id_rsa_personal
ssh-add id_rsa_work
```
test to make sure keys are stored
```bash
ssh-add -l
```
test to make sure Github recognizes the keys
```bash
ssh -T personal
```
