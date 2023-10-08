from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def __innit__(self):
        self.image("shirtificate.png", w = self.pdf.epw)


    def header(self):
        self.set_font("helvetica", "B", 30)
        self.cell(30)
        # Printing title:
        self.cell(30, 10, "Title", align="C")




def main():
    pdf = PDF()
    pdf.add_page()


    pdf.set_title("CS50 Shirtificate")
    pdf.output("test.pdf")

main()