## Deployment Guide (Linux)

## Prerequisites

- python 3.9.5
    $ `python3.9 -V` should show python 3.9.5 version, else install
    
***Install***\
    - `sudo apt-get install gcc openssl-devel bzip2-devel libffi-devel zlib-devel`\
    - `wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz`\
    - `tar xzf Python-3.9.5.tgz`\
    - `cd Python-3.9.5`\
    - `sudo ./configure --enable-optimizations`\
    - `sudo make altinstall`\
    - `sudo rm Python-3.9.5.tgz`\
    - `python3.9 -V`\

## One Time Configuration

### Gunicorn

1. Linux: Move `rest_flask/deployment/rest_flask_gunicorn.service` file to `/etc/systemd/system/` directory.
2. Update <NODE_IP> with the server node ip address
3. Linux: Run following commands.\
    3.1. `sudo systemctl daemon-reload`\
    3.2. `sudo systemctl stop rest_flask_gunicorn`\
    3.3 `sudo systemctl start rest_flask_gunicorn`\
    3.4 `sudo systemctl enable rest_flask_gunicorn`\

### Python
1. Code: Open `rest_flask/deployment/profac.conf` file, replace the place holder `<...>` with appropriate value.
2. Linux: Move the above file to `/home/services/`

## Deployment Configuration

### Python/Flask
1. Fetch the latest code from codebase, then move it to `/home/servers/rest_flask/`.
2. Linux: Run the command $ `cd /home/servers/rest_flask && make && ..`
3. Restart Gunicorn server: $ `sudo systemctl restart rest_flask_gunicorn`

***Not required: Helpful commands***
- gunicorn restart: $ `sudo systemctl restart rest_flask_gunicorn`
- gunicorn status: $ `sudo systemctl status rest_flask_gunicorn`
