from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
        
def import_folder(path):
    surface_list = []
    
    for _,__,img_files in walk(path): #importa le immagini di una cartella
        for image in img_files: #dà il percorso, una lista vuota e una lista con i file presenti nella cartella
            full_path = path + "/" + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    
    return surface_list   
