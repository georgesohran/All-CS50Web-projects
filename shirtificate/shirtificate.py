from fpdf import FPDF
from PIL import ImageOps

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)

        # Moving cursor to the right:
        self.cell(30)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


def main():
    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png", 105, 0, 80)
    pdf.set_title("CS50 Shirtificate")
    pdf.output("test.pdf")

main()