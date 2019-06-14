# Gympass Interview Test - F1 Race Log Analyzer
This solution was written to solve the challenge to position of Software Engineer at Gympass. The challenge description can be found on [CHALLENGE.md](CHALLENGE.md) file.

The solution is a simple console application written in Python. It analyzes a race log file and give some insights about the race. An example of log can be found on [race-log.txt](race-log.txt) file.

## Requirements
This solution was written and tested with Python 3.7.0, so Python 3.7.0 is mandatory.
Is also possible to run this solution using docker, so is not necessary to install nothing, only Docker.
To simplify the test process I used the libs [PyTest](https://pytest.org) and [AssertPy](https://github.com/ActivisionGameScience/assertpy). Those are the only external libs in the entire project and was used only to simplify the TDD process. You only need to install them if you intend to run the unit tests (strongly recommended).

### Running the tests (optional)
This step is totally optional but strongly recommended. You need to install the external dependencies:  
```sh
$ pip install -r requirements.txt
$ python -m pytest
```

All tests should pass, if some test brake, feel free to open an issue.

## Running solution
You only need to run:  
```sh
$ python main.py race-log.txt
```

The file race-log.txt can be replaced by any other path that contains race-log with same format.

## Running tests and solution with docker
If you have docker on your computer, you can run all the tests and the solution itself with a simple command:  
```sh
$ docker build -t gympass-challenge . && docker run -it gympass-challenge
```
