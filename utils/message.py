def convert_result_to_message(result):
    if len(result) == 0:
        return "Sorry, we currently don't have any recipe pertaining to your food."
    message = ""
    for data in result:
        message += f"Food: {data['name']}\n"
        message += "Steps\n"
        count = 1
        for step in data['steps']:
            message += f"{count}. {step}\n"
            count += 1
        message += '\n\n'

    return message
