class ZipCode:
    mainCity = ""
    code = ""
    
    def __init__(self, mainCity, code):
        self.mainCity = mainCity
        self.code=code

myZipCode = ZipCode('Brooklyn','11238')
cuspZipCode = ZipCode('Brooklyn','11201')
