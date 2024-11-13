import numpy as np
import moderngl as mgl
import pywavefront

class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['cat'] = CatVBO(ctx)
        self.vbos['drag'] = DragVBO(ctx)
    
    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]

class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attrib: list = None
    
    def get_vertex_data(self): ...

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        #aqui um obj buffer é criado passando os vértices para a memória da GPU
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()

class CubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        #2f / 3f refere ao formato do buffer que passa 2 ou 3 valores para uma posição (x, y) ou (x, y, z)
        self.format = '2f 3f 3f'
        # a cordenada da textura, a cordenada da ... e cordenada de posição dos vértices
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    #metodo estático para gerar dados de vertices com base nos vertices e indices
    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        #array numpy do tipo float32. float32 = f4
        return np.array(data, dtype='f4')
    
    def get_vertex_data(self):
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]
        
        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        
        vertex_data = self.get_data(vertices, indices)

        #define a cordenada de uma face do cubo
        tex_coord = [(0, 0), (1, 0), (1, 1), (0, 1)]
        #informa os indices de cada triangulo que forma o cubo
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1),]
        #combina os dados de geometria e os dados de coordenadas de textura em uma matriz 
        tex_coord_data = self.get_data(tex_coord, tex_coord_indices)

        normals = [( 0, 0, 1) * 6,
                   ( 1, 0, 0) * 6,
                   ( 0, 0,-1) * 6,
                   (-1, 0, 0) * 6,
                   ( 0, 1, 0) * 6,
                   ( 0,-1, 0) * 6,]
        normals = np.array(normals, dtype='f4').reshape(36, 3)
        vertex_data = np.hstack([normals, vertex_data])

        vertex_data = np.hstack([tex_coord_data, vertex_data])

        return vertex_data
    
class CatVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('C:/Users/Gabriel Castagna/Documents/Projetos GitHub/PyGame/pygame/objects/cat/20430_Cat_v1_NEW.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class DragVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('C:/Users/Gabriel Castagna/Documents/Projetos GitHub/PyGame/pygame/objects/drag/StylizedDragon.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data