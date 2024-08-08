tools = [{
          "type": "function",
          "function": {
            "name": "test",
            "description": "рассказать сказку о колобке",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g., San Francisco, CA"
                },
                "unit": {
                  "type": "string",
                  "enum": ["Celsius", "Fahrenheit"],
                  "description": "The temperature unit to use. Infer this from the user's location."
                }
              },
              "required": ["location", "unit"]
            }
          }
        },
      ]
