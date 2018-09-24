# [TinyWebServer](https://github.com/mmaltsev/TinyWebServer)

TinyWebServer is a light but reliable web server.

## Setup.

#### Install Dependencies
Make sure to have *Python 3* on your system.

After that, install all required dependencies by executing:

`pip install -r requirements` or `python -m pip install -r requirements`

#### Set Configurations
Edit `config.json` if needed.

Make sure to have `HOST`, `PORT` and `ENDPOINTS` specified in the file.

#### Run Web Server
Execute `python server.py`.

You should see the message `Tiny Web Server is up at HOST:PORT`, where `HOST` and `PORT` are those specified in the `config.json` file.

#### Request Data
If the server was executed with the default configurations, navigate to `http://0.0.0.0:8080/example`.

You should see there a dummy JSON file served at the `/example` endpoint.
```JSON
{
  "one": 1
}
```

## License.
MIT License. Copyright (c) 2018 Maxim Maltsev.