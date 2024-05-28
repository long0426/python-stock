# python-stock

Pull docker image :

```
docker pull long0426/python-stock:{{TAG}}
```

Build docker image :

```
docker build -t long0426/python-stock:{{TAG}} .
```

Run Container :

```
docker run -it --name {{CONTAINER_NAME}} long0426/python-stock:{{TAG}}
```

Run Container(SSH) :

```
docker run -d -p 22:22 --name {{CONTAINER_NAME}} long0426/python-stock:{{TAG}}
```

SSH connect :
```
ssh -i /{{YOUR_PATH}}/id_rsa root@localhost
```

Create New Git Branch :

```
git checkout -b {{BRANCH_NAME}}
```

Setup git identification :

```
git config --global user.name "{{GIT_USER_NAME}}"
git config --global user.email "{{GIT_USER_EMAIL}}"
```

__________

> [!IMPORTANT]
> :sparkles:***Please request the public and private keys from the administrator.***:sparkles:
