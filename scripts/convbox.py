import sys
import mandoline
import re

def parse_gcode(file_path):
    # Regular expression to match G-code coordinates
    line_pattern = re.compile(r'^G.*')
    coord_pattern = re.compile(r'([XYZ])([-+]?\d*\.?\d+)')
    
    # Initialize min and max values for bounding box
    min_x = min_y = min_z = float('inf')
    max_x = max_y = max_z = float('-inf')
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[50:-100]:
            # Find all coordinates in the line
            coords = coord_pattern.findall(line)
            if coords:
                for axis, value in coords:
                    value = float(value)
                    if axis == 'X':
                        min_x = min(min_x, value)
                        max_x = max(max_x, value)
                    elif axis == 'Y':
                        min_y = min(min_y, value)
                        max_y = max(max_y, value)
                    elif axis == 'Z':
                        min_z = min(min_z, value)
                        max_z = max(max_z, value)
    
    bounding_box = {
        'min_x': min_x,
        'max_x': max_x,
        'min_y': min_y,
        'max_y': max_y,
        'min_z': min_z,
        'max_z': max_z,
        'width': max_x - min_x,
        'depth': max_y - min_y,
        'height': max_z - min_z
    }
    
    return bounding_box

sys.argv = ['convert.py', '-o', 'cube.gcode', 'cube.stl']

mandoline.main()

file_path = 'cube.gcode'
bounding_box = parse_gcode(file_path)

print("Bounding Box Dimensions:")
print(f"Width (X): {bounding_box['width']}")
print(f"Depth (Y): {bounding_box['depth']}")
print(f"Height (Z): {bounding_box['height']}")

