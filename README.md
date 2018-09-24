# [TinyWebServer](https://github.com/mmaltsev/TinyWebServer)

TinyWebServer is small but scalable web server.

## Setup

#### Install Dependencies
Make sure to have *Python 3* on your system.
Install all required dependencies by executing:

`pip install -r requirements` or `python -m pip install -r requirements`

#### Set Configurations
Edit `config.json` if needed. Make sure to have `HOST`, `PORT` and `ENDPOINTS` specified in the file.

#### Run Web Server
Execute

`python server.py`

You should see the message `Tiny Server is up at HOST:PORT`, where `HOST` and `PORT` are those, which were specifeid at the `config.json` file.

## License.
MIT License. Copyright (c) 2018 Maxim Maltsev.