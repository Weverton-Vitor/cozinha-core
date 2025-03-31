from abc import ABC, abstractmethod

class ReportExporter(ABC):
    def exportar(self, dados, caminho_arquivo):
        self.preparar_dados(dados)
        self.salvar_arquivo(caminho_arquivo)
        print(f"Relatório salvo em {caminho_arquivo}")

    @abstractmethod
    def preparar_dados(self, dados):
        pass

    @abstractmethod
    def salvar_arquivo(self, caminho_arquivo):
        pass
