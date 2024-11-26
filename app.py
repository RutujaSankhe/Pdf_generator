#Import Libraries
import streamlit as st
from fpdf import FPDF

st.title("Test App")
st.write("If you see this, Streamlit is working correctly!")

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", style="B", size=14)
        self.cell(0, 10, "Service Proposal & Pricing", ln=True, align="C")
        self.ln(10)  # Add a blank line below header

def create_pdf(name, date, address, phone):
    pdf = PDF()
    pdf.add_page()

    # Add content
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Date: {date}", ln=True)
    pdf.ln(5)
    pdf.cell(0, 10, f"Name: {name}", ln=True)
    pdf.cell(0, 10, f"Address: {address}", ln=True)
    pdf.cell(0, 10, f"Phone Number: {phone}", ln=True)

    pdf.ln(10)  # Add space before pricing
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Pricing Information:", ln=True)

    # Sample pricing data (from the uploaded PDF)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "1. AI Automations (6 Scenarios): £1000", ln=True)
    pdf.cell(0, 10, "2. WhatsApp Automation: £750", ln=True)
    pdf.cell(0, 10, "3. Email Marketing Setup: £500", ln=True)

    # Save PDF to file
    pdf_file = "DM & Automations Services Pricing - Andrew 1.pdf"
    pdf.output(pdf_file)
    return pdf_file


def main():
    st.title("Customized PDF Generator")
    st.write("Enter your details below to generate a PDF.")

    # Input fields
    name = st.text_input("Name")
    date = st.date_input("Date")
    address = st.text_area("Address")
    phone = st.text_input("Phone Number")

    # Generate PDF button
    if st.button("Generate PDF"):
        if name and address and phone:
            pdf_path = create_pdf(name, str(date), address, phone)
            with open(pdf_path, "rb") as pdf_file:
                st.download_button(
                    label="Download PDF",
                    data=pdf_file,
                    file_name="Service_Proposal.pdf",
                    mime="application/pdf",
                )
        else:
            st.error("Please fill out all fields!")

if __name__ == "__main__":
    main()
