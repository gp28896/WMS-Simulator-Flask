import csv
from typing import List, Dict

class CSVRepository:
    def __init__(self, file_path: str, fieldnames: List[str]):
        self.file_path = file_path
        self.fieldnames = fieldnames

    def read_all(self) -> List[Dict]:
        try:
            with open(self.file_path, "r", newline="") as f:
                return list(csv.DictReader(f))
        except:
            return []

    def write_all(self, rows: List[Dict]):
        with open(self.file_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def append(self, row: Dict):
        rows = self.read_all()
        rows.append(row)
        self.write_all(rows)