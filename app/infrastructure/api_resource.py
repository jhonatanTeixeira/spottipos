from flask import request
from flask_restplus import Api, Resource, fields
from app.domain.model import Property, Area
from flask import Flask
import container

app = Flask(__name__)
api = Api(app, version='0.1', title='Manage properties on Spottipos',
          description='Registre e pesquise informações sobre imóveis mais badalados em Spottipos =)')

ns = api.namespace('Spottipos', description='restful endpoints')

property_model = api.model('property', {
    'id': fields.Integer(readonly=True),
    'x': fields.Integer(),
    'y': fields.Integer(),
    'title': fields.String(),
    'price': fields.Integer(),
    'description': fields.String(),
    'beds': fields.Integer(),
    'baths': fields.Integer(),
    'squareMeters': fields.Integer(),
    'provinces': fields.List(cls_or_instance=fields.String(), readonly=True),
})

property_model_list = api.model('properties', {
    'totalProperties': fields.Integer(),
    'properties': fields.List(cls_or_instance=fields.Nested(property_model))
})


@ns.route('/properties')
class PropertyResource(Resource):
    @ns.doc('post_property')
    @ns.marshal_with(property_model)
    @ns.expect(property_model)
    def post(self):
        "register a Spotippos property"
        try:
            property = Property(**api.payload)
            container.world_service.add_property(property)
        except ValueError as error:
            return 400, str(error)

        return property

    @ns.doc('get_properties', params={
        'ax': 'upper left x',
        'ay': 'upper left y',
        'bx': 'bottom right x',
        'by': 'bottom right y',
    })
    @ns.marshal_with(property_model_list)
    def get(self):
        "get a property list filtered by the specified area"
        try:
            area = Area(int(request.args['ax']), int(request.args['ay']), int(request.args['bx']),
                        int(request.args['by']))
        except TypeError as error:
            return 400, str(error)

        properties = container.world_service.get_properties(area)

        return {
            'totalProperties': len(properties),
            'properties': properties
        }


@ns.route('/properties/<id>')
class FornecedorItemResource(Resource):
    """property"""
    @ns.doc('get_property')
    @ns.marshal_with(property_model)
    def get(self, id: int):
        """returns a property by its id"""
        return container.world_service.get_property_by_id(id)
