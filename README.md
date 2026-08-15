# IBM Applied Data Science Capstone — SpaceX Falcon 9 Landing Prediction

Predicts whether the Falcon 9 first stage will land successfully, using
public launch data (payload, orbit, launch site, flight number, booster
reuse). Final deliverable for the IBM Applied Data Science Capstone.

## Contents

| File | Description | Runs offline? |
|---|---|---|
| `01_data_collection_api.ipynb` | Pulls launch data from the SpaceX REST API | No — needs internet |
| `02_data_collection_webscraping.ipynb` | Scrapes historical launch tables from Wikipedia | No — needs internet |
| `03_data_wrangling.ipynb` | Cleans data, builds the binary `Class` label | Yes |
| `04_eda_visualization.ipynb` | Matplotlib EDA charts | Yes |
| `05_eda_sql.ipynb` | SQLite queries: sites, payload, success rates, rankings, time trends | Yes |
| `06_predictive_analysis.ipynb` | GridSearchCV over 4 classifiers, confusion matrix | Yes |
| `folium_map.py` | Interactive launch-site map (markers, clusters, proximity) | No — needs internet |
| `dash_app.py` | Interactive Plotly Dash dashboard (dropdown, slider, pie, scatter) | No — needs internet |
| `falcon9_dataset.csv` | Working dataset used by the offline notebooks | — |
| `Data_Science_Capstone_Project_Report.pptx` | Final presentation | — |

## How to run

1. Notebooks 3–6 run anywhere with Python (Jupyter, Colab, VS Code) — no
   internet required, since they read `falcon9_dataset.csv` directly.
2. Notebooks 1–2 and the two `.py` scripts need internet access (SpaceX
   API, Wikipedia, and Dash's local web server) — run these in Google
   Colab or a local machine with a network connection.
3. For the presentation's Folium/Dash slides, run `folium_map.py` and
   `dash_app.py` locally, screenshot the real output, and drop the images
   into the deck.

## Tools

Python, Pandas, NumPy, Requests, BeautifulSoup, SQLite, Matplotlib,
Folium, Plotly Dash, scikit-learn.
