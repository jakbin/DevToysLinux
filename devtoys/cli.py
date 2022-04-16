import argparse
import json
import yaml
import base64
from html import escape, unescape
from urllib.parse import quote, unquote

__version__ = "1.0.2"
package_name = "devtoys"

def format(file: str):
	with open(file, 'r+') as f:
		data = json.load(f)
		f.seek(0)
		rdata = json.dumps(data, indent=4, sort_keys=True)
		f.write(rdata)

def json_to_yaml(file: str):
	data = yaml.dump(json.load(open(file)))
	targetyaml = file.replace('json', 'yaml')
	with open(targetyaml, 'w') as f:
		f.write(data)

def yaml_to_json(file: str):
    data = yaml.safe_load(open(file))
    targetjson = file.replace('yaml', 'json')
    with open(file, 'r') as f_json, open(targetjson ,'w') as f_yaml:
        json.dump(data, f_yaml, indent=4)

def convert(file: str):
    if file.endswith('json'):
        json_to_yaml(file)
    elif file.endswith('yaml'):
        yaml_to_json(file)
    else:
        return 'file type not supported'

def base64_encode(text:str):
    text_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(text_bytes)
    base64_text = base64_bytes.decode('ascii')
    return print(base64_text)

def base64_decode(text:str):
    base64_bytes = text.encode('ascii')
    text_bytes = base64.b64decode(base64_bytes)
    text = text_bytes.decode('ascii')
    return print(text)

def html_encode(html:str):
    return print(escape(html))

def html_decode(html:str):
    return print(unescape(html))

def url_encode(url:str):
    return print(quote(url, safe=''))

def url_decode(url:str):
    return print(unquote(url))

def encode():
    num = input("Encode:- \n(1) base64 \n(2) html \n(3) url \nSelect option: ")
    if str(num) == '1':
        text = input('Enter your text: ')
        base64_encode(str(text))
    elif str(num) == '2':
        html = input('Enter your html: ')
        html_encode(html)
    elif str(num) == '3':
        url = input('Enter your url: ')
        url_encode(url)
    else:
        return 'Wrong option selected.'

def decode():
    num = input("Decode:- \n(1) base64 \n(2) html \n(3) url \nSelect option: ")
    if str(num) == '1':
        text = input('Enter your base64: ')
        base64_decode(str(text))
    elif str(num) == '2':
        html = input('Enter your html: ')
        html_decode(html)
    elif str(num) == '3':
        url = input('Enter your url: ')
        url_decode(url)
    else:
        return 'Wrong option selected.'

example_uses = '''example:
   devtoys format {filename.json}
   devtoys convert {filename.json}'''

def main(argv = None):
    parser = argparse.ArgumentParser(prog=package_name, description="upload your files on anonfile server", epilog=example_uses, formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest="command")

    format_parser = subparsers.add_parser("format", help="format json files")
    format_parser.add_argument("file", type=str, help="give file to format")

    convert_parser = subparsers.add_parser("convert", help="convert json to yaml and yaml to json")
    convert_parser.add_argument("file", type=str, help="give file to convert")

    decode_parser = subparsers.add_parser("decode", help="decode text")

    encode_parser = subparsers.add_parser("encode", help="encode text")

    parser.add_argument('-v',"--version",
                            action="store_true",
                            dest="version",
                            help="check version of devtoys")

    args = parser.parse_args(argv)

    if args.command == "format":
        return format(args.file)
    elif args.command == "convert":
        return convert(args.file)
    elif args.command == "decode":
        return decode()
    elif args.command == "encode":
        return encode()
    elif args.version:
        return print(__version__)
    else:
        parser.print_help()

if __name__ == '__main__':
    raise SystemExit(main())