from model import *

#classe criada para centralizar todos os objetos e componentes criados
#necessitando apenas chamar essa classe no init da class Main
class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object
        
        #add (Cube(app))
        #tex_id é o ID da textura, pos é a posição no plano, rot é a rotação e scale o "espichamento"
        #add (Cube(app, tex_id=1, pos=(-2.5, 0, 0), rot=(45, 0, 0), scale=(1, 2, 1)))
        #add (Cube(app, tex_id=2, pos=(2.5, 0, 0), rot=(0, 0, 45), scale=(1, 1, 2)))
    
        n, s, = 30, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

        #add(Cat(app, pos=(10, -1, -10), rot=(-90, 0, 180)))
        add(Drag(app, pos=(0, 5, -10)))

    def render (self):
        for obj in self.objects:
            obj.render()