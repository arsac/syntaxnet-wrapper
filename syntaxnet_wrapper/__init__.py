import yaml
import os.path as path
import os.environ as env
print os.environ['HOME']

# Set configs and paths
root_dir = env['SYNTAXNET_ROOT_DIR']
parser_eval_path = env['SYNTAXNET_PARSER_EVAL']
context_path = env['SYNTAXNET_CONTEXT']
model_path = env['SYNTAXNET_MODEL']
