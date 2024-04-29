# nothing imported if you run this IT WILL WRITE OVER YOUR Default index.html file.

def create_html_file(filename, title, h1, body_content):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <!-- no link to stylesheet -->  
    </head>
    <body>
        <nav>
            <a href="index.html">Home</a> 
            <a href="about.html">About</a>
            <a href="experience.html">Experience</a>
            <a href="projects.html">Projects</a>
        </nav>
        <div class="content">
            <h1>{h1}</h1>
            <p>{body_content}</p>
        </div>
    </body>
    </html>
    """

    with open(filename, 'w') as file:
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
        print(f"Created {filename}.")

if __name__ == "__main__":
    main()
