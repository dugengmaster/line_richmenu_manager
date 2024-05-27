from settings import (
    LINE_CHANNEL_ACCESS_TOKEN,
    CONFIGS_DIR,
    IMAGES_DIR,
    )
import requests
import json
import os

def create_headers(content_type=None):
    if content_type is not None:
        return {
            "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
            "Content-Type": content_type
        }
    else:
        return {"Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}"}

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            return "Configuration file not found."
        except json.JSONDecodeError:
            return "Invalid JSON in configuration file."
        except requests.RequestException as e:
            return f"HTTP Request failed: {str(e)}"
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return wrapper

@error_handler
def create_rich_menu(config_name):
    config_path = os.path.join(CONFIGS_DIR, config_name)
    api = "https://api.line.me/v2/bot/richmenu"
    headers = create_headers("application/json")

    with open(config_path, "r", encoding="utf-8") as file:
        rich_menu = json.load(file)
        response = requests.post(api, headers=headers, data=json.dumps(rich_menu).encode("utf-8"))
        if response.status_code == 200:
            rich_menu_id = response.json()['richMenuId']
            return f"Rich Menu ID: {rich_menu_id}"
        else:
            return response.status_code, response.text

@error_handler
def upload_rich_menu_image(richMenuId, image_name):
    image_path = os.path.join(IMAGES_DIR, image_name)
    api = f"https://api-data.line.me/v2/bot/richmenu/{richMenuId}/content"
    headers = create_headers("image/jpeg")
    with open(image_path, "rb") as file:
        response = requests.post(api, headers=headers, data=file)
        if response.status_code == 200:
            return None
        else:
            return response.status_code, response.text

@error_handler
def get_rich_menu_list(method=None):
    headers = create_headers()
    api = f"https://api.line.me/v2/bot/richmenu/list"
    
    response = requests.get(api, headers=headers)
    if response.status_code != 200:
        return response.status_code, response.text
    else:
        if method is None:
            richmenus = response.json().get("richmenus", [])
            result = ""
            for richmenu in richmenus:
                result += f"richMenuId: {richmenu['richMenuId']}\nname: {richmenu['name']}\n"
            return result
        elif method == "details":
            richmenus = response.json().get("richmenus", [])
            result = ""
            for richmenu in richmenus:
                result += (
                    f"richMenuId: {richmenu['richMenuId']}\n"
                    f"name: {richmenu['name']}\n"
                    f"size: [{richmenu['size']['width']}, {richmenu['size']['height']}]\n"
                    f"chatBarText: {richmenu['chatBarText']}\n"
                    f"selected: {str(richmenu['selected']).lower()}\n"
                    f"areas:\n"
                )
                for area in richmenu['areas']:
                    bounds = area['bounds']
                    action = area['action']
                    action_type = action['type']
                    
                    action_data = ''
                    if action_type == 'postback':
                        action_data = f"[data: {action.get('data', 'N/A')}, displayText: {action.get('displayText', 'N/A')}, inputOption: {action.get('inputOption', 'N/A')}, fillInText: {action.get('fillInText', 'N/A')}]"
                    elif action_type == 'message':
                        action_data = f"[text: {action.get('text', 'N/A')}]"
                    elif action_type == 'uri':
                        action_data = f"[uri: {action.get('uri', 'N/A')}, altUri: {action.get('altUri', {}).get('desktop', 'N/A')}]"
                    elif action_type == 'datetimepicker':
                        action_data = f"[data: {action.get('data', 'N/A')}, mode: {action.get('mode', 'N/A')}, initial: {action.get('initial', 'N/A')}, max: {action.get('max', 'N/A')}, min: {action.get('min', 'N/A')}]"
                    elif action_type == 'camera':
                        action_data = "[camera action]"
                    elif action_type == 'cameraRoll':
                        action_data = "[cameraRoll action]"
                    elif action_type == 'location':
                        action_data = "[location action]"
                    elif action_type == 'richmenuswitch':
                        action_data = f"[richMenuAliasId: {action.get('richMenuAliasId', 'N/A')}, data: {action.get('data', 'N/A')}]"
                    elif action_type == 'clipboard':
                        action_data = f"[clipboardText: {action.get('clipboardText', 'N/A')}]"
                    
                    result += (
                        f"  [{bounds['x']}, {bounds['y']}, {bounds['width']}, {bounds['height']}] "
                        f"[{action_type}, {action_data}]\n"
                    )
                result += "\n"
            return result.strip()

@error_handler
def delete_rich_menu(richMenuId):
    api = f"https://api.line.me/v2/bot/richmenu/{richMenuId}"
    headers = create_headers()
    
    response = requests.delete(api, headers=headers)
    if response.status_code != 200:
        return None
    else:
        return response.status_code, response.text

@error_handler
def get_default_rich_menu():
    api = f"https://api.line.me/v2/bot/user/all/richmenu"
    headers = create_headers()

    response = requests.get(api, headers=headers)
    if response.status_code == 200:
        rich_menu_id = response.json()['richMenuId']
        return f"Rich Menu ID: {rich_menu_id}"
    else:
        return response.status_code, response.text

@error_handler
def default_rich_menu(richMenuId, method):
    api = f"https://api.line.me/v2/bot/user/all/richmenu/{richMenuId}"
    headers = create_headers()
    
    if method == "set":
        response = requests.post(api, headers=headers)
        if response.status_code != 200:
            return response.status_code, response.text
    elif method == "cancel":
        if response.status_code != 200:
            return response.status_code, response.text
    else:
        return ValueError("Invalid method. Use 'set' or 'cancel'.")
    return None
