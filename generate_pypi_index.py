import os
import sys


def generate_pypi_index(folder_path):
    with open(os.path.join(folder_path, "index.html"), "w") as index_file:
        index_file.write(
            "<!DOCTYPE html>\n<html>\n  <head>\n    <title>Package Index</title>\n  </head>\n  <body>\n"
        )
        index_file.write("    <h1>Package Index</h1>\n    <ul>\n")

        wheel_files = [f for f in os.listdir(folder_path) if f.endswith(".whl")]
        for wheel_file in wheel_files:
            link = f'      <li><a href="{wheel_file}">{wheel_file}</a></li>\n'
            index_file.write(link)

        index_file.write("    </ul>\n  </body>\n</html>\n")


if __name__ == "__main__":
    wheel_folder_path = sys.argv[1]
    generate_pypi_index(wheel_folder_path)
