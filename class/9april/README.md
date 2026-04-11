# Basic Git Commands

This README provides a practical reference for common Git commands used in daily version control workflows. It covers setup, repository creation, staging, committing, branching, merging, remote work, and helpful tips.

## Table of Contents

1. [Git Setup](#git-setup)
2. [Creating a Repository](#creating-a-repository)
3. [Checking Status and Changes](#checking-status-and-changes)
4. [Staging and Committing](#staging-and-committing)
5. [Branching and Switching](#branching-and-switching)
6. [Merging Branches](#merging-branches)
7. [Working with Remotes](#working-with-remotes)
8. [Common Workflows](#common-workflows)
9. [Useful Tips](#useful-tips)

## Git Setup

Configure Git with your name and email once per machine:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Verify your configuration:

```bash
git config --list
```

## Creating a Repository

Initialize a new Git repository in the current directory:

```bash
git init
```

Clone an existing repository from a remote URL:

```bash
git clone https://github.com/user/repo.git
```

## Checking Status and Changes

See which files are new, modified, or staged:

```bash
git status
```

Review unstaged changes:

```bash
git diff
```

Review staged changes:

```bash
git diff --staged
```

## Staging and Committing

Add a specific file to the staging area:

```bash
git add filename
```

Stage all changes in the current directory:

```bash
git add .
```

Commit staged changes with a descriptive message:

```bash
git commit -m "Describe your changes clearly"
```

To amend the last commit message or include additional staged changes:

```bash
git commit --amend
```

## Branching and Switching

List local branches:

```bash
git branch
```

Create a new branch:

```bash
git branch feature-name
```

Switch to an existing branch:

```bash
git checkout feature-name
```

Create and switch to a new branch in one step:

```bash
git checkout -b feature-name
```

Newer Git versions also support:

```bash
git switch -c feature-name
```

## Merging Branches

Merge another branch into the current branch:

```bash
git merge feature-name
```

If merge conflicts occur:

1. Open conflicted files.
2. Resolve the conflict markers.
3. Stage the resolved files.
4. Commit the merge.

## Working with Remotes

Add a remote repository named `origin`:

```bash
git remote add origin https://github.com/user/repo.git
```

Show configured remotes:

```bash
git remote -v
```

Push your current branch to the remote:

```bash
git push origin main
```

Fetch and merge changes from the remote branch:

```bash
git pull origin main
```

Push a local branch to a new remote branch:

```bash
git push -u origin feature-name
```

## Common Workflows

1. Start a branch for a feature or fix:
   ```bash
git checkout -b feature-name
```
2. Work and stage changes:
   ```bash
git add .
```
3. Commit progress often:
   ```bash
git commit -m "Add feature update"
```
4. Pull latest changes before pushing:
   ```bash
git pull origin main
```
5. Push your branch:
   ```bash
git push origin feature-name
```

## Useful Tips

- Use short, meaningful commit messages.
- Keep commits focused on a single goal.
- Pull before pushing to reduce merge conflicts.
- Use branches for features, fixes, and experiments.
- Use `git log --oneline --graph --all` to inspect history visually.

## Helpful Commands

Show concise commit history:

```bash
git log --oneline --graph --all
```

Discard local changes in a file:

```bash
git checkout -- filename
```

Remove a tracked file from Git and disk:

```bash
git rm filename
```

Undo the last commit but keep changes staged:

```bash
git reset --soft HEAD~1
```

Undo the last commit and unstage changes:

```bash
git reset --mixed HEAD~1
```

## Notes

This is a basic reference suitable for beginners. For advanced workflows, explore rebasing, cherry-picking, and stash commands.
