import os

# Define folder structure
folders = ['docs', 'src', 'test']
files = {
    'README.md': '# Consent Nodes\n\n## Overview\n\nDescription of Consent Nodes.',
    'docs/overview.md': '# Overview\n\nDetailed overview of Consent Nodes.',
    'src/index.js': '// Entry point for Consent Nodes logic',
    'test/test.js': '// Unit tests for Consent Nodes'
}

# Create folders
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Create files
for path, content in files.items():
    with open(path, 'w') as f:
        f.write(content)

print("Folders and files created successfully.")