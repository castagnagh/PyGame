import os

class ShaderProgram:
    def __init__(self, ctx):
        self.ctx = ctx
        self.programs = {}
        self.programs['default'] = self.get_program('default')

    def get_program(self, shader_program_name) :
        base_path = os.path.dirname(__file__)

        # Construa o caminho completo para os arquivos de shader
        vertex_shader_path = os.path.join(base_path, 'shaders', f'{shader_program_name}.vert')
        fragment_shader_path = os.path.join(base_path, 'shaders', f'{shader_program_name}.frag')

        # Verifique os caminhos para depuração
        print(f"Vertex Shader Path: {vertex_shader_path}")
        print(f"Fragment Shader Path: {fragment_shader_path}")

        # Abra e leia os arquivos de shader
        with open(vertex_shader_path) as file:
            vertex_shader = file.read()

        with open(fragment_shader_path) as file:
            fragment_shader = file.read()

        # Crie o programa do shader
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    def destroy(self):
        [program.release() for program in self.programs.values()]