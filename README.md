# py-reddit-expunger

Created by Weidi Zhang

## Description

py-reddit-expunger is a way to edit all your comments on Reddit to remove the contents.
This is important for privacy because straight up deleting the comments results in the original comment content
being stored on Reddit servers, and also they can still be accessed via deleted comment viewing sites.

## Obtaining Client Keys

1. Go to https://www.reddit.com/prefs/apps/
2. Hit "create another app..."
3. Choose "script" for type
4. Put anything, such as http://localhost, for redirect uri
5. Use the keys for this script

## Limitations

Default comment limit is set to 1000 as this is reportedly the limitation of Reddit in fetching comment history.
This can, however, be changed using the ```--limit``` option.

## Usage

To see usage:
```
python3 CLI.py --help
```

## License

Please read LICENSE.md to learn about what you can and cannot do with this source code.