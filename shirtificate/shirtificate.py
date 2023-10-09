from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 36)
        self.set_x(210 / 2)
        self.cell(
            1,
            30,
            "CS50 Shirtificate",
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )
        self.ln(10)
    def footer(self):
        



def main():
    pdf = PDF()
    pdf.set_margin(0)
    pdf.add_page()
    pdf.image("shirtificate.png", w = pdf.epw)
    pdf.output("test.pdf")

main()