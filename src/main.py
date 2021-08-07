from brango import *
fileName = "src\Berke.js"
fileWritecommand = "a"
Brango(fileName, fileWritecommand).CreateFile()
Brango(fileName, fileWritecommand).WriteFile("dd = document.getElementById('Berke');")
Brango(fileName, fileWritecommand).FindIdElement("bb", "Berke")
Brango(fileName, fileWritecommand).FindIdWrite("sg", "Berke", "MERHABA DÜNYA")