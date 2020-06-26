# Common git commands
- ```git log```: show thes history of commits
```bash
git log --pretty=oneline --abbrev-commit -n 5 # prettify and show latest 5 logs
```

- ```git reflog```: shows the logs of the different references git is keeping track of
- ```git reset```: reset back the mistake after you commit
```bash
git reset --hard <commit hash> 
git reset --hard origin/master # go back to version in origin master
```
- ```git stash```: Stash the changes in a dirty working directory away
```bash
git stash list: list modifications stashed away
git stash show: inspect
git stash pop: remove a single stashed state from the stash list and apply it on top of the current working tree state
```
Commonly used:
- To ```git pull```
```bash
git stash
git pull
git pop
# locally you merge the incoming commits
```
## Delete a local Commit
[more info](https://ncona.com/2011/07/how-to-delete-a-commit-in-git-local-and-remote/)
```bash
git reset -hard HEAD~ #Delete the most recent commit
```
Using git rebase
```bash
git rebase -i HEAD~2 # 
```
HEAD is the commit currently checked out (wherever you are right now). HEAD~ is the same as HEAD~1, which means one commit before the current commit. HEAD~2, or HEAD~n, means n number of commits before the current commit.

# git submodules
## Add gitsubmodule
```bash
git submodule add [--name <name>] <repository> [<path>]
```
where
- `<name>` is the submodule's name that will appear in the `.gitmodules` file. if left unspecified, `<name>` simply defaults to `<path>`
- `<repository>` is the URL of the new submodule's repo
- `<path>` is the name of the subdirectory of the main repo
## Delete gitsubmodule
- Delete the relevant section from the `.gitmodules` file
- Stage the `.gitmodules` changes `git add .gitmodules`
- Delete the relevant section from `.git/config`
- Run `git rm --cached path_to_submodule (no trailing slash)`
- Run `rm -rf .git/modules/path_to_submodule (no trailing slash)`
- Commit `git commit -m "Removed submodule "`
- Delete the now untracked submodule files `rm -rf path_to_submodule`

## Cloning a project with submodule
1. Clone the main repo. By default, you will get the directories that contain submodules, but none of the files within them yet.
1. Run `git submodule init` to initialize your local configuration file and `git submodule update` to fetch all the data from that project.

Subsequently, you can just `git pull --recurse-submodules`

## Managing Multiple GitHub Accounts
[more info](https://mherman.org/blog/managing-multiple-github-accounts/) <br>
Essentially, it a matter of balancing both your git and ssh configuratins. 

### SSH Keys
Let's assume you have two github accounts `githubWork` `githubPersonal`. 
1. Create two SSH keys, saving each to a seperate file:
```bash
cd ~/.ssh
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
