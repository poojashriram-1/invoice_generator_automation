import csv
import os
from fpdf import FPDF
from datetime import datetime

os.makedirs("invoices", exist_ok=True)


class InvoicePDF(FPDF):

    def header(self):

        self.set_font("Arial", "B", 20)
        self.cell(0, 10, "ABC CORPORATION", ln=True, align="C")

        self.set_font("Arial", "", 12)
        self.cell(0, 10, "Professional Invoice", ln=True, align="C")

        self.ln(10)


def generate_invoice(name, email, hours, rate, invoice_no):

    amount = float(hours) * float(rate)

    pdf = InvoicePDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    date = datetime.now().strftime("%d-%m-%Y")

    pdf.cell(100, 10, f"Invoice Number: {invoice_no}", ln=True)
    pdf.cell(100, 10, f"Invoice Date: {date}", ln=True)

    pdf.ln(10)

    pdf.cell(100, 10, f"Customer Name: {name}", ln=True)
    pdf.cell(100, 10, f"Email: {email}", ln=True)

    pdf.ln(10)

    # Table Header
    pdf.set_font("Arial", "B", 12)

    pdf.cell(40, 10, "Item", 1)
    pdf.cell(40, 10, "Hours", 1)
    pdf.cell(40, 10, "Rate", 1)
    pdf.cell(40, 10, "Amount", 1)
    pdf.ln()

    pdf.set_font("Arial", "", 12)

    pdf.cell(40, 10, "Work Service", 1)
    pdf.cell(40, 10, hours, 1)
    pdf.cell(40, 10, f"{rate}", 1)
    pdf.cell(40, 10, f"{amount}", 1)
    pdf.ln()

    pdf.ln(10)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(120, 10, "Total", 1)
    pdf.cell(40, 10, f"{amount}", 1)

    filename = f"invoices/{name.replace(' ','_')}.pdf"

    pdf.output(filename)

    print("Invoice created:", filename)


with open("data/clients.csv") as file:

    reader = csv.DictReader(file)

    invoice_no = 1001

    for row in reader:

        generate_invoice(
            row["name"],
            row["email"],
            row["hours"],
            row["rate"],
            invoice_no
        )

        invoice_no += 1