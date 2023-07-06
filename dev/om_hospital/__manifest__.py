{
    "name": "Hospital Management System",
    "author": "Viper",
    "summary": "Hospital patient management app",
    "version": "1.0.0",
    "depends": ["mail"],
    "installable": True,
    "application": True,
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/menu.xml",
        "views/patient.xml"
    ]

}