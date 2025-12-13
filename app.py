import streamlit as st
import pyperclip

st.title("Here you go :)")

with st.form("Data Entry Form"):
    dealer = st.text_input("Dealer")
    subject = st.text_input("Subject")
    phone_numbers = st.text_input("Phone Number(s)")
    vehicle = st.text_input("Vehicle")
    vin = st.text_input("VIN")
    notes = st.text_area("Notes")

    submitted = st.form_submit_button("Submit")

if submitted:
    output_lines = [
        f"Dealer: {dealer}",
        f"Subject: {subject}",
        f"Phone Number(s): {phone_numbers}",
        f"Vehicle: {vehicle}",
        f"VIN: {vin}",
        f"Notes: {notes}",
    ]
    output = "\n".join(output_lines)
    st.code(output)
