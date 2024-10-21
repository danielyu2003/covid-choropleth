# covid-choropleth

## About

A collection of forecasting models trained on the NYT Covid-19 database,
with animations showing the number of cases over time for a given area.

## Setup

Prerequisites:
- python3 and pip
- make

1. Clone the repo and cd into it.

2. (Optionally) Initialize a virtual environment inside the repo.

3. Run `pip install -r requirements.txt`.

4. Run `make`.

## Usage

To run a given model, run `python3 -m models.[module]` where [module] is one of
the listed modules, ex. `python3 -m models.prophet`.

## Contribution

Feel free to open an issue or a pull request to improve this project.

## License

This project is 