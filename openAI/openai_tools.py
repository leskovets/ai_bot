tools = [{
            "type": "function",
            "function": {
                "name": "save_value",
                "description": "before replying to each message, analyze the story, find my hobby",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "choose one hobby and write to me in one word"
                        },
                    },
                    "required": ["location", ]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_rain_probability",
                "description": "Get the probability of rain for a specific location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g., San Francisco, CA"
                        }
                    },
                    "required": ["location"]
                }
            }
        }]
