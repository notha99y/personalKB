## Docker

- Default docker network using proxy [link](https://docs.docker.com/network/proxy/)
- Do it in docker file. Set and unset[link](https://stackoverflow.com/questions/55789409/how-to-unset-env-in-dockerfile)

## Docker Compose

Instead of adding the proxy into the DockerFile, you can specify it as an `BUILD_ARGS`

```bash
# Some Shell File
BUILD_ARGS="--build-arg http_proxy=http://user:pw@address:port \
            --build-arg https_proxy=http://user:pw@address:port \
            --build-arg HTTP_PROXY=http://user:pw@address:port \
            --build-arg HTTPS_PROXY=http://user:pw@address:port"

docker-compose build ${BUILD_ARGS} container_name
```

## Apt

- apt-get install [link](https://www.unixmen.com/45713-2/)
[link](https://stackoverflow.com/questions/11211705/how-to-set-proxy-for-wget)
```bash
sudo vi /etc/apt/apt.conf
```
```bash
# apt.conf
Acquire::http::Proxy "http://user:pass@proxy_host:port";
```
- apt-key
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --keyserver-options http-proxy=http://localhost:3128 --recv-keys BBEBDCB318AD50EC6865090613B00F1FD2C19886
```
- apt-add-repository
```bash
export http_proxy=http://<proxy>:<port>
export https_proxy=http://<proxy>:<port> #sometimes its only http
sudo -E apt-add-repository ppa:linaro-maintainers/toolchain
```
## Wget

For all users of the system via the `/etc/wgetrc` or for the user only with the `~/.wgetrc file`:

```bash
# wgetrc 
use_proxy=yes
http_proxy=127.0.0.1:8080
https_proxy=127.0.0.1:8080
```
or via -e options placed after the URL:
```bash
wget ... -e use_proxy=yes -e http_proxy=127.0.0.1:8080 ..
```

## Curl
```bash
curl -L -O <url> --proxy <http_proxy>
```

From man curl:
```bash
-x, --proxy <[protocol://][user:password@]proxyhost[:port]>

     Use the specified HTTP proxy. 
     If the port number is not specified, it is assumed at port 1080.
```

## Pip
```bash
pip install --proxy=http://user:pw@address:port somepackage

# example
pip install --proxy=http://user:pw@address:port numpy
```


## Conda
```bash
conda config --set proxy_servers.http http://user:pw@address:port
conda config --set proxy_servers.https https://user:pw@address:port
```