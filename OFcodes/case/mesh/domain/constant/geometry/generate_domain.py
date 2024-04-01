import sys

def write_stl_file(filename, solids):
    with open(filename, 'w') as file:
        for solid, triangles in solids.items():
            file.write(f"solid {solid}\n")
            for triangle in triangles:
                normal = calculate_normal(triangle[0], triangle[1], triangle[2])
                file.write(f"  facet normal {normal[0]} {normal[1]} {normal[2]}\n")
                file.write("    outer loop\n")
                for vertex in triangle:
                    file.write(f"      vertex {vertex[0]} {vertex[1]} {vertex[2]}\n")
                file.write("    endloop\n")
                file.write("  endfacet\n")
            file.write("endsolid\n")

def calculate_normal(vertex1, vertex2, vertex3):
    # Calculate the normal vector of a triangle given its vertices
    # Cross product of two vectors: (vertex2 - vertex1) x (vertex3 - vertex1)
    x = (vertex2[1] - vertex1[1]) * (vertex3[2] - vertex1[2]) - (vertex2[2] - vertex1[2]) * (vertex3[1] - vertex1[1])
    y = (vertex2[2] - vertex1[2]) * (vertex3[0] - vertex1[0]) - (vertex2[0] - vertex1[0]) * (vertex3[2] - vertex1[2])
    z = (vertex2[0] - vertex1[0]) * (vertex3[1] - vertex1[1]) - (vertex2[1] - vertex1[1]) * (vertex3[0] - vertex1[0])
    magnitude = (x**2 + y**2 + z**2)**0.5

    return x / magnitude, y / magnitude, z / magnitude

def generate_solid(surface, x_min, x_max, y_min, y_max, z_min, z_max):
    vertices = [
        (x_min, y_min, z_min),  # Vertex 0
        (x_max, y_min, z_min),  # Vertex 1
        (x_max, y_max, z_min),  # Vertex 2
        (x_min, y_max, z_min),  # Vertex 3
        (x_min, y_min, z_max),  # Vertex 4
        (x_max, y_min, z_max),  # Vertex 5
        (x_max, y_max, z_max),  # Vertex 6
        (x_min, y_max, z_max)   # Vertex 7
    ]

    if surface == 'xMin':
        triangles = [
            (vertices[0], vertices[3], vertices[7]),  # Triangle 1
            (vertices[0], vertices[7], vertices[4]),  # Triangle 2
        ]
    elif surface == 'xMax':
        triangles = [
            (vertices[1], vertices[5], vertices[6]),  # Triangle 1
            (vertices[1], vertices[6], vertices[2]),  # Triangle 2
        ]
    elif surface == 'yMin':
        triangles = [
            (vertices[0], vertices[1], vertices[5]),  # Triangle 1
            (vertices[0], vertices[5], vertices[4]),  # Triangle 2
        ]
    elif surface == 'yMax':
        triangles = [
            (vertices[2], vertices[6], vertices[7]),  # Triangle 1
            (vertices[2], vertices[7], vertices[3]),  # Triangle 2
        ]
    elif surface == 'zMin':
        triangles = [
            (vertices[0], vertices[2], vertices[1]),  # Triangle 1
            (vertices[0], vertices[3], vertices[2]),  # Triangle 2
        ]
    elif surface == 'zMax':
        triangles = [
            (vertices[4], vertices[6], vertices[5]),  # Triangle 1
            (vertices[4], vertices[7], vertices[6]),  # Triangle 2
        ]
    else:
        raise ValueError('Invalid surface')

    return triangles

# Get the command-line arguments
args = sys.argv[1:]

# Check if the correct number of arguments is provided
if len(args) != 7:
    print("Usage: python3 generate_domain.py filename xMin xMax yMin yMax zMin zMax")
    sys.exit(1)

# Parse the arguments
filename = args[0]
x_min, x_max, y_min, y_max, z_min, z_max = map(float, args[1:])

# Generate the solids for each surface
solids = {
    'xMin': generate_solid('xMin', x_min, x_min, y_min, y_max, z_min, z_max),
    'xMax': generate_solid('xMax', x_max, x_max, y_min, y_max, z_min, z_max),
    'yMin': generate_solid('yMin', x_min, x_max, y_min, y_min, z_min, z_max),
    'yMax': generate_solid('yMax', x_min, x_max, y_max, y_max, z_min, z_max),
    'zMin': generate_solid('zMin', x_min, x_max, y_min, y_max, z_min, z_min),
    'zMax': generate_solid('zMax', x_min, x_max, y_min, y_max, z_max, z_max)
}

# Write the STL file
write_stl_file(filename, solids)
