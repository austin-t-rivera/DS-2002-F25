#!/bin/bash

# Does this fix everything?

# Exit immediately if a command exits with a non-zero status.
set -e

# Function to check for `upstream` and `origin` remotes
check_remotes() {
    echo "Checking Git remotes..."
    REMOTE_LIST=$(git remote -v)

    # Check that upstream points to the original repo
    if ! echo "$REMOTE_LIST" | grep -q "upstream.*\(https://github.com/austin-t-rivera/DS-2002-F25.git\|git@github.com:austin-t-rivera/DS-2002-F25.git\)"; then
        echo "Error: 'upstream' remote is not set correctly. It should be your instructor's repo." >&2
        exit 1
    fi
    
    # Check that origin does NOT point to the instructor's repo
    if echo "$REMOTE_LIST" | grep -q "origin.*\(https://github.com/austin-t-rivera/DS-2002-F25.git\|git@github.com:austin-t-rivera/DS-2002-F25.git\)"; then
        echo "Error: 'origin' remote is set to your instructor's repo. It should be your personal fork." >&2
        exit 1
    fi
    echo "Remotes are set up correctly."
}

# Function to update `main` branch from `upstream`
update_main() {
    echo "Updating your 'main' branch..."
    git checkout main    # Switch to local main branch
    git fetch upstream    # Download everything from the upstream remote repository
    git merge upstream/main -m "Merging upstream/main into local main via update_repo"    # Merge the commits from upstream/main into your current branch (i.e. your local main branch)
    git push origin main    # push your local main branch to your remote main branch
    echo "Local and Remote 'main' branches are now up to date with the original repo."
}

# Function to handle branch updates
update_branches() {
    echo "Do you want to update your other branches? (Y/N)"
    read -n 1 -r REPLY
    echo

    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Exiting script. Your other branches have not been updated."
        exit 0
    fi

    echo "Your current branches:"
    git branch

    echo "Would you like to update ALL branches or decide One At A Time? (All please / OAAT)"
    read -r DECISION
    
    # Get a list of all local branches except main
    BRANCHES=$(git branch | grep -v main | sed 's/ //g')

    if [[ "$(echo "$DECISION" | tr '[:upper:]' '[:lower:]')" == "all please" ]]; then
        for branch in $BRANCHES; do
            merge_branch "$branch"
        done
    elif [[ "$(echo "$DECISION" | tr '[:upper:]' '[:lower:]')" == "oaat" ]]; then
        for branch in $BRANCHES; do
            merge_branch_interactive "$branch"
        done
    else
        echo "Invalid choice. Exiting script." >&2
        exit 1
    fi
}

# Helper function to merge a single branch
merge_branch() {
    local branch=$1
    echo "Updating branch: $branch"
    git checkout "$branch"
    # Merges main into the current branch with a non-interactive message
    git merge main -m "Merging main into branch via update_repo"
    
    if [ $? -ne 0 ]; then
        handle_conflict "$branch"
    else
        git push origin "$branch"
    fi
}

# Helper function for interactive merge
merge_branch_interactive() {
    local branch=$1
    echo "Do you want to update branch '$branch'? (Y/N)"
    read -n 1 -r REPLY
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        merge_branch "$branch"
    else
        echo "Skipping branch '$branch'."
    fi
}

# Helper function to handle merge conflicts
handle_conflict() {
    local branch=$1
    echo "Merge conflict detected on branch '$branch'. Do you want to skip this branch for now? (Y/N)"
    read -n 1 -r REPLY
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git merge --abort
        echo "Merge aborted. Skipping this branch."
        return 1
    else
        echo "Exiting to resolve conflicts. Please deal with the conflicts and re-run the script." >&2
        exit 1
    fi
}

# Main script logic
check_remotes
update_main
update_branches

# Final checkout to main branch after all operations are complete
git checkout main
echo "Script complete. All specified branches have been updated, and you are back on the main branch."
