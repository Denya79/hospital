{
    'name': 'HR hospital',
    'summary': '',
    'author': 'Denys',
    'website': 'https://hr.hospital/',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.2.2.0',

    'depends': [
        'base',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [
        'security/ir.model.access.csv',

        'views/hr_hospital_menu.xml',
        'views/hr_hospital_doctor.xml',
        'views/hr_hospital_disease_types.xml',
        'views/hr_hospital_patient.xml',
        'views/hr_hospital_visits.xml',
        
        'data/hr.hospital.disease.types.csv'

    ],
    'demo': [
        'demo/hr_hospital_doctor.xml'
        'demo/hr.hospital.patient.csv'


    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],

}