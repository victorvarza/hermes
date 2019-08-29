# Hermes

## Configure gdrive auth 
```
https://pythonhosted.org/PyDrive/quickstart.html#authentication
```

## run docker
```
/usr/bin/docker run \
        -v /docker/hermes/conf:/app/conf:rw \
        -v /mnt/monitor:/monitor:rw \
        -v /docker/hermes/conf/client_secrets.json:/app/client_secrets.json \
        --name hermes \
        qedzone/hermes:1.0
```

```
ls -l /docker/hermes/conf
-rw-r--r-- 1 root root 453 May 29 14:32 client_secrets.json
-rw-r--r-- 1 root root 947 May 29 15:34 gdrive_cred.json
-rw-r--r-- 1 root root 402 May 29 15:27 hermes.yaml
```

```
/mnt/monitor --> folder to monitor
```