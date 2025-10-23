# AI Math Solver

A Streamlit-based AI Math Solver that performs various mathematical operations including differentiation, integration, trigonometry, matrix operations, and more.

## ⚠️ Important Compatibility Note

**Python Version:** This project requires **Python 3.9 - 3.12**. Python 3.14 is currently too new and lacks pre-built wheels for required dependencies (Streamlit, PyArrow). Please install Python 3.12 or earlier from [python.org](https://www.python.org/downloads/).

## Features

- **Differentiation**: Calculate derivatives of mathematical expressions
- **Integration**: Calculate integrals of mathematical expressions
- **Trigonometry**: Evaluate sin, cos, tan functions
- **Logarithm**: Calculate logarithms with custom base
- **Matrix Operations**: Perform transpose and inverse operations
- **Binomial Expansion**: Expand binomial expressions
- **Motion of a Particle**: Calculate particle position in a plane
- **Diffusion Measurement**: Calculate diffusion probability
- **Solve Polynomial Equations**: Find roots of polynomial equations
- **Solve Inequalities**: Solve mathematical inequalities
- **Vector Operations**: Perform addition, dot product, and cross product
- **Affordable Program Evaluation**: Check if a program fits your budget
- **Statics Analysis**: Analyze force components

## Installation

1. **Ensure you have Python 3.9 - 3.12 installed**
2. Clone this repository
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run main.py
```

The app will open in your default web browser. Select an operation from the sidebar and enter the required inputs.

## Example Inputs

- **Differentiation**: `x**2 + 3*x + 1` with respect to `x`
- **Integration**: `x**2` with respect to `x`
- **Binomial Expansion**: `(x + 1)**3`
- **Matrix**: `[[1, 2], [3, 4]]`
- **Polynomial**: `[1, 0, -1]` for x² - 1
- **Vectors**: `[[1, 2, 3], [4, 5, 6]]`

## Requirements

- Python 3.9 - 3.12 (NOT 3.13+)
- streamlit
- sympy
- numpy

## Troubleshooting

If you encounter installation errors, ensure:
1. You're using Python 3.9 - 3.12 (check with `python --version`)
2. pip is up to date: `python -m pip install --upgrade pip`
3. All dependencies are installed: `pip install -r requirements.txt`
