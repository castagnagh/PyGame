import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene

class GraphicsEngine:
    #metodo para converter os valores do tamanho da tela para o opengl
    def __init__(self, win_size=(1600, 900)):
        #iniciando os modulos do pygame
        pg.init()
        #tamanho da janela
        self.WIN_SIZE = win_size
        #setar atributos opengl especificando qual a mior e menor versão a ser utilizada
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        #seta um perfil para dizer que não usara a versão obsoleta
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        #criando um contexto opengl
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        #configurações do mouse para não passar da tela e para deixar invisivel
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        #detecta e usa contexto opengl existente
        self.ctx = mgl.create_context()
        #ativando o teste de profundidade (para não exibir as faces do fundo) | e cull face para não renderizar as fases do fundo 
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        #self.ctx.front_face = 'cw'
        #cria um objeto para definir a taxa de atualização de quadros
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        #light
        self.light = Light()
        #camera
        self.camera = Camera(self)
        #mesh
        self.mesh = Mesh(self)
        #criando uma instancia da classe triangulo para renderizção
        self.scene = Scene(self)
       
    
    #evendo para monitorar a tecla de ESC e Fechar a janela
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()
    
    #metodo para limpar o buffer de tela e definir uma cor de fundo
    def render(self):
        #limpando o buffer e setando a cor
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        self.scene.render()
        #trocando o buffer
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001
    
    #metodo principal para rodar a aplicação
    def run(self):
        #while para verificar os metodos acima de eventos, renderizaçaõ e atualização de quadro
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            #definindo 60 quadros por segundo
            self.delta_time = self.clock.tick(60)
    
if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()