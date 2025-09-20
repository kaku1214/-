# Script to create a fixed version of index.html

# Read the original file
with open('index.html', 'rb') as f:
    content = f.read()

# Find the start and end positions of the problematic section
start_pattern = b'document.addEventListener(\'DOMContentLoaded\', () => {'
end_pattern = b'        });\n    </script>\n</body>\n</html>'

start_pos = content.find(start_pattern)
end_pos = content.rfind(end_pattern)

if start_pos != -1 and end_pos != -1:
    # Extract the content before the problematic section
    before = content[:start_pos]
    
    # Define the correct JavaScript code
    correct_js = b'''document.addEventListener('DOMContentLoaded', () => {
            // Add smooth scrolling
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href')).scrollIntoView({
                        behavior: 'smooth'
                    });
                });
            });
            
            // Initialize step display
            showStep(1);
            
            // Ensure beginner questions are shown
            beginnerQuestions.classList.remove('hidden');
            nonBeginnerQuestions.classList.add('hidden');
        });
    </script>
</body>
</html>'''
    
    # Create the fixed content
    fixed_content = before + correct_js
    
    # Save as a new file
    with open('index_fixed.html', 'wb') as f:
        f.write(fixed_content)
    
    print("Success! Created index_fixed.html with corrected JavaScript code.")
    print("Please use this file instead of the original index.html.")
else:
    print("Error: Could not find the correct positions in the file.")
    print("Please try manual editing of index.html.")