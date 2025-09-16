# Working with remote data

## json

### Fetch Remote Data using `curl` and `jq`
```
# Replace USER with your GitHub username
```
curl https://api.github.com/users/USER/events
```

### Scroll through events
```
curl https://api.github.com/users/nmagee/events | jq .[] | less
```

### Filter out values:
```
curl https://api.github.com/users/nmagee/events | jq .[].id
curl https://api.github.com/users/nmagee/events | jq .[].payload.commits
curl https://api.github.com/users/nmagee/events | jq .[].payload.commits | jq .[].message
```

### Format output:
```
curl 'https://api.github.com/repos/stedolan/jq/commits'
curl 'https://api.github.com/repos/stedolan/jq/commits' \
   | jq '.[] | {message: .commit.message, name: .commit.committer.name}'
```

There are plenty of other examples in the tutorial at https://stedolan.github.io/jq/tutorial/

## Tools for Retrieving Data

`curl` - is a common Linux-based tool to fetch raw files. You've been using it in the exercises above.
```
curl https://www.virginia.edu/ > index.html
```

`wget` - another common Linux-based tool, similar to `curl`.
```
wget https://www.virginia.edu/
```

`http` - runs the HTTPie tool to fetch web resources:
```
http --head https://www.virginia.edu/
http --body https://www.virginia.edu/
```

Windows 10 and above come with `curl.exe` installed:
```
# example 1
curl.exe --output index.html --url https://superuser.com
# example 2
curl.exe -o index.html https://superuser.com
```
