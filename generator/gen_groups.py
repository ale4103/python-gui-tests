from comtypes.client import CreateObject
import os
import random

class GenGroups:
    def __init__(self, app):
        self.app = app

    def read_excel(self):
        project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        xl = CreateObject("Excel.application")
        xl.Workbooks.Open(os.path.join(project_dir, "groups.xlsx"))
        xl.Visible = True
        sheet = xl.Workbooks[1].Sheets["Лист1"]
        list = []
        for i in sheet.Range("A1", "A10"):
            list.append(i.Value())
        item = random.choice(list)
        xl.Quit()
        return item