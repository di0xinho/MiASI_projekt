"This module contains helper functions for creating keyboards - lots of buttons."

from PySide6.QtWidgets import QPushButton, QGridLayout

class KeboardHelp:
    def __init__(self, keyboardGrid: QGridLayout, buttonMap: dict) -> None:
        self.keyboardGrid = keyboardGrid
        self.buttonMap = buttonMap
        pass
    def addButtonAtPos(self, text: str | None, col, row):
        "Add a button to keyboardGrid layout."
        if text is None: return
        self.buttonMap[text] = QPushButton(text)
        self.keyboardGrid.addWidget(self.buttonMap[text], row, col)
    def addButtons(self, buttTextList: list[str] | tuple[str], gridWidth, startAt=0):
        "gridWidth must not be 0"
        row = startAt // gridWidth
        col = startAt % gridWidth
        for buttonText in buttTextList:
            self.addButtonAtPos(buttonText, col, row)
            row += (col + 1) // gridWidth
            col = (col + 1) % gridWidth
        pass
    pass # class end

def inserter(insertTo: list, stuff: list[tuple]):
    "stuff - list of (index, object) pairs"
    for pair in stuff:
        insertTo.insert(pair[0], pair[1])
    return insertTo