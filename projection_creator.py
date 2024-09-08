import open3d as o3d
import numpy as np
import time

mesh = o3d.io.read_triangle_mesh('trial.stl')
angle = 0.0

# init
vis = o3d.visualization.Visualizer()
vis.create_window(window_name="STL", left=1000, top=200, width=1280, height=720)
vis.add_geometry(mesh)
height = 0.0
frame_count = 0

# init camera
ctr = vis.get_view_control()
ctr.set_zoom(1)

# those are angles , or angle steps. camera moves downwards (height), while object is rotating
angle_increment = 0.0341
height_increment = 0.341
# radius=25
while height < np.pi/2:
    angle = 0.0  
    while angle < 2 * np.pi:
        mesh.compute_vertex_normals()
        
        # Rotation of stl
        rotation_matrix = mesh.get_rotation_matrix_from_xyz((0, 0, angle))
        rotated_mesh = mesh.rotate(rotation_matrix, center=(0, 0, 0))
        # camera down!
        ctr.rotate(height, 0, 0)
        
        vis.update_geometry(mesh)
        vis.poll_events()
        vis.update_renderer()
        
        # Save projection as jpg
        vis.capture_screen_image(f'frame_{frame_count}.jpg')
        frame_count += 1
        
        
        angle += angle_increment  
    height += height_increment

# close the window
vis.destroy_window()
