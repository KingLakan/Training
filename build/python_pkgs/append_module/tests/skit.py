from os.path import exists

class apa:

    def __init__(self, mystring:str):
        pass
    @staticmethod
    def _dg(system_definition_path: str):
        print("Exists: ", exists(system_definition_path))
        print("EndsWith: ", system_definition_path.endswith('.nivssdf'))
        if not (exists(system_definition_path) and system_definition_path.endswith('.nivssdf')):
            print("its happening")
            raise FileNotFoundError
        else:
            print("condition doesnt work")

if __name__ == "__main__":
    #apa._dg(r"C:\Users\dsamuels\Documents\VeriStand Projects\Engine Demo 2\Engine Demo.nivssdf")
    apa._dg("")