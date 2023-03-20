# Copyright 2019-2020 Onestein (<https://www.onestein.eu>)
# Copyright 2019 BIG-Consulting GmbH(<http://www.openbig.org>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "German VAT Statement",
    "version": "13.0.1.0.1",
    "category": "Localization",
    "license": "AGPL-3",
    "author": "Onestein, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-germany",
    "depends": ["account", "date_range"],
    "data": [
        "security/ir.model.access.csv",
        "security/tax_statement_security_rule.xml",
        "data/paperformat.xml",
        "templates/assets.xml",
        "views/l10n_de_tax_statement_view.xml",
        "views/report_tax_statement.xml",
        "report/report_tax_statement.xml",
    ],
    "installable": True,
}
