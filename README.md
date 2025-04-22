# CS 5040 Final Project
## Team Members - Brandon Herrin, Ethan Stapley, Trevor Shupe

### Creating and Configuring Python Environment
For the best results with the Jupyter Notebooks, please set up a virtual Python environment using `venv` and install the Python packages found in `requirements.txt`.

```bash
python -m venv env

# Activate the virtual environment (on Linux)
source env/bin/activate

pip install -r requirements.txt
```

### 2D Visualizations

The 2D Visualization of the Vector Field and the Coreline Extraction is located under `[src/vortex.ipynb](src/vortex.ipynb)`. Before launching the notebook, make sure the virtual Python environment is active and has the appropriate packages installed.

### 3D Visualizations

The 3D Visualizations of the Vector Field and Coreline Extraction are contained within the Paraview state files in the [`paraview`](paraview/) directory and in `[coreline.py](src/coreline.py)` and `[coreline_through_time.py](src/coreline_through_time.py)` under the `src` directory. The two Python scripts will launch interactive PyVista windows.

**Note: Make sure the `beads2d.vti` dataset is downloaded and located in whichever directory you launch the scripts from.** `beads2d.vti` can be downloaded from [here](https://cgl.ethz.ch/Downloads/Data/ScientificData/beads2d_vti.zip)



```bash
python src/coreline_through_time.py

python src/coreline.py
```