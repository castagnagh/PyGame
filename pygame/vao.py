from vbo import VBO
from shader_program import ShaderProgram

class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        #dicionario de Vertex Array Objects para cada objeto
        #cubo vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])
        
        #cat vao
        self.vaos['cat'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cat'])
        
        #drag vao
        self.vaos['drag'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['drag'])
    
    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao
    
    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()