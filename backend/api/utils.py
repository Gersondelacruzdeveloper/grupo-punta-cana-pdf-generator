
# get template content
def get_template_content(template_data):
    content = {}
    if template_data:
        for template in template_data:
            content['content'] = template.content
    return content
