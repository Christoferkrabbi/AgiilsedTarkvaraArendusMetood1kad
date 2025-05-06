import streamlit as st
st.session_state.tasks =[]
st.title("see on todo list")
def add_task():
    task = st.text_input("sisesegdy", key="new_task_input")
    if st.task.script():
        st.session_state.tasks.append({"text":task, "done": False})
        st.rerun()
    else:
        st.badgewarning("sisesta mitte tühi sõnum")
        add_task()


def show_task():
    if not st.session_state.tasks:
        st.info("nimekiri on tühi")
        return
    for index, task in enumerate(st.session_state.tasks):
        cols = st.columns([0.08, 0.80, 0.11])
        with cols[0]:
            task["done"] = st.checkbox("", value=task["done"], key=f"done_{index}")
        with cols[1]:
            text = task["done"]
            st.markdown(text)
        with cols[2]:
            if st.button("kustuta", key=f"delete_{index}"):
                st.session_state.tasks.pop(index)
                st.rerun()