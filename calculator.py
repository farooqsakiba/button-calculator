import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")
st.title("Button Calculator")

# Session states
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Display input field
expression = st.text_input("Type here or use buttons:", value=st.session_state.expression)

# Manual typing
if expression != st.session_state.expression:
    try:
        expr = expression.replace("÷", "/").replace("×", "*")
        expression = str(eval(expr))
    except:
        expression = "Error"
    st.session_state.expression = expression


# Show current expression
st.code(st.session_state.expression, language="")

# Button click handler
def button_click(value):
    if value == "C":
        st.session_state.expression = ""
    elif value == "=":
        try:
            expr = st.session_state.expression
            expr = expr.replace("÷", "/").replace("×", "*")
            st.session_state.expression = str(eval(expr))
        except:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += value

# Buttons
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-\u00A0"],
    ["C", "0", "=", "+\u00A0"]
]

# Render buttons
for row in buttons:
    cols = st.columns(len(row))
    for i, label in enumerate(row):
        cols[i].button(label, on_click=button_click, args=(label,))





