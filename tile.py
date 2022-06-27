import pygame
from settings import *

class Tile(pygame.sprite.Sprite):           #roccia-- ma non solo!!!!
    def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):          #pos per dichiarare la posizione, groups indica il gruppo a cui appartiene
        super().__init__(groups)            #indispensabile per gli sprite
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == "object":
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE)) #per gli ogg più grandi
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10) #inflate prende un rect e ne cambia le dimensioni