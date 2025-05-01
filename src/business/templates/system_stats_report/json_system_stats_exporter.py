import json
from business import templates

class JsonSystemStatsExporter(templates.ISystemStatsReportExporter):
    def preparar_dados(self, dados):
        self.dados_json = json.dumps(dados, indent=4)

    def salvar_arquivo(self, caminho_arquivo):
        with open(caminho_arquivo, "w") as f:
            f.write(self.dados_json)