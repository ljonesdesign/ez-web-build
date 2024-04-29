import os # need to import os module to output files to a build directory

def create_html_file(filename, title, h1, body_content, output_dir="build"):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" href="../assets/style.css"> <!-- this needed .. added to work -->
    </head>
    <body class="cover_img">
        <nav>
            <a href="index.html"{' class="active"' if filename == 'index.html' else''}>Home</a>
            <a href="about.html"{' class="active"' if filename == 'about.html' else''}>About</a>
            <a href="experience.html"{' class="active"' if filename == 'experience.html' else''}>Experience</a>
            <a href="projects.html"{' class="active"' if filename == 'projects.html' else''}>Projects</a>
        </nav>
        <div class="content">
            <h1>{h1}</h1>
            <p>{body_content}</p>
        </div>
    </body>
    </html>
    """

    output_path = os.path.join(output_dir, filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w') as file:
        file.write(html_content)

def main():
    pages = [
        ('index.html', 'Home', 'Welcome to my website', 'This is the homepage.'),
        ('about.html', 'About', 'About Me', 'This is the about content.'),
        ('experience.html', 'Experience', 'My Experience', 'This is the experience content.'),
        ('projects.html', 'Projects', 'My Projects', 'This is the projects content.')
    ]

    for page in pages:
        filename, title, h1, body_content = page
        create_html_file(filename, title, h1, body_content)
        print(f"Created {filename} in the 'build' directory.")

if __name__ == "__main__":
    main()
