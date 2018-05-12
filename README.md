# qlab
The lab repository for experiment and analysis codes
# To Start
## Setup git
You can easily setup Git in any operating system. Detailed instructions are available at <http://git-scm.com/downloads>

Getting started instructions: <http://git-scm.com/book/en/Getting-Started-Git-Basics>

An excellent interactive tutorial is available here: [Try Git](https://try.github.io/levels/1/challenges/1)

## Create a Github account
If you do not already have a Github account, create one for free. Just go to <https://github.com>

## Fork repository
Fork the public repository named "qlab" at: <https://github.com/Qlab-UDel/qlab>, just press the fork button (make sure you are currently logged into your own account).

As you fork this repo, this qlab repo will appear in your own github profile. 

## Watch the upstream repository <https://github.com/Qlab-UDel/qlab>.
You will get email notification when there are changes on the repo.

## Setting up your local clone in local terminal (you only need to do this once for the 'qlab' repo)
`cd` into your local directory where you would like to save the lab repo.

Type:
```
git clone https://github.com/YourGitHubAccount/qlab.git
```

Now you will have a local folder called qlab on the computer.

Then type:
```
cd ./qlab
git remote add upstream https://github.com/Qlab-UDel/qlab.git
git remote -v
git remote set-url --push upstream Oops.no.push.to.upstream
```
In the output you will see:
```
origin https://github.com/zhenghanQ/qlab.git (fetch)
origin https://github.com/zhenghanQ/qlab.git (push)
upstream https://github.com/Qlab-UDel/qlab.git (fetch)
upstream	Oops.no.push.to.upstream (push)
```
## Doing your work in a branch in local clone (every time you start working on sth)
1) Go to local clone's master, update local clone's master, update origin's master
```
git checkout master
git fetch upstream
git merge upstream/master
git push origin master
```
2a) If you want to continue working on a branch on a computer where you have set up the qlab folder:
```
git checkout your_working_branch
git fetch origin
git merge origin/your_working_branch
```
2b) If you want to continue working on a branch on a computer where you have NOT set up the qlab folder:
```
git clone https://github.com/YourGitHubAccount/qlab.git
git branch -a
git checkout origin/your_working_branch
git checkout your_working_branch
```
3) If you are starting to do something new, create a new branch in local clone: branch_name
```
git checkout -b branch_name
```
4) work on this branch: edit files, add files, create new folders etc. Make sure you **never rename or move** existing folders on your end.

5) commit changes to this branch
```
git add directories/files
git commit -m "your commit message"
```
See here for how to write a commit message: <https://chris.beams.io/posts/git-commit/>

5) push this branch to origin 
```
git push origin branch_name
```

6) In your forked repo on github, you will see an automatically generated message on the pull request page. Create pull request comparing Qlab-Udel/qlab master and YourGitHubAccount/qlab branch_name. 

7) Wait for Zhenghan to merge your changes to the qlab.Udel lab master. You will receive an email when this step is done.

### Note:
1. If you have any questions, ask them on our git_github slack channel. Please send the history of your command (type history in the command window) as well as the error messages.
2. Before you leave the work, make sure you do 
```
git add new_files
git commit 
git push origin branch_name
```
3. Once you have a working version of any script you have been working on, issue a pull request.
