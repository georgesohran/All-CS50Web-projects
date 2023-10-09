from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def __innit__(self):
        super().__innit__()

    def header(self):
        self.set_font("helvetica", "B", 30)
        self.cell(30)
        self.cell(30, 10, "Title", align="C")



def main():
    pdf = PDF(orientation="landscape")
    pdf.set_margin(0)
    pdf.add_page()
    pdf.image("shirtificate.png",h = pdf.eph, w = pdf.epw)

    pdf.output("test.pdf")

main()