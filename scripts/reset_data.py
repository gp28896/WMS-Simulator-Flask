import os
from app.config import CSV_DIR, JSON_DIR


def reset_files():

	for folder in [CSV_DIR ,JSON_DIR]:
		for file in os.listdir(folder):
			path = os.path.join(folder, file)
			
			with open(path, "w") as f:
				if file.endswith(".json"):
					f.write("[]")
				else:
					f.write("")


if __name__ == "__main__":
	reset_files()
	print("Data reset completed successfully")	
