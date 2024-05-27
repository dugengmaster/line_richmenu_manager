# LINE Rich Menu Manager

This script allows you to manage LINE Rich Menus. You can create, upload images, list, delete, and set default rich menus for a LINE Bot.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Create a Rich Menu](#create-a-rich-menu)
  - [Upload an Image for a Specific Rich Menu](#upload-an-image-for-a-specific-rich-menu)
  - [List All Available Rich Menu IDs](#list-all-available-rich-menu-ids)
  - [List Detailed Information for All Available Rich Menus](#list-detailed-information-for-all-available-rich-menus)
  - [Delete a Specific Rich Menu](#delete-a-specific-rich-menu)
  - [Set a Specific Rich Menu as the Default](#set-a-specific-rich-menu-as-the-default)
  - [Get the ID of the Currently Set Default Rich Menu](#get-the-id-of-the-currently-set-default-rich-menu)
  - [Cancel the Currently Set Default Rich Menu](#cancel-the-currently-set-default-rich-menu)
- [Example](#example)
- [Contributing](#contributing)

## Prerequisites

Make sure you have Python installed. You also need to install the `argparse` and `requests` modules if they are not already installed.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/dugengmaster/line_richmenu_manager.git
    ```

2. Navigate to the project directory:
    ```bash
    cd line_richmenu_manager
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the root of your project directory and add your LINE channel access token:
    ```plaintext
    LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
    ```

2. Ensure your project structure looks like this:
    ```
    line_richmenu_manager/
    ├── images/
    ├── rich_menu_configs/
    ├── .env
    ├── settings.py
    ├── line_richmenu_manager.py
    └── requirements.txt
    ```

3. Place your JSON configuration files for rich menus in the `rich_menu_configs` directory. For example, you might have a file named `test.json`:
    ```
    line_richmenu_manager/
    ├── rich_menu_configs/
    │   └── test.json
    ```

4. Place your JPEG image files for rich menus in the `images` directory. For example, you might have a file named `menu_image.jpg`:
    ```
    line_richmenu_manager/
    ├── images/
    │   └── menu_image.jpg
    ```

## Usage

The script provides several commands to manage your LINE Rich Menus. Below are the available commands and their descriptions:

### Create a Rich Menu

To create a rich menu from a specified configuration file:
```bash
python line_richmenu_manager.py -C <rich_menu_config_name>
```

### Upload an Image for a Specific Rich Menu

To upload an image for a specific rich menu by providing its ID and the image file name:
```bash
python line_richmenu_manager.py -U <rich_menu_id> <image_name>
```

### List All Available Rich Menu IDs

To list all available rich menu IDs:
```bash
python line_richmenu_manager.py -L
```

### List Detailed Information for All Available Rich Menus

To list detailed information for all available rich menus:
```bash
python line_richmenu_manager.py -LD
```

### Delete a Specific Rich Menu

To delete a specific rich menu by providing its ID:
```bash
python line_richmenu_manager.py -D <rich_menu_id>
```

### Set a Specific Rich Menu as the Default

To set a specific rich menu as the default by providing its ID:
```bash
python line_richmenu_manager.py -sd <rich_menu_id>
```

### Get the ID of the Currently Set Default Rich Menu

To get the ID of the currently set default rich menu:
```bash
python line_richmenu_manager.py -gd
```

### Cancel the Currently Set Default Rich Menu

To cancel the currently set default rich menu by providing its ID:
```bash
python line_richmenu_manager.py -cd <rich_menu_id>
```

## Example

Here's an example of how to use the script:

1. Create a rich menu from a configuration file:

    ```bash
    python line_richmenu_manager.py -C rich_menu_configs/test.json
    ```
    **Expected output:**
    ```
    Rich Menu ID: <rich_menu_id>
    ```
2. Upload an image to the rich menu:
    ```bash
    python line_richmenu_manager.py -U <rich_menu_id> images/menu_image.jpg
    ```

3. List all rich menu IDs:
    ```bash
    python line_richmenu_manager.py -L
    ```
    **Expected output:**
    ```
    richMenuId: <rich_menu_id_1>
    name: <rich_menu_name_1>
    richMenuId: <rich_menu_id_2>
    name: <rich_menu_name_2>
    ```
4. List detailed information for all rich menus:
    ```bash
    python line_richmenu_manager.py -LD
    ```
    **Expected output:**
    ```
    richMenuId: <rich_menu_id_1>
    name: <rich_menu_name_1>
    size: [2500, 1686]
    chatBarText: <chat_bar_text_1>
    selected: false
    areas:
      [x, y, width, height] [action_type, action_data]
    
    richMenuId: <rich_menu_id_2>
    name: <rich_menu_name_2>
    size: [2500, 1686]
    chatBarText: <chat_bar_text_2>
    selected: false
    areas:
      [x, y, width, height] [action_type, action_data]
    
    ```

5. Set a rich menu as the default:
    ```bash
    python line_richmenu_manager.py -sd <rich_menu_id>
    ```
6. Get the ID of the currently set default rich menu:
    ```bash
    python line_richmenu_manager.py -gd
    ```
    **Expected output:**
    ```
    Rich Menu ID: <rich_menu_id>
    ```
7. Cancel the currently set default rich menu:
    ```bash
    python line_richmenu_manager.py -cd <rich_menu_id>
    ```

### Error Handling

Example error outputs you may encounter:

1. If there is no image set to the rich menu (400 Bad Request):
    ```python
    (400, '[{"message": "must upload richmenu image before applying it to user", "details": []}]')
    ```

2. If you specify a non-existent rich menu (404 Not Found):
    ```python
    (404, '[{"message": "Not found"}]')
    ```
## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.
