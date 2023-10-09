from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.set_x((210 - width) / 2)
        self.cell(
            2,
            9,
            self.title,
            border=1,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )
        self.ln(10)


def main():
    pdf = PDF()
    pdf.set_margin(0)
    pdf.add_page()
    pdf.set_title("CS50 Shirtificate")
    pdf.image("shirtificate.png", w = pdf.epw)
    pdf.output("test.pdf")

main()