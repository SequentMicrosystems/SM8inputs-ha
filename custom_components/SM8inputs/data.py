import lib8inputs
API = lib8inputs
DOMAIN = "SM8inputs"
NAME_PREFIX = "sm8i"
SM_MAP = {
    "binary_sensor": {
        "opto": {
                "chan_no": 8,
                "com": {
                    "get": "get_opto",
                },
        },
    },
}
