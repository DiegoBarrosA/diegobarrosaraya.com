#!/usr/bin/env python3
"""Update resume content from the resume generator repository."""

import requests
import base64
from datetime import datetime
import sys

def fetch_resume_content():
    """Fetch the latest resume markdown from the generator repository."""
    resume_url = "https://api.github.com/repos/DiegoBarrosA/diego-barros-resume-generator/contents/docs/resume.md"
    
    try:
        response = requests.get(resume_url)
        if response.status_code == 200:
            data = response.json()
            return base64.b64decode(data['content']).decode('utf-8')
        else:
            print(f"❌ Failed to fetch resume: HTTP {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error fetching resume: {e}")
        return None

def create_jekyll_resume(resume_content):
    """Create Jekyll-formatted resume page."""
    if not resume_content:
        return None
    
    # Clean up any existing front matter from the source
    lines = resume_content.split('\n')
    content_start = 0
    
    # Skip any existing front matter
    if lines[0].strip() == '---':
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                content_start = i + 1
                break
    
    clean_content = '\n'.join(lines[content_start:]).strip()
    
    # Create Jekyll front matter
    front_matter = f"""---
layout: default
title: Resume
description: "Diego Barros Araya - Senior IT Engineer Resume"
permalink: /resume/
last_updated: {datetime.now().strftime('%Y-%m-%d')}
robots: index, follow
sitemap_priority: 0.9
---

"""
    
    # Create footer with PDF download
    footer = f"""

---

**Last Updated**: {datetime.now().strftime('%B %d, %Y')}

<div style="text-align: center; margin: 20px 0;">
<a href="https://raw.githubusercontent.com/DiegoBarrosA/diego-barros-resume-generator/main/docs/resume.pdf" 
   class="btn btn-primary" 
   target="_blank" 
   rel="noopener"
   download="diego-barros-resume.pdf">
   📄 Download ATS-Optimized PDF Resume
</a>
</div>

*This resume is automatically synchronized with the latest version from the resume generator.*
"""
    
    return front_matter + clean_content + footer

def main():
    """Main function to update the resume."""
    print("🔄 Fetching latest resume content...")
    
    resume_content = fetch_resume_content()
    if not resume_content:
        print("❌ Failed to fetch resume content")
        sys.exit(1)
    
    print("✏️  Creating Jekyll resume page...")
    jekyll_content = create_jekyll_resume(resume_content)
    if not jekyll_content:
        print("❌ Failed to create Jekyll content")
        sys.exit(1)
    
    # Write to resume.md
    try:
        with open('resume.md', 'w', encoding='utf-8') as f:
            f.write(jekyll_content)
        print("✅ Resume updated successfully")
        print("📝 Jekyll page: resume.md")
        print("🔗 Will be available at: /resume/")
    except Exception as e:
        print(f"❌ Error writing resume file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()