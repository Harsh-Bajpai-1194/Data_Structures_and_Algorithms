class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = rows
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split('+')
        return self._getOperandValue(x) + self._getOperandValue(y)

    def _getOperandValue(self, operand: str) -> int:
        if operand[0].isalpha():
            return self.cells.get(operand, 0)
        return int(operand)

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)