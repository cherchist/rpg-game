import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon
from ui import UI

class Level:
    def __init__(self):
        
        #get the disp surf
        self.display_surface = pygame.display.get_surface() #prende la disp surf da qualunque punto del codice
        
        #sprite group setup
        self.visible_sprites = YSortCameraGroup() #va modificata in un Gruppo custom-made
        self.obstacle_sprites = pygame.sprite.Group()
        
        #attack sprites
        self.current_attack = None
        
        #sprite setup
        self.create_map()
        
        #user interface
        self.ui = UI()
        
    def create_map(self):
        layouts = {
            "boundary": import_csv_layout("map/map_FloorBlocks.csv"),
            "grass": import_csv_layout("map/map_Grass.csv"),
            "object": import_csv_layout("map/map_LargeObjects.csv"),
        }
        graphics = {
            'grass': import_folder("graphics/Grass"),
            "objects": import_folder("graphics/objects")
        }
        
        
        for style,layout in layouts.items():            #style: boundary. layout: mappa in csv
            for row_index,row in enumerate(layout):  #mi serve sapere l'index di ogni lista
                for col_index,col in enumerate(row):    #ora mi serve sapere l'index di ogni posizione della world map
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == "boundary":
                            Tile((x,y),[self.obstacle_sprites],"invisible")
                        if style == "grass":
                            random_grass_image = choice(graphics["grass"])
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],"grass",random_grass_image)
                            
                        if style == "object":
                            surf = graphics["objects"][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],"object",surf)
                            
        self.player = Player((2000,1430),[self.visible_sprites],self.obstacle_sprites,self.create_attack,self.destroy_attack)        
    
    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites])
    
    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None
    
    def run(self):
        #update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)
        
class YSortCameraGroup(pygame.sprite.Group): #camera! gli sprite vengono scelti secondo la coordinata y
    def __init__(self):
        
        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2 
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2() #va connesso al pg. andrebbe messo in mezzo allo schermo
        
        #il cazzo di pavimento
        self.floor_surf = pygame.image.load("graphics/tilemap/ground.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
        
    def custom_draw(self,player):
    
        #getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        #drawing the floor_rect
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)        
        
        #for sprite in self.sprites():              #qui ?? dove vienedrawato tutto. la mappa deve essere sotto tutto perch?? conta come pavimento
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery): #non ho capito un cazzo lol   
            offset_pos = sprite.rect.topleft - self.offset  
            self.display_surface.blit(sprite.image,offset_pos)
            
    '''
    bisogna ordinare gli sprite: dire alla classe quando disegnare lo specifico sprite
    '''