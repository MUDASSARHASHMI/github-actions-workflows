
def lambda_handler(event, context):
    print("Starting functions\n.....................................")
    if event["input"] == "Hello":
        return "World"
    else:
        raise ValueError("Input must be Hello")
