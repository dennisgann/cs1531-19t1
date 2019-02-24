# Git Basics

We hope you all have watched the Git videos outlined in your lab specification. Let us test how much you know about Git.

Which one of these statements about Git is not true? Git allows you to:
 - a. Git allows you to keep track of all files in a project
 - b. Git allows you to record any changes to project files
 - c. Git allows your to restore previous versions of files
 - **d. Git and GitHub are the same thing**
 - e. Merge code from different team members

Who is attributed with inventing Git?
 - a. Junio C. Hamano
 - b. James Gosling
 - **c. Linus Torvalds**

Katherine, decides to use Git for her version control. Enter the appropriate Git operation for each of the following tasks that she wants to perform:

1. Git generally comes pre-installed with Linux. Katherine can find out if Git is installed on her system by typing **git --version.**

2. As Katherine is using Git for the first time on her system, she must configure her username and email address on Git by typing: **git config --global user.name "My Name Here"
git config --global user.email "myemail@example.com"**

3. initialise a new Git repository **git init**

4. After initialising a new Git repository, if you run ls -a, what is the name of the folder created in the current project directory? **.git**

5. Now, Katherine creates a file readme.txt and adds the line initial edit to the file. She saves and closes the file. Git isn’t aware of this file yet. To track this file she must type: **git add [file]**

6. Next, Katherine can commit the changes with a meaningful message. To do that, she must run the command: **git commit -m "My message here"**

7. To check the history of commits by typing: **git log**

8. Katherine wants to add a new feature but does not want to mess up the old features. She decide to create a new branch, to make her changes. To create a branch called feature1 , she must type: **git branch feature1**

9. To check out to the new branch, type: **git checkout [new-branch-name]**

10. Alternatively, Katherine can also create a new branch and check out to this new branch by typing a single command: **git checkout -b [new-branch-name]**

11. Katherine now makes some changes to her file, adding a comment like “A change exclusive to this branch only”. Git isn’t aware of this changes yet, to stage and commit the changes, she must type: **git commit -am "Message"**

The above exercises demonstrate the use of version-control tool Git. In the labs, you will learn how to setup a remote repository on your Github account and push the changes from your local Git repository to the remote GitHub Repository and also pull changes from the remote repository into your local repo.