from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    text_hight = 30
    def header(self):
        self.set_font("helvetica", "B", 36)
        self.set_x(210 / 2)
        self.cell(
            1,
            self.text_hight,
            "CS50 Shirtificate",
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )
        self.ln(10)

    def render_text(self,txt):
        self.image("shirtificate.png", w = self.epw)
        self.set_font("helvetica", "B", 20)
        self.set_text_color(255,255,255)
        self.text((210 - self.get_string_width(f"{txt} took CS50"))/2, self.text_hight*3, f"{txt} took CS50")




def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.set_margin(0)
    pdf.add_page()
    pdf.render_text(name)
    pdf.output("shirtificate.pdf")

main()