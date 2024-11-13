SEARCH_MW_BODY = {
    "request": {
        "waybill_number": [
            "{{iew_num}}"
        ]
    },
    "projection": {
        "waybill_number": 1,
        "state": 1,
        "created_at": 1,
        "shipper.name": 1,
        "shipper.pickup_address.region": 1,
        "shipper.pickup_address.address": 1,
        "shipper.pickup_address.country": 1,
        "shipper.pickup_address.city": 1,
        "shipper.pickup_address.street": 1,
        "shipper.pickup_address.zipcode": 1,
        "shipper.pickup_address.building": 1,
        "shipper.type": 1,
        "consignee.name": 1,
        "consignee.type": 1,
        "consignee.phone_num_main": 1,
        "consignee.email": 1,
        "consignee.delivery_address.country": 1,
        "consignee.delivery_address.city": 1,
        "consignee.delivery_address.building": 1,
        "consignee.delivery_address.street": 1,
        "consignee.delivery_address.zipcode": 1,
        "shipment_info.pcs_description": 1,
        "shipment_info.general_description": 1,
        "shipment_info.general_description_lat": 1,
        "references.num": 1,
        "references.type": 1,
        "references.description": 1,
        "references.data": 1,
        "reported_by_partner_code": 1,
        "payment": 1,
        "status": 1,
        "history": 1,
        "general_cost_info": 1,
        "invoices": 1,
        "references.partner_code": 1,
        "partner_code": 1,
        "shipper.phone_num_main": 1
    }
}

SEARCH_MW_BODY_PHONE = {
    "request": {
        "counterparty": {
            "phone_num_main": None
        },
        "state_in": [
            "Created",
            "Active",
            "Draft"
        ],
        "created_at_ge": "1726451882",
        "sort_by": "created_at",
        "sort_type": "0",
        "limit": "6",
        "offset": "0",
        "count_check": "1"
    }
}

SEARCH_NPS_BODY = {
    "company_id": "npi",
    "request": {
        "references": [
            {
                "num": None
            }
        ]
    },
    "limit": 50,
    "offset": 0,
    "count_check": 1
}
