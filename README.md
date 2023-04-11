# API Client with Tkinter GUI

This is a simple API client with a graphical user interface built using the Python tkinter library. It allows you to make GET and POST requests to an API, and display the results in a text widget.

## Getting started

1. Clone this repository or download the source code
2. Install the required dependencies by running `pip install -r requirements.txt`
3. Run the program using `python api_client_gui.py`

## How to use

1. Enter the API URL and API token in the respective entry fields.
2. Choose the HTTP method (GET or POST) you want to use.
3. If using POST, enter the JSON payload in the text area provided.
4. Click the "Send Request" button to send the request to the API.
5. The response will be displayed in the text widget.

Note: This program ignores SSL certificates, so be careful when using it to make requests to untrusted endpoints.

## Dependencies

- Python 3.x
- tkinter
- requests

## Contributing

Contributions are welcome! Feel free to submit a pull request.
