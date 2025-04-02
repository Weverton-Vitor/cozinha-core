
import pandas as pd
from infra import templates

# TODO Add pandas into dependencies

class CsvSystemStatsExporter(templates.interfaces.SystemStatsReportExporter):
    def preparar_dados(self, dados):
        self.df = pd.DataFrame(dados)

    def salvar_arquivo(self, caminho_arquivo):
        self.df.to_csv(caminho_arquivo, index=False)
