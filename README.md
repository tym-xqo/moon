# moon

A simple CLI moon phase toy with [PyEphem](TK) and [CoreLocationCLI](https://github.com/fulldecent/corelocationcli).

## Installation

Clone this repo, then

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The script assumes you are using a Mac and have CoreLocationCLI installed

```sh
brew install cask corelocationcli
```

## Usage

`python moon.py` prints a human-readable moon phase, the percent illuminated, and calendar date of the next New, Full, or Quarter moon event, for example: 

```txt
The Moon today is Waning Gibbous, with 99.16% illuminated
Last Quarter upcoming on 2021-05-03
```

## Tests

[TK]

Contributions, issue reports, and any other related contact always welcome.
