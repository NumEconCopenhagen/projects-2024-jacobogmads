# Model Analysis Project

## Project Title
**Dynamic Optimization in Economics: The Cake-Eating Problem**

## About
This project explores the dynamic optimization problem commonly known in economic theory as the "Cake-Eating Problem". The objective is to determine an optimal consumption strategy that maximizes long-term utility from a finite resource. We implement this model using the Bellman equation in a discrete-time setup and solve it using value function iteration. The model provides insights into how different parameters like discount factor, population growth rate, and capital elasticity affect consumption decisions over time.

## Results
The results of the project can be seen from running [modelproject.ipynb](modelproject.ipynb). This Jupyter Notebook includes a detailed implementation of the Cake-Eating model, the computational methods used to solve it, and visualizations of the policy and value functions over different capital grids.

## Dependencies
Apart from a standard Anaconda Python 3 installation, the project requires the following packages:
- `numpy`
- `scipy`

Ensure these packages are installed by running:
```bash
conda install numpy scipy
```

or using pip:
```bash
pip install numpy scipy
```

## Usage
To view and interact with the project:
1. Ensure you have Jupyter Notebook installed via Anaconda or using pip.
2. Open the terminal or command prompt.
3. Navigate to the project directory.
4. Run the command:
   ```bash
   jupyter notebook modelproject.ipynb
   ```
5. The notebook will open in your default web browser where you can run and modify the simulations.