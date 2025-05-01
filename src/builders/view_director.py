from builders.view_builder import IViewBuilder

class ViewDirector:
    __builder: IViewBuilder

    def __init__(self, builder: IViewBuilder):
        self.__builder = builder

    def set_builder(self, builder: IViewBuilder):
        self.__builder = builder

    def make(self):
        self.__builder.build_DAO()
        self.__builder.build_validators()

        self.__builder.build_repository()
        self.__builder.build_service()
        self.__builder.build_controller()

        self.__builder.build_view()
