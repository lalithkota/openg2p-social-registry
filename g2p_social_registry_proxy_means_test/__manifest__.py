# Part of OpenG2P. See LICENSE file for full copyright and licensing details.
{
    "name": "G2P Social Registry: PMT",
    "category": "G2P",
    "version": "17.0.0.0.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "LGPL-3",
    "depends": ["base", "web", "g2p_registry_base", "g2p_social_registry"],
    "data": [
        "security/ir.model.access.csv",
        "views/pmt_config_view.xml",
        "views/individual_view.xml",
        "views/group_view.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
