#!/usr/bin/env python3
"""Update resume content from the resume generator repository."""

import requests
import base64
from datetime import datetime

def main():
    # Fetch the resume markdown from the generator repository
    resume_url = "https://api.github.com/repos/DiegoBarrosA/diego-barros-resume-generator/contents/docs/resume.md"
    
    try:
        response = requests.get(resume_url)
        if response.status_code == 200:
            data = response.json()
            # Decode the base64 content
            resume_content = base64.b64decode(data['content']).decode('utf-8')
            
            # Create Jekyll front matter
            front_matter = f"""---
layout: default
title: Resume
description: "Diego Barros Araya - Senior IT Engineer Resume"
permalink: /resume/
last_updated: {datetime.now().strftime('%Y-%m-%d')}
---

"""
            
            # Create footer
            footer = f"""

---

**Last Updated**: {datetime.now().strftime('%B %d, %Y')}

[Download PDF Resume](https://raw.githubusercontent.com/DiegoBarrosA/diego-barros-resume-generator/main/docs/resume.pdf)
"""
            
            # Combine all content
            jekyll_content = front_matter + resume_content + footer
            
            # Write to resume.md
            with open('resume.md', 'w', encoding='utf-8') as f:
                f.write(jekyll_content)
            
            print("✅ Resume updated successfully")
        else:
            print(f"❌ Failed to fetch resume: {response.status_code}")
            exit(1)
    except Exception as e:
        print(f"❌ Error updating resume: {e}")
        exit(1)

if __name__ == "__main__":
    main()