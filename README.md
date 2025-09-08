# Filter Me If You Can

<img src="assets/image.png" alt="Filter Me If You Can logo" width="250"/>

### A mini Python project to practice:
- Classes
- Reading CSV files
- Converting data into a **pandas** DataFrame
- Filtering and saving new files


## How to run
1. Clone this repository
2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```
3. Run the project with Poetry:

    ```bash
    poetry run python main.py
    ````
## Project Structure

````
filter-me-if-you-can/
│── src/
│   ├── core/        # main classes
│   ├── main.py      # entry point
│── data/            # input and output files
│── assets/          # images for the README
│── pyproject.toml   # Poetry dependencies
│── README.md
````

## Goal

Load a CSV file, transform it into a DataFrame, apply filters, and save the result.
A quick and fun exercise to practice object-oriented Python.
