import yaml
import os
import os.path as path


# Set configs and paths
root_dir = os.getenv('SYNTAXNET_ROOT_DIR')
parser_eval_path = os.getenv('SYNTAXNET_PARSER_EVAL')
context_path = os.getenv('SYNTAXNET_CONTEXT')
model_path = os.getenv('SYNTAXNET_MODEL')
