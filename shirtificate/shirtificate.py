from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def __innit__(self):
        super().__innit__()


def main():
    pdf = PDF()
    pdf.set_margin(0)
    pdf.add_page()
    pdf.set_title("CS50 Shirtificate")
    pdf.image("shirtificate.png", w = pdf.epw)

    pdf.output("test.pdf")

main()