TOP_NPI_BODY = {
    "request": {
        "api_order":
            "TOP00000001111111124NPI",
        "references": [
            {
                "num": "TOP00000001111111124NGUS",
                "type": "Waybill number",
                "partner_code": 12
            }
        ],
        "shipper": {
            "pickup_address": {
                "address_type": "Door",
                "region": "Kyivska oblast",
                "country": "UA",
                "city": "Kyiv",
                "street": "Stolychne shose",
                "zipcode": "03026",
                "address": "Kyiv, Stolychne shose 2"
            },
            "name": "HappyChan Global",
            "email": "test@wp.pl",
            "type": "Legal entity",
            "phone_num_main": "380682679343"
        },
        "consignee": {
            "delivery_address": {
                "address_type": "Door",
                "country": "PL",
                "region": "Białystok",
                "city": "Białystok",
                "street": "Mieszka I",
                "zipcode": "15-054",
                "address": "Białystok, Mieszka I 2"
            },
            "name": "Walc Magdalena",
            "type": "Private person",
            "phone_num_main": "48534012345",
            "email": "test@wp.pl"
        },
        "payment": {
            "service": {
                "delivery_type": "WarehouseDoor",
                "name": "E-commerce Standard",
                "payer_type": "Third party",
                "payment_type": "Cashless"
            },
            "additional_services": [
                {
                    "id": "1",
                    "currency": "UAH",
                    "cost": "100",
                    "domestic_currency": "UAH",
                    "domestic_currency_cost": "100",
                    "service_paid": None,
                    "service_paid_at": None,
                    "service_payment_type": None,
                    "service_provided": None,
                    "service_provided_at": None,
                    "description": None,
                    "comment": None,
                    "payer_counterparty": {
                        "name": "Walc Magdalena",
                        "type": "Private person",
                        "code": None,
                        "public_legal_registry_code": None,
                        "residency": None,
                        "account_no": None,
                        "contact_person_name": None,
                        "contact_person_surname": None,
                        "phone_num_main": None,
                        "initial_phone_num": None,
                        "additional_phone_nums": None,
                        "email": None,
                        "address": {
                            "country": None,
                            "country_name": None,
                            "state": None,
                            "region": None,
                            "county": None,
                            "city": None,
                            "district": None,
                            "address": None,
                            "street": None,
                            "building": None,
                            "apt": None,
                            "zipcode": None,
                            "latitude": None,
                            "longitude": None,
                            "lang": None,
                            "channel": None,
                            "comments": None
                        },
                        "service_data": {
                            "master_system_id": None,
                            "master_id": None
                        }
                    },
                    "partner_code": "12",
                    "partner_name": "Nova Global US Inc",
                    "name": "TOP",
                    "key": "26",
                    "payer_type": "Consignee",
                    "payment_type": "Cashless"
                }
            ]
        },
        "shipment_info": {
            "pcs_description": [
                {
                    "id": "1",
                    "index": "1",
                    "length": "10",
                    "width": "10",
                    "height": "10",
                    "actual_weight": "0.26",
                    "volume_weight": "0.2",
                    "control_length": None,
                    "control_width": None,
                    "control_height": None,
                    "control_actual_weight": None,
                    "control_volume_weight": "0",
                    "barcode": "TOP0000000111111209NGUS",
                    "description": None,
                    "pack_num": "TOP0000000111111209NGUS",
                    "volume": "0.001",
                    "control_volume": "0",
                    "parcel_type": None,
                    "status": None
                }
            ]
        },
        "invoices": [
            {
                "currency": "GBP",
                "incoterms": "EXW",
                "invoice_details": [
                    {
                        "customs_code": "6404110000",
                        "material": "Artificial fabrics handmade",
                        "description": "Shoes - polyurethane",
                        "quantity": 1,
                        "units": "package",
                        "cost_per_unit": 100,
                        "subtotal_cost_per_good": 100,
                        "origin": "GB"
                    }
                ]
            }
        ],
        "general_cost_info": {
            "declared_cost": "19.8",
            "declared_currency": "USD",
            "cost": None,
            "currency": None,
            "domestic_currency_cost": None,
            "domestic_currency": None,
            "discount_code": None,
            "discount_value": None,
            "promo_code": None,
            "cod": {
                "amount": None,
                "domestic_currency_amount": None,
                "currency": None,
                "counterparty": {
                    "name": None,
                    "type": None,
                    "code": None,
                    "public_legal_registry_code": None,
                    "residency": None,
                    "account_no": None,
                    "contact_person_name": None,
                    "contact_person_surname": None,
                    "phone_num_main": None,
                    "initial_phone_num": None,
                    "email": None,
                    "address": {
                        "country": None,
                        "country_name": None,
                        "state": None,
                        "region": None,
                        "county": None,
                        "city": None,
                        "district": None,
                        "address": None,
                        "street": None,
                        "building": None,
                        "apt": None,
                        "zipcode": None,
                        "latitude": None,
                        "longitude": None,
                        "lang": None,
                        "channel": None,
                        "comments": None
                    },
                    "service_data": {
                        "master_system_id": None,
                        "master_id": None
                    },
                    "additional_phone_nums": [
                        None
                    ]
                }
            }
        }
    }
}

TOP_NGUS_BODY = {
    "request": {
        "api_order":
            "TOP00000001111111124NGUS",
        "references": [
            {
                "num": "TOP00000001111111124NGUS",
                "type": "Waybill number",
                "partner_code": 238
            }
        ],
        "shipper": {
            "pickup_address": {
                "address_type": "Door",
                "region": "Kyivska oblast",
                "country": "UA",
                "city": "Kyiv",
                "street": "Stolychne shose",
                "zipcode": "03026",
                "address": "Kyiv, Stolychne shose 2"
            },
            "name": "HappyChan Global",
            "email": "test@wp.pl",
            "type": "Legal entity",
            "phone_num_main": "380682679343"
        },
        "consignee": {
            "delivery_address": {
                "address_type": "Door",
                "country": "PL",
                "region": "Białystok",
                "city": "Białystok",
                "street": "Mieszka I",
                "zipcode": "15-054",
                "address": "Białystok, Mieszka I 2"
            },
            "name": "Walc Magdalena",
            "contact_person_name": "Magdalena",
            "contact_person_surname": "Walc",
            "type": "Private person",
            "phone_num_main": "48534012345",
            "email": "test@wp.pl"
        },
        "payment": {
            "service": {
                "delivery_type": "WarehouseDoor",
                "name": "E-commerce Standard",
                "payer_type": "Third party",
                "payment_type": "Cashless"
            },
            "additional_services": [
                {
                    "id": "1",
                    "currency": "UAH",
                    "cost": "100",
                    "domestic_currency": "UAH",
                    "domestic_currency_cost": "100",
                    "service_paid": None,
                    "service_paid_at": None,
                    "service_payment_type": None,
                    "service_provided": None,
                    "service_provided_at": None,
                    "description": None,
                    "comment": None,
                    "payer_counterparty": {
                        "name": "Walc Magdalena",
                        "type": "Private person",
                        "code": None,
                        "public_legal_registry_code": None,
                        "residency": None,
                        "account_no": None,
                        "contact_person_name": None,
                        "contact_person_surname": None,
                        "phone_num_main": None,
                        "initial_phone_num": None,
                        "additional_phone_nums": None,
                        "email": None,
                        "address": {
                            "country": None,
                            "country_name": None,
                            "state": None,
                            "region": None,
                            "county": None,
                            "city": None,
                            "district": None,
                            "address": None,
                            "street": None,
                            "building": None,
                            "apt": None,
                            "zipcode": None,
                            "latitude": None,
                            "longitude": None,
                            "lang": None,
                            "channel": None,
                            "comments": None
                        },
                        "service_data": {
                            "master_system_id": None,
                            "master_id": None
                        }
                    },
                    "partner_code": "238",
                    "partner_name": "Nova Global US Inc",
                    "name": "TOP",
                    "key": "26",
                    "payer_type": "Consignee",
                    "payment_type": "Cashless"
                }
            ]
        },
        "shipment_info": {
            "pcs_description": [
                {
                    "id": "1",
                    "index": "1",
                    "length": "10",
                    "width": "10",
                    "height": "10",
                    "actual_weight": "0.26",
                    "volume_weight": "0.2",
                    "control_length": None,
                    "control_width": None,
                    "control_height": None,
                    "control_actual_weight": None,
                    "control_volume_weight": "0",
                    "barcode": "TOP0000000111111209NGUS",
                    "description": None,
                    "pack_num": "TOP0000000111111209NGUS",
                    "volume": "0.001",
                    "control_volume": "0",
                    "parcel_type": None,
                    "status": None
                }
            ]
        },
        "invoices": [
            {
                "currency": "GBP",
                "incoterms": "EXW",
                "invoice_details": [
                    {
                        "customs_code": "6404110000",
                        "material": "Artificial fabrics handmade",
                        "description": "Shoes - polyurethane",
                        "quantity": 1,
                        "units": "package",
                        "cost_per_unit": 100,
                        "subtotal_cost_per_good": 100,
                        "origin": "GB"
                    }
                ]
            }
        ],
        "general_cost_info": {
            "declared_cost": "19.8",
            "declared_currency": "USD",
            "cost": None,
            "currency": None,
            "domestic_currency_cost": None,
            "domestic_currency": None,
            "discount_code": None,
            "discount_value": None,
            "promo_code": None,
            "cod": {
                "amount": None,
                "domestic_currency_amount": None,
                "currency": None,
                "counterparty": {
                    "name": None,
                    "type": None,
                    "code": None,
                    "public_legal_registry_code": None,
                    "residency": None,
                    "account_no": None,
                    "contact_person_name": None,
                    "contact_person_surname": None,
                    "phone_num_main": None,
                    "initial_phone_num": None,
                    "email": None,
                    "address": {
                        "country": None,
                        "country_name": None,
                        "state": None,
                        "region": None,
                        "county": None,
                        "city": None,
                        "district": None,
                        "address": None,
                        "street": None,
                        "building": None,
                        "apt": None,
                        "zipcode": None,
                        "latitude": None,
                        "longitude": None,
                        "lang": None,
                        "channel": None,
                        "comments": None
                    },
                    "service_data": {
                        "master_system_id": None,
                        "master_id": None
                    },
                    "additional_phone_nums": [
                        None
                    ]
                }
            }
        }
    }
}
