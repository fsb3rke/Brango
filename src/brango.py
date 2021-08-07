class Brango():
    def __init__(self, JAVASCRIPT_FILE_NAME:str, FILE_WRITE_COMMAND:str):
        self.fileName = JAVASCRIPT_FILE_NAME
        self.fileWritecommand = FILE_WRITE_COMMAND
    def CreateFile(self):
        file = open(self.fileName, self.fileWritecommand)
        file.close()
    def WriteFile(self, JAVASCRIPT_CODE:str):
        with open(self.fileName, self.fileWritecommand) as file:
            file.write(JAVASCRIPT_CODE+"\n")
            file.close()
    def FindIdElement(self, VARIABLE_NAME:str, ID_NAME:str):
        with open(self.fileName, self.fileWritecommand) as file2:
            file2.write(f"{VARIABLE_NAME} = document.getElementById('{ID_NAME}');\n")
            file2.close()