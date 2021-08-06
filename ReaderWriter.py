class ReaderWriterDir:
    def __init__(self, directory, ext=".txt"):
        super().__init__()
        self.dir = directory
        self.ext = ext
    
    def getFile(self, index):
        return ReaderWriter(self.dir + str(index) + self.ext)
    
    def read(self, index, delim=""):
        return self.getFile(index).read(delim)

    def write(self, index, rows, delim=""):
        self.getFile(index).write(rows, delim)

    def readAll(self, indices, delim=""):
        indexToRows = dict()
        for index in indices:
            indexToRows[index] = self.read(index, delim)
        return indexToRows
    
    def writeAll(self, indexToRows, delim=""):
        for index, rows in indexToRows.items():
            self.write(index, rows, delim)

class ReaderWriter:
    def __init__(self, filename):
        super().__init__()
        self.filename = str(filename)
    
    def read(self, delim=""):
        file = open(self.filename)
        rows = list()
        for row in file:
            if row.endswith("\n"):
                row = row[:-1]
            if delim == "":
                rows.append(row)
            else:
                rows.append(row.split(delim))
        file.close()
        return rows

    def write(self, rows, delim=""):
        file = open(self.filename, "w")
        for row in rows:
            if delim == "":
                file.write(row + "\n")
            else:
                file.write(delim.join(row) + "\n")
        file.close()