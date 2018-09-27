# [TinyWebServer](https://github.com/mmaltsev/TinyWebServer)

TinyWebServer is a light but reliable web server.

## Setup.

#### Install Dependencies
Make sure to have *Python 3* on your system.

After that, install all required dependencies by executing:

`pip install -r requirements` or `python -m pip install -r requirements`

#### Set Configurations
Edit `config.json` if needed.

Make sure to have `HOST` and `PORT` specified in the file.

Feel free to edit any of the properties from the configuration file.

#### Run Web Server
Execute `python server.py`.

You should see the message `Tiny Web Server is up at HOST:PORT` in the console, where `HOST` and `PORT` are those specified in the `config.json` file.

#### Request Data
If the server was executed with the default configurations, navigate to `http://0.0.0.0:8080/one` (by default, `HOST` is `'0.0.0.0'` and `PORT` is `'8080'`).

You should see there a dummy JSON file served at the `/one` endpoint.
```JSON
{
    "one": 1
}
```

#### Add New Endpoint
In order to add more endpoints, please, follow the instructions:
* edit `config.json` by adding new property to the `ENDPOINTS`. Specify `request_type`, `mime_type` and `method_name`.
* create a function in the `endpoints.py` by the name `method_name`. Specify endpoint's functionality there.

## License.
MIT License. Copyright (c) 2018 Maxim Maltsev.