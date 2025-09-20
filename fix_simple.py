# Simple fix script using only ASCII characters

# Read the file in binary mode to avoid encoding issues
with open('index.html', 'rb') as f:
    content = f.read()

# Define search patterns using only ASCII characters
search_patterns = [
    b'python -m http.server 8000python -m http.server 8000     showStep(1);',
    b'python -m http.server 8000 python -m http.server 8000     showStep(1);'
]
replace_with = b'showStep(1);'

# Try to find and replace the pattern
fixed = False
for pattern in search_patterns:
    if pattern in content:
        content = content.replace(pattern, replace_with)
        fixed = True
        print(b"Found and fixed error pattern: ", pattern)
        break

# Save the fixed file
with open('index.html', 'wb') as f:
    f.write(content)

if fixed:
    print("index.html has been successfully fixed!")
else:
    print("Error: Could not find the pattern to fix. Please try manual editing.")