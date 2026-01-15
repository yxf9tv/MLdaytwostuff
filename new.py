# %% 
import pandas as pd
import numpy as np  
from sodapy import Socrata 
import folium
from folium import plugins

#%%
## my_terminal_path = @yxf9tv ➜ /workspaces/MLdaytwostuff (main) $

### You should not include the virtual environment in the repo

### New Terminal Display Path: (.venv) @yxf9tv ➜ /workspaces/MLdaytwostuff (main) $ 

# Load Data
# %% 
# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cityofnewyork.us", None)

# %%
# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("vfnx-vebw", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

#%%
# Convert x and y columns to numeric
results_df['x'] = pd.to_numeric(results_df['x'], errors='coerce')
results_df['y'] = pd.to_numeric(results_df['y'], errors='coerce')

# Perks of Data Wrangler:
# %%
# (From Data Wrangler README))
# 📊 Visualize & filter large tabular datasets
# 🧹 One-click transforms (fill, drop, type-cast…)
# 🐼 Automatic Pandas code preview & export
# 🚀 Launch from CSV/Parquet/Excel/Jsonl files or Jupyter notebooks
# 🤖 GitHub Copilot integration: just ask it to perform the data operations you need
# ⚙️ FlashFill integration: Provide an example to automatically fill all remaining rows in a column

# Plotly version
#### Plotly==6.5.2
#### We use a requirements file in order to make it easy for people who want to use the repo

# Recipe to create a new working project environment
# %%
#### Step-by-Step Recipe for Creating a New Working Project Environment

# Step 1: Create a Project Directory**
# - Create a new folder for your project: `mkdir my-project`
# - Navigate into it: `cd my-project`
# - Initialize version control: `git init`

# **Step 2: Set Up Python Virtual Environment**
# - Create a virtual environment: `python -m venv venv`
# - Activate the environment:
#   - macOS/Linux: `source venv/bin/activate`
#   - Windows: `venv\Scripts\activate`
# - Verify activation (your terminal should show `(venv)` prefix)

# **Step 3: Create Essential Project Files**
# - Create a requirements.txt file (initially empty)
# - Create a .gitignore file and add:
#   ```
#   venv/
#   __pycache__/
#   *.pyc
#   .DS_Store
#   ```
# - Create your main Python script: `touch main.py` or `script.py`

# **Step 4: Install Required Packages**
# - Upgrade pip: `pip install --upgrade pip`
# - Install needed packages: `pip install package_name`
# - Generate requirements file: `pip freeze > requirements.txt`

# **Step 5: Configure Your Project Structure**
# - Create additional directories as needed (e.g., `mkdir src/`, `mkdir tests/`, `mkdir data/`)
# - Add a `README.md` file with project description

# **Step 6: Initialize Remote Repository**
# - Create a repository on GitHub
# - Add remote: `git remote add origin https://github.com/username/repo.git`
# - Create initial commit: `git add .` → `git commit -m "Initial commit"`
# - Push to remote: `git push -u origin main` (or `master`)

# **Step 7: Verify Environment**
# - Test by running: `python main.py`
# - Ensure all imports work correctly
# - Confirm virtual environment is isolated from system Python

# **Step 8: Document Your Setup**
# - Add setup instructions to README.md for other users/future you
# - Include Python version, key dependencies, and activation steps

# ---

