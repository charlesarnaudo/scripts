import subprocess
import json
from treelib import Node, Tree


def run_cmd(cmd: str):
    proc = subprocess.Popen(
        cmd, shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, _ = proc.communicate()
    return(stdout.decode('utf-8').rstrip())


def traverse(path: str):
    result = run_cmd(f"vault kv list -format=json {path}")
    data = json.loads(result)
    for key in data:
        tree.create_node(key, f"{path}{key}", parent=path)
        traverse(f"{path}{key}")


secret = run_cmd(
    """vault secrets list -format=json | jq -r 'to_entries[] | select(.value.type =="kv") | .key'""")

tree = Tree()
tree.create_node(secret, secret)

traverse(secret)
tree.show()

