"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    # Build Person model from person.ent file
    database_model = entity_mm.model_from_file(join(this_folder, 'tablatest.ent'))

    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in database_model.entities:
            return True
        else:
            return False

    def sqltype(s):
        """
        Maps type names from PrimitiveType to SQL.
        """
        return {
                'integer': 'bigint',
                'string': 'varchar(?)',
                'fecha' : 'date'
        }.get(s.name, s.name)

    # Create output folder
    sqlgen_folder = join(this_folder, 'sqlGenerado')
    if not exists(sqlgen_folder):
        mkdir(sqlgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to SQL type names.

    jinja_env.tests['entity'] = is_entity

    jinja_env.filters['sqltype'] = sqltype

    # Load tabla template
    template = jinja_env.get_template('tabla.template')

    folder = join(sqlgen_folder, "Tablas")        
    if not exists(folder):
        mkdir(folder)

    for entity in database_model.entities:
        # For each entity generate sql file
        with open(join(folder,
                       "%s.sql" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

    # Load consulta template
    template = jinja_env.get_template('consulta.template')

    folder = join(sqlgen_folder, "Consultas")        
    if not exists(folder):
        mkdir(folder)

    for entity in database_model.entities:
        # For each entity generate sql file 
        with open(join(folder,
                       "consulta%s.sql" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

    # Load consulta template
    template = jinja_env.get_template('actualiza.template')

    folder = join(sqlgen_folder, "Actualizar")        
    if not exists(folder):
        mkdir(folder)

    for entity in database_model.entities:
        # For each entity generate sql file 
        with open(join(folder,
                       "actualiza%s.sql" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

    # Load consulta template
    template = jinja_env.get_template('inserta.template')

    folder = join(sqlgen_folder, "Insertar")        
    if not exists(folder):
        mkdir(folder)

    for entity in database_model.entities:
        # For each entity generate sql file 
        with open(join(folder,
                       "insterta%s.sql" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

    # Load consulta template
    template = jinja_env.get_template('alterar.template')

    folder = join(sqlgen_folder, "Alterar")        
    if not exists(folder):
        mkdir(folder)

    for entity in database_model.entities:
        # For each entity generate sql file 
        with open(join(folder,
                       "altera%s.sql" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))
"""

    # Load template
    template = jinja_env.get_template('editar.template')

    for entity in person_model.entities:
        # For each entity generate html file
        with open(join(srcgen_folder,
                       "editar%s.html" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

    # Load template
    template = jinja_env.get_template('agregarCtrl.template')

    for entity in person_model.entities:
        # For each entity generate js file
        with open(join(srcgen_folder,
                       "agregar%s.js" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))
            """

if __name__ == "__main__":
    main()