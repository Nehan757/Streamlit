import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #ADD8E6; /* Light blue */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Data Science Portfolio")

st.header("Heading")
st.subheader("Subheading")

st.text("this is a random text")

st.success("Sucess")
st.error("Fail")
st.warning("Warning")
st.info("Information")

st.selectbox("Select an option", options=["Data Scientist", "ML Engineer", "Data Analyst"])
if not st.checkbox("I Agree to terms and Conditions") :
    st.text("Select to continue")

if st.button("Click to see a Quote"):
     st.text("Dont be so Fixated")
