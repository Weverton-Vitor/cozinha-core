
import pandas as pd
from business import templates

# TODO Add pandas into dependencies

class CsvSystemStatsExporter(templates.ISystemStatsReportExporter):
    def preparar_dados(self, dados):
        self.df = pd.DataFrame(dados)

    def salvar_arquivo(self, caminho_arquivo):
        self.df.to_csv(caminho_arquivo, index=False)
