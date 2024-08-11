assistant_tools = [{
    "type": "function",
    "function": {
        "name": "save_value",
        "description": "when you find out my key values, this function will save them to the database",
        "parameters": {
            "type": "object",
            "properties": {
                "key_value": {
                    "type": "string",
                    "description": "choose one key value and write it briefly in one or two words"
                },
            },
            "required": ["key_value", ]
        }
    }
},
    {
        "type": "file_search"
    }
]

completions_tool = [
    {
        "type": "function",
        "function": {
            "name": "validator",
            "description": "check if it can be of value to a person:"
                           "the response was received in the True or False format",
            "parameters": {
                "type": "object",
                "properties": {
                    "is_valid": {
                        "type": "string",
                        "enum": ["True", "False"],
                        "description": "choose the appropriate option",
                    },
                },
                "required": ["is_valid"],
                "additionalProperties": False,
            },
        }
    }
]
