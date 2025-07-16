{
    "name": "MRP Process Costing",
    "summary": "Calculate material, labor, and overhead cost for manufacturing orders.",
    "description": """
        Real-time process costing for Manufacturing Orders and Work Orders.
        - Estimate cost from BOM.
        - Calculate actual cost based on material usage and time logs.
        - Compare estimated and actual costs.
        - Support for labor and overhead costing per work center.
    """,
    "category": "Manufacturing",
    "depends": ["mrp", "stock"],
    "data": [
        "security/ir.model.access.csv",
        'report/mrp_costing_report_action.xml',
        "views/mrp_production_views.xml",
        "views/mrp_workcenter_views.xml",
        "report/mrp_costing_report.xml",
    ],
    "installable": True,
    "application": False,
}
