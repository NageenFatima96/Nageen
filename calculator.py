import streamlit as st
from add import add_numbers
from subtract import subtract_numbers
from multiply import multiply_numbers
from divide import divide_numbers

st.title('Nageen Calculator')

def calculator():
    # Input fields for two numbers
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Dropdown for selecting the operator
    operator = st.selectbox("Choose an operator:", ['+', '-', '*', '/'])

    # Perform the calculation based on the operator
    if operator == '+':
        result = add_numbers(num1, num2)
    elif operator == '-':
        result = subtract_numbers(num1, num2)
    elif operator == '*':
        result = multiply_numbers(num1, num2)
    else:
        try:
            result = divide_numbers(num1, num2)
        except ValueError as e:
            st.error(f"Error: {e}")
            result = None

    # Display the result
    if result is not None:
        st.success(f"Result: {result}")


if __name__ == "__main__":
    calculator()
