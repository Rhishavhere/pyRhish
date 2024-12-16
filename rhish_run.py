import sys
from interpreter import RhishInterpreter

def run_rhish(file_path):
  with open(file_path,"r") as file:
    rhish_code=file.read()

  interpreter = RhishInterpreter()
  # print(f"Running Rhish file: {file_path}")
  interpreter.execute(rhish_code)

if len(sys.argv) < 2:
  print("Usage: python rhish_run.py <path_to_file.rsv>")
else:
  file_path = sys.argv[1]
  run_rhish(file_path)