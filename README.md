# Integration of Offshore Energy into the National Energy System: A Case Study on Belgium

This repository contains all the necessary files to reproduce the simulations presented in the article:  
**_"Integration of offshore energy into national energy system: a case study on Belgium"_**.

The study models a multi-carrier energy system (natural gas, electricity, and hydrogen) for Belgium in 2050 under a carbon neutrality constraint, aiming to assess whether the energy mix should include offshore hydrogen production.

---

## Repository Structure

The repository is organized into **3 main folders** and several standalone files outside these folders.

### Key Files
- **`Gboml_runner.ipynb`**:  
  This Jupyter notebook is used to run the simulations.  
  - Each cell corresponds to a scenario sensitivity test.  
  - The first cell ("Set up") must be executed before running any other scenario-related cells.  
  - In the second-to-last line of the "Set up" cell, adjust the `file_path` to specify where the CSV and JSON results files will be exported.

- **`3_cluster_Belgium.txt`** and **`3_clusters_Belgium_DC.txt`**:  
  These files contain the GBOML code required by `Gboml_runner.ipynb` to run the scenarios.

- **`gurobi_detail.txt`** and **`gurobi.opt.txt`**:  
  Configuration files for the Gurobi optimizer used in the simulations.

- **`requirements.txt`**:  
  Lists the Python packages required to run the code.  
  Install them using:
  ```bash
  pip install -r requirements.txt

---

### Folders

#### 1. `Data`
- Contains all the **timeseries data** used in the model.

#### 2. `Templates`
- Includes **technology-specific code**, which is used in the files:
  - `3_cluster_Belgium.txt`
  - `3_clusters_Belgium_DC.txt`
- These files help to construct the complete model.

#### 3. `Postprocessing`
- Contains the **code for generating result analysis graphs**.
- Key files in this folder:
  - **`Postprocessing_3C_loop.py`**:  
    - Generates the graphs shown in Section 4 ("Results and Discussion") of the article.  
    - Also creates additional graphs for a deeper analysis of results.  
    - **Important**: Update the `file_path` at line 31 to specify the directory where the results are saved.  
    - Once executed, subfolders are created within `Postprocessing` for each scenario, containing the associated graphs.

  - **`Distance_sensitivity.ipynb`** and **`H2_import_sensitivity.ipynb`**:  
    - These Jupyter notebooks generate the graphs for Section 5 ("Sensitivity Analysis") of the article.  
    - **Important**: Modify the `file_path` in the second cell ("Data import") to load the correct data.  
    - Execute the notebooks to produce the graphs.

  - **Other files**:  
    - Support the scripts and notebooks mentioned above. They are essential for running the postprocessing workflows.

## How to Use

### Running the Simulations
1. Open the Jupyter notebook **`Gboml_runner.ipynb`**.
2. Execute the **"Set up" cell** at the top of the notebook.
   - This initializes the required settings for the simulations.
3. Update the `file_path` in the **second-to-last line** of the "Set up" cell:
   - Define the directory where the simulation results will be saved (in CSV and JSON formats).
4. Execute the cells corresponding to the desired scenarios to run the simulations.

---

### Generating Graphs

#### For Graphs in Section 4 ("Results and Discussion"):
1. Open the Python script **`Postprocessing_3C_loop.py`**.
2. Update the `file_path` at **line 31** to point to the directory where the simulation results are stored.
3. Run the script:
   - Subfolders will be created inside the **`Postprocessing`** folder for each scenario.
   - These subfolders will contain the generated graphs.

#### For Sensitivity Analysis Graphs (Section 5):
1. Open the Jupyter notebooks:
   - **`Distance_sensitivity.ipynb`**
   - **`H2_import_sensitivity.ipynb`**
2. Update the `file_path` in the **second cell** ("Data import"):
   - Ensure the path points to the directory containing the simulation results.
3. Execute the notebook to generate the sensitivity analysis graphs.

---

### Notes
- Ensure that all required dependencies are installed before running any script or notebook. Use:
  ```bash
  pip install -r requirements.txt

---

## Citation

If you use this repository or reference the associated work, please cite the following article:

**_"Integration of offshore energy into national energy system: a case study on Belgium"_**



