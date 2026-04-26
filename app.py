import streamlit as st

st.title("SIMPLE CALCULATOR")

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []
if "last_result" not in st.session_state:
    st.session_state.last_result = None
if "num1_input" not in st.session_state:
    st.session_state.num1_input = 0.0
if "num2_input" not in st.session_state:
    st.session_state.num2_input = 0.0

# Safety: fix stale/invalid widget values from older sessions
if not isinstance(st.session_state.num1_input, (int, float)):
    st.session_state.num1_input = 0.0
if not isinstance(st.session_state.num2_input, (int, float)):
    st.session_state.num2_input = 0.0


def use_last_result():
    if st.session_state.last_result is not None:
        st.session_state.num1_input = float(st.session_state.last_result)


# Inputs
col1, col2 = st.columns(2)

with col1:
    num1_input = st.number_input("Enter the 1st number:", step=1.0, key="num1_input")

with col2:
    num2_input = st.number_input("Enter the 2nd number:", step=1.0, key="num2_input")
    

operation = st.selectbox("Choose the operation:", ["+", "-", "*", "//", "%", "/"])

if st.session_state.last_result is not None:
    st.button("Use Last Result as First Number", on_click=use_last_result)

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
        st.session_state.history.append(f"{num1_input} {operation} {num2_input} = {result}")

# History section
st.divider()
st.subheader("Previous Calculations")

if st.session_state.history:
    for item in reversed(st.session_state.history):
        st.write(item)

    # Clear only history; keep last_result for reuse feature
    if st.button("Clear History"):
        st.session_state.history = []
        st.success("History cleared.")
else:
    st.info("No calculations yet.")
