from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.cell(210,10)
        self.set_font("helvetica", "B", 24)
        self.set_x(210 / 2)
        self.cell(
            2,
            9,
            "CS50 Shirtificate",
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )
        self.ln(10)


def main():
    pdf = PDF()
    pdf.set_margin(0)
    pdf.add_page()
    pdf.image("shirtificate.png", w = pdf.epw)
    pdf.output("test.pdf")

main()