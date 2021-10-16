import argparse
import json

ap = argparse.ArgumentParser(description='run = python3 ilham_octony_kurniawan.py {path_log} -t (optional, json/text, default=text) -o {path_output}')
ap.add_argument("path_file", metavar='N', type=str,
	help="path file log")
ap.add_argument("-t", "--type", type=str, default="text",
	help="select file type json / text (default = text)")
ap.add_argument("-o", "--output", type=str,
	help="path to output convert file", required=True)
args = vars(ap.parse_args())

a = open(args["path_file"],'r')
text = a.read()
text_as_list = text.split('\n')
keys = text_as_list[0].split()
result = []
path_json = args['output']
path_txt = args['output']

for item in text.split('\n')[2:len(text_as_list)]:
    temp_dict = {}  
    for i,j in zip(keys,item.split()):  
        if j.isdigit():         
            temp_dict[i] = int(j)
        else:
            temp_dict[i] = j
    result.append(temp_dict)

if args["type"] == "json":
    result_json = {
        "file_json" : result
    }
    with open(args['output'], 'w') as f:
        json.dump(result_json, f)

elif args["type"] == "text":
    with open(args['output'], 'w') as f:
        for parse_list in result:
            for key, value in parse_list.items():
                f.write('%s:%s\n' % (key, value))

else:
    print("try again please input -t {text or json}")
        