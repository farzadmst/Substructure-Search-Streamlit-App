# Streamlit Substructure Search App

This is a **Streamlit app** for performing **substructure searches** in a **SMILES dataset**. Users can input datasets, define substructure queries using **SMARTS patterns**, and view matching molecules in an interactive interface.
## Live Demo

You can access the live version of the app here:

[Substructure Search App - Streamlit Cloud](https://substructure-search-app.streamlit.app/)
## Features
- Upload a SMILES dataset (in CSV or other formats).
- Search for molecular substructures within the dataset using SMARTS patterns.
- Visualize and explore the results in an intuitive web-based interface.

## Installation

### Prerequisites
- Python 3.x
- Streamlit
- Other dependencies (listed in `requirements.txt`)

### Steps to Run Locally:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/streamlit-substructure-search.git
2. Navigate to the project folder:
   ```bash
   cd streamlit-substructure-search
3. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
5. Run the app:
   ```bash
   Streamlit run substructure_search.py

The app will open in your browser, where you can interact with the app and perform substructure searches.

## How to Use
- Upload a dataset of SMILES strings (CSV format recommended).
- Enter the SMARTS pattern for the substructure you want to search for.
- The app will display matching molecules based on the query.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- Streamlit for creating a powerful app framework.
- Open-source contributors for the tools and libraries used in this project.




   
