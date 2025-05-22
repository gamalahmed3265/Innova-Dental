import os

# Start building the HTML content
html = '''<section class="py-12 bg-gray-100">
  <div class="max-w-7xl mx-auto px-4">\n'''

# Walk through directories
for dirpath, dirnames, filenames in os.walk("."):
    # Skip current dir "."
    if dirpath == ".":
        continue
 
    # Clean up filenames (only images)
    images = [f for f in filenames if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.JPG'))]

    # Skip empty folders
    if not images:
        continue

    # Add category heading
    html += f'    <h3 class="text-2xl font-bold mb-4">{os.path.basename(dirpath)}</h3>\n'
    html += '    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">\n'

    # Add each image
    for img in images:
        html += f'''      <div class="overflow-hidden rounded-lg transform transition duration-300 hover:scale-105 hover:shadow-2xl">
        <img src="./assets/imgs/{dirpath}/{img}" alt="{img}" class="w-full h-auto object-cover transition-transform duration-500 hover:rotate-1">
      </div>\n'''

    html += '    </div>\n'

# Close the section
html += '  </div>\n</section>'

# Save to a file
with open("gallery.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Gallery HTML generated successfully in 'gallery.html'")