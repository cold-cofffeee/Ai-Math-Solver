# main.py

import streamlit as st
from sympy import *
import numpy as np



st.header('This is AI Math Solver', divider='rainbow')
st.link_button("Contact me:", "https://www.facebook.com/hiranmayroy123/")


def differentiate_expression(expression, variable):
    x = symbols(variable)
    try:
        expr = sympify(expression)
        result = diff(expr, x)
        return result
    except Exception as e:
        return f"Error: Invalid expression - {str(e)}"

def integrate_expression(expression, variable):
    x = symbols(variable)
    try:
        expr = sympify(expression)
        result = integrate(expr, x)
        return result
    except Exception as e:
        return f"Error: Invalid expression - {str(e)}"

def evaluate_trigonometry_function(function, angle_degrees):
    angle_radians = angle_degrees * (pi / 180.0)
    try:
        if function == 'sin':
            result = sin(angle_radians)
        elif function == 'cos':
            result = cos(angle_radians)
        elif function == 'tan':
            result = tan(angle_radians)
        else:
            result = "Error: Unsupported trigonometric function"
        return result
    except:
        return "Error: Invalid input"

def evaluate_logarithm(base, value):
    try:
        result = log(value, base)
        return result
    except:
        return "Error: Invalid input"

def perform_matrix_operations(matrix_str):
    try:
        matrix = Matrix(eval(matrix_str))
        transpose = matrix.transpose()
        inverse = matrix.inv()
        return f"Transpose:\n{transpose}\n\nInverse:\n{inverse}"
    except:
        return "Error: Invalid matrix"

def expand_binomial(expression):
    try:
        expr = sympify(expression)
        result = expand(expr)
        return result
    except Exception as e:
        return f"Error: Invalid expression for binomial expansion - {str(e)}"

def motion_of_particle_in_plane(initial_position, initial_velocity, acceleration, time):
    try:
        position = initial_position + initial_velocity * time + 0.5 * acceleration * time**2
        return position
    except:
        return "Error: Invalid input for motion of a particle in a plane"

def diffusion_measurement_probability(diffusion_coefficient, time, distance):
    try:
        probability = 1 / (sqrt(4 * pi * diffusion_coefficient * time)) * exp(-distance**2 / (4 * diffusion_coefficient * time))
        return probability
    except:
        return "Error: Invalid input for diffusion measurement and probability"

def solve_polynomial_equation(coefficients):
    x = symbols('x')
    try:
        equation = sum(coefficients[i] * x**i for i in range(len(coefficients)))
        solutions = solve(equation, x)
        return solutions
    except:
        return "Error: Invalid input for polynomial equation"

def solve_real_numbers_inequalities(inequality):
    x = symbols('x')
    try:
        ineq = sympify(inequality)
        solution = solve(ineq, x)
        return solution
    except Exception as e:
        return f"Error: Invalid inequality - {str(e)}"

def vector_operations(vectors):
    try:
        vectors = eval(vectors)
        vec1 = np.array(vectors[0])
        vec2 = np.array(vectors[1])
        addition = vec1 + vec2
        dot_product = np.dot(vec1, vec2)
        cross_product = np.cross(vec1, vec2)
        return f"Addition: {addition}\nDot Product: {dot_product}\nCross Product: {cross_product}"
    except:
        return "Error: Invalid vector input"

def affordable_programs_evaluation(program_cost, user_budget):
    try:
        if program_cost <= user_budget:
            return "Affordable: You can purchase this program!"
        else:
            return "Not Affordable: This program exceeds your budget."
    except:
        return "Error: Invalid input for program cost evaluation"

def statics_analysis(force, angle):
    try:
        angle_radians = angle * (pi / 180.0)
        force_x = force * cos(angle_radians)
        force_y = force * sin(angle_radians)
        return f"Force Components:\nX: {force_x}\nY: {force_y}"
    except:
        return "Error: Invalid input for statics analysis"

def main():
    st.title("AI Math Solver")

    st.sidebar.title("Math Operations")
    options = ["Differentiation", "Integration", "Trigonometry", "Logarithm", "Matrix Operations",
               "Binomial Expansion", "Motion of a Particle", "Diffusion Measurement",
               "Solve Polynomial Equation", "Solve Inequalities", "Vector Operations",
               "Affordable Program Evaluation", "Statics Analysis"]
    choice = st.sidebar.selectbox("Select an operation", options)

    if choice == "Differentiation":
        expression = st.text_input("Enter expression to differentiate:", "x**2 + 3*x + 1")
        variable = st.text_input("Enter variable with respect to which you want to differentiate:", "x")
        if st.button("Differentiate"):
            result = differentiate_expression(expression, variable)
            st.write("Result:", result)

    elif choice == "Integration":
        expression = st.text_input("Enter expression to integrate:", "x**2")
        variable = st.text_input("Enter variable with respect to which you want to integrate:", "x")
        if st.button("Integrate"):
            result = integrate_expression(expression, variable)
            st.write("Result:", result)

    elif choice == "Trigonometry":
        function = st.selectbox("Select function", ["sin", "cos", "tan"])
        angle = st.number_input("Enter angle in degrees:", 0.0)
        if st.button("Evaluate"):
            result = evaluate_trigonometry_function(function, angle)
            st.write("Result:", result)

    elif choice == "Logarithm":
        base = st.number_input("Enter base:", 2.0)
        value = st.number_input("Enter value:", 1.0)
        if st.button("Evaluate"):
            result = evaluate_logarithm(base, value)
            st.write("Result:", result)

    elif choice == "Matrix Operations":
        matrix_str = st.text_area("Enter matrix as a list of lists (e.g., [[1, 2], [3, 4]]):", "[[1, 2], [3, 4]]")
        if st.button("Perform Operations"):
            result = perform_matrix_operations(matrix_str)
            st.write("Result:", result)

    elif choice == "Binomial Expansion":
        expression = st.text_input("Enter expression for binomial expansion:", "(x + 1)**3")
        if st.button("Expand"):
            result = expand_binomial(expression)
            st.write("Result:", result)

    elif choice == "Motion of a Particle":
        initial_position = st.number_input("Enter initial position:", 0.0)
        initial_velocity = st.number_input("Enter initial velocity:", 0.0)
        acceleration = st.number_input("Enter acceleration:", 0.0)
        time = st.number_input("Enter time:", 0.0)
        if st.button("Calculate Position"):
            result = motion_of_particle_in_plane(initial_position, initial_velocity, acceleration, time)
            st.write("Result:", result)

    elif choice == "Diffusion Measurement":
        diffusion_coefficient = st.number_input("Enter diffusion coefficient:", 1.0)
        time = st.number_input("Enter time:", 1.0)
        distance = st.number_input("Enter distance:", 1.0)
        if st.button("Calculate Probability"):
            result = diffusion_measurement_probability(diffusion_coefficient, time, distance)
            st.write("Result:", result)

    elif choice == "Solve Polynomial Equation":
        coefficients_str = st.text_input("Enter coefficients as a list (e.g., [1, 0, -1] for x^2 - 1):", "[1, 0, -1]")
        if st.button("Solve"):
            try:
                coefficients = eval(coefficients_str)
                result = solve_polynomial_equation(coefficients)
                st.write("Result:", result)
            except Exception as e:
                st.write(f"Error: {str(e)}")

    elif choice == "Solve Inequalities":
        inequality = st.text_input("Enter inequality (e.g., x**2 - 1 > 0):", "x**2 - 1 > 0")
        if st.button("Solve"):
            result = solve_real_numbers_inequalities(inequality)
            st.write("Result:", result)

    elif choice == "Vector Operations":
        vectors_input = st.text_area("Enter vectors in the form [[1, 2, 3], [4, 5, 6]]:", "[[1, 2, 3], [4, 5, 6]]")
        if st.button("Perform Operations"):
            vector_operations_result = vector_operations(vectors_input)
            st.write(f"Result:\n{vector_operations_result}")

    elif choice == "Affordable Program Evaluation":
        program_cost = st.number_input("Enter program cost:", 0.0)
        user_budget = st.number_input("Enter your budget:", 0.0)
        if st.button("Evaluate"):
            result = affordable_programs_evaluation(program_cost, user_budget)
            st.write(result)

    elif choice == "Statics Analysis":
        force = st.number_input("Enter force magnitude:", 0.0)
        angle = st.number_input("Enter force angle in degrees:", 0.0)
        if st.button("Analyze"):
            statics_result = statics_analysis(force, angle)
            st.write(f"Result:\n{statics_result}")

if __name__ == "__main__":
    main()
