import pandas as pd
from business import templates

# TODO Add pandas into dependencies

class XlsxSystemStatsExporter(templates.ISystemStatsReportExporter):
    def preparar_dados(self, dados):
        self.df = pd.DataFrame(dados)

    def salvar_arquivo(self, caminho_arquivo):
        self.df.to_excel(caminho_arquivo, index=False)