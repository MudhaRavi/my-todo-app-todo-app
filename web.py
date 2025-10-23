import streamlit as st
import functions
import datetime

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
st.sidebar.title("Date")
st.sidebar.write(f"Current Date: {current_date}")

todos = functions.get_todos()

def add_todos():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To-Do List App")
st.subheader("Manage your tasks efficiently")
st.write("This is a simple to-do list application built with Streamlit.")

# Initialize session state for tasks
for todo in todos:
    checkbox = st.checkbox(todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        st.rerun()
st.text_input(label="Add a new task:", placeholder="Enter a new to-do item...",
              on_change=add_todos, key="new_todo")







