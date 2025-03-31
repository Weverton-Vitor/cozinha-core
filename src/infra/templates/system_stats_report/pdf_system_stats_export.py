from fpdf import FPDF
from infra import templates

# TODO Add fpdf into dependencies

class PdfSystemStatsExporter(templates.interfaces.ReportExporter):
    def preparar_dados(self, dados):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        for linha in dados:
            self.pdf.cell(200, 10, txt=str(linha), ln=True)

    def salvar_arquivo(self, caminho_arquivo):
        self.pdf.output(caminho_arquivo)
