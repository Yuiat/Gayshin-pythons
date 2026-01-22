import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generates a merged mod from several mod folders")
    args = parser.parse_args()
    png_files = collect_ini(args.root, args.name)
    print("\nFound:")
    for i, ini_file in enumerate(ini_files):
        print(f"\t{i}:  {ini_file}")
     
    # sets key to cycle forward
    key = 'r'
    name = 'fendo

    result = f"[Constants]\nglobal $speed = 0\nglobal $time = 0\nglobal $frame = 0\nglobal $active\nglobal $creditinfo = 0\n\n[KeySwap]\ncondition = $active == 1\nkey = {key}\ntype = cycle\n$frame = {','.join([str(x) for x in range(len(png_files))])}\n$creditinfo = 0\n\n[Present]\n\n[TextureOverride] //db27dec1 //dc29da79\nhash = 7df7cf79\nrun = CommandlistFrame\n$active = 1\n\n[TextureOverride1]\nhash = a75957d9\nrun = CommandlistFrame\n$active = 1\n\n[CommandlistFrame]"
    
    for i, png_file in enumerate(png_files):
        result += f"if $frame == {i}\n\tps-t0 = Resource{i+1}\nendif\n\n"
    for i, png_file in enumerate(png_files):
        result += f"[Resource{i+1}]\nfilename = {png_file}\n\n"
    with open(f"{name}.ini", "w", encoding="utf-8") as f:
        f.write(result)

# Collects all .ini files from current folder and subfolders
def collect_ini(path, ignore):
    ini_files = []
    for root, dir, files in os.walk(path):
        if "disabled" in root.lower():
            continue
        for file in files:
            if "disabled" in file.lower() or ignore.lower() in file.lower():
                continue
            if os.path.splitext(file)[1] == ".png":
                ini_files.append(os.path.join(root, file))
    return ini_files







    
if __name__ == "__main__":
    main()
