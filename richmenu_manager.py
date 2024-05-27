from line_api_utils import *
import argparse

def main():
    parser = argparse.ArgumentParser(description='Manage LINE Rich Menus. This script allows creating, uploading images, listing, deleting, and setting default rich menus for a LINE Bot.')
    parser.add_argument('-C', '--create', metavar='rich_menu_config', help='Create a rich menu from a specified configuration file.')
    parser.add_argument('-U', '--upload', nargs=2, metavar=('rich_menu_id', 'image_name'), help='Upload an image for a specific rich menu by providing its ID and the image file name.')
    parser.add_argument('-L', '--list-ids', action='store_true', help='List all available rich menu IDs.')
    parser.add_argument('-LD', '--list-details', action='store_true', help='List detailed information for all available rich menus.')
    parser.add_argument('-D', '--delete', metavar='rich_menu_id', help='Delete a specific rich menu by providing its ID.')
    parser.add_argument('-sd', '--set-default', metavar='rich_menu_id', help='Set a specific rich menu as the default by providing its ID.')
    parser.add_argument('-gd', '--get-default', action='store_true', help='Get the ID of the currently set default rich menu.')
    parser.add_argument('-cd', '--cancel-default', metavar='rich_menu_id', help='Cancel the currently set default rich menu by providing its ID.')

    args = parser.parse_args()

    if args.create:
        return print(create_rich_menu(args.create))
    elif args.upload:
        rich_menu_id, image_name = args.upload
        response = upload_rich_menu_image(rich_menu_id, image_name)
        if response is not None:
            return print(response)
    elif args.list_ids:
        response = get_rich_menu_list()
        if response is not None:
            return print(response)
    elif args.list_details:
        response = get_rich_menu_list("details")
        if response is not None:
            return print(response)
    elif args.delete:
        response = delete_rich_menu(args.delete)
        if response is not None:
            return print(response)
    elif args.set_default:
        response = default_rich_menu(args.set_default, "set")
        if response is not None:
            return print(response)
    elif args.get_default:
        response = get_default_rich_menu()
        if response is not None:
            return print(response)
    elif args.cancel_default:
        response = default_rich_menu(args.cancel_default, "cancel")
        if response is not None:
            return print(response)

if __name__ == "__main__":
    main()