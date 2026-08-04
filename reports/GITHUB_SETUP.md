# Create / link GitHub remote

Local git is ready in this folder (`main`, 2 commits). `gh` is not installed on this machine yet.

## Option A — GitHub website (no CLI)

1. Open https://github.com/new  
2. Repository name suggestion: `grambank-side-harmony`  
3. **Private** recommended until submission (or Public if you prefer)  
4. Do **not** add README / .gitignore / license (repo already has commits)  
5. Then run:

```bash
cd /Users/domi/Documents/Uni/DataScience_Lingo/project
git remote add origin git@github.com:YOUR_USER/grambank-side-harmony.git
# or HTTPS:
# git remote add origin https://github.com/YOUR_USER/grambank-side-harmony.git
git push -u origin main
```

## Option B — GitHub CLI (after install)

```bash
# Homebrew
brew install gh

# or download: https://cli.github.com/

gh auth login
cd /Users/domi/Documents/Uni/DataScience_Lingo/project
gh repo create grambank-side-harmony --private --source=. --remote=origin --push
```

## Invite supervisor later

```bash
gh repo invite JohannesDellert --permission push
# or add collaborator in GitHub Settings → Collaborators
```

(Use his actual GitHub username when known.)
