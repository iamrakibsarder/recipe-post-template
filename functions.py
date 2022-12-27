import openai


def heading2(text):
    output = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return output


def heading3(text):
    h3 = f'<!-- wp:heading {"level":3} --><h3>{text}</h3><!-- /wp:heading -->'
    return h3


def heading4(text):
    h4 = f'<!-- wp:heading {"level":4} --><h4>{text}</h4><!-- /wp:heading -->'
    return h4


def heading5(text):
    h5 = f'<!-- wp:heading {"level":5} --><h5>{text}</h5><!-- /wp:heading -->'
    return h5


def paragraph(text):
    output = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return output


def wp_headers(username, password):
    import base64
    credential = f'{username}:{password}'
    token = base64.b64encode(credential.encode())
    headers = {'Authorization': f'Basic {token.decode("utf-8")}'}
    return headers


def wp_posting(title, slug, post_content, excerpt, status='publish'):
    site_url = 'https://pentagrowthdigital.com/practice/wp-json/wp/v2/posts'
    datas = {
        'title': title,
        'slug': slug,
        'content': post_content,
        'status': status,
        'excerpt': excerpt
    }

    published = post(site_url, data=datas, headers=headers)
    print(f'{title} is posted!')


def wp_list(list_item):
    first = f'<!-- wp:list --><ul>'
    for item in list_item:
        first += f'<!-- wp:list-item --><li>{item}</li><!-- /wp:list-item -->'
    last = f'</ul><!-- /wp:list -->'
    code = first + last
    return code


# def dict_lists(dictionary):
#     first = f'<!-- wp:list --><ul>'
#     for key, value in dictionary.items():
#         first += f'<!-- wp:list-item --><li> <strong>{key.title()}</strong> : {value.title}</li><!-- /wp:list-item -->'
#     last = f'</ul><!-- /wp:list -->'
#     code = first + last
#     return code

def dict_list(dicts):
    start = '<!-- wp:list --><ul>'
    for key, value in dicts.items():
        start += f'<!-- wp:list-item --><li><strong>{key.title()}</strong>:  {value.title()}</li><!-- /wp:list-item -->'
    ends = '</ul><!-- /wp:list -->'
    code = start + ends
    return code


def media_from_url(image_url, phone_name):
    media_image = f'<!-- wp:image {{"align":"center","sizeSlug":"large"}} --><figure class="wp-block-image aligncenter size-large"><img src="{image_url}" alt="{phone_name} image"/><figcaption class="wp-element-caption">{phone_name}</figcaption></figure><!-- /wp:image -->'
    return media_image


def wp_tables(dictionary):
    code = '<!-- wp:table --><figure class="wp-block table"><table><tbody>'
    for key, value in dictionary.items():
        tr_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
        code += tr_data
    code += '</tbody></table></figure> <!-- /wp:table -->'
    return code


def openai_ans(text):
    import os
    from dotenv import load_dotenv
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_KEY')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    output = response.get('choices')[0].get('text')
    return output
