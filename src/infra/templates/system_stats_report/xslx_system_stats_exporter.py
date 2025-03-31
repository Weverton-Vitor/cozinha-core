import pandas as pd
from infra import templates

# TODO Add pandas into dependencies

class XlsxSystemStatsExporter(templates.interfaces.SystemStatsReportExporter):
    def preparar_dados(self, dados):
        self.df = pd.DataFrame(dados)

    def salvar_arquivo(self, caminho_arquivo):
        self.df.to_excel(caminho_arquivo, index=False)