# Optimized `g` Function Generator for Quantum Gates

This repository contains Python tools to generate the optimized `g` function as defined [here](https://arxiv.org/abs/2507.02030) (Eq. (34)), for specific quantum unitary transformations (currently one- and two-qubit gates).

The `g` function can be computed fully or queried at a specific entry `(α, β)`, depending on your needs. The repository also includes precomputed examples for commonly used gates.

## Features

- Compute the full optimized `g` function for a given unitary
- Query a specific entry `(α, β)` of the function
- Precomputed results for:
  - **CNOT** (`g_CNOT.npy`)
  - **iSWAP** (`g_iSWAP.npy`)

## Repository Structure
.
├── src/
│ ├── __init__.py
│ ├── optimizer.py  # Core logic for generating and evaluating g
│ └── utils.py      # Auxiliary functions
├── examples/
│ ├── g_CNOT.npy    # Precomputed g for CNOT
│ └── g_iSWAP.npy   # Precomputed g for iSWAP
├── requirements.txt
└── README.md

## Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/m-crupi/optimal_g.git
cd optimal_g
python -m venv .venv
# On Unix/macOS
source .venv/bin/activate
# On Windows
.venv\Scripts\activate

pip install -r requirements.txt
