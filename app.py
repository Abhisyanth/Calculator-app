import streamlit as st

st.title("SIMPLE CALCULATOR")
st.write("A simple calculator for doing addition, subtraction and other operations")

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []
if "last_result" not in st.session_state:
    st.session_state.last_result = None


# Callback for reuse button
def use_last_result():
    st.session_state.num1_input = st.session_state.last_result


# Inputs
col1, col2 = st.columns(2)
with col1:
    num1_input = st.number_input(
        "Enter the 1st number:", value=0.0, step=1.0, key="num1_input"
    )
with col2:
    num2_input = st.number_input(
        "Enter the 2nd number:", value=0.0, step=1.0, key="num2_input"
    )

operation = st.selectbox("Choose the operation:", ["+", "-", "*", "//", "%", "/"])

if st.session_state.last_result is not None:
    st.button(
        "Use Last Result as First Number",
        on_click=use_last_result,
    )

# Calculate
result = None
if st.button("Calculate"):
    if operation == "+":
        result = num1_input + num2_input
    elif operation == "-":
        result = num1_input - num2_input
    elif operation == "*":
        result = num1_input * num2_input
    elif operation == "%":
        if num2_input == 0:
            st.error("Cannot modulo by zero!")
        else:
            result = num1_input % num2_input
    elif operation == "//":
        if num2_input == 0:
            st.error("Cannot divide by zero!")
        else:
            result = num1_input // num2_input
    elif operation == "/":
        if num2_input == 0:
            st.error("Cannot divide by zero!")
        else:
            result = round(num1_input / num2_input, 2)

    if result is not None:
        st.session_state.last_result = result
        st.subheader("Calculation Result")
        st.success(f"{num1_input} {operation} {num2_input} = {result}")
        history_entry = f"{num1_input} {operation} {num2_input} = {result}"
        st.session_state.history.append(history_entry)

# History section
st.divider()
st.subheader("Previous Calculations")

if len(st.session_state.history) > 0:
    for item in reversed(st.session_state.history):  # newest first
        st.write(item)

    if st.button("Clear History"):
        st.session_state.history = []
        st.session_state.last_result = None
        st.success("History cleared.")
else:
    st.info("No calculations yet.")