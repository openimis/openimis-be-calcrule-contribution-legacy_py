CLASS_RULE_PARAM_VALIDATION = None

FROM_TO = [
        {"from": "Policy", "to": "Invoice"},
        {"from": "Contract", "to": "Invoice"}
]

DESCRIPTION_CONTRIBUTION_VALUATION = F"" \
    F"This calculation will, for the selected level and product," \
    F" calculate how much the insuree will have to" \
    F" pay based on the product modeling," \
    F" it will also manage the conversion into an invoice"
