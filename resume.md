---
layout: default
title: Resume
description: "Diego Barros Araya - Senior IT Engineer Resume"
permalink: /resume/
---

# Resume

<div class="text-center" style="margin-bottom: 30px;">
    <button id="download-pdf-link" class="btn btn-primary">
        <i class="fa-solid fa-file-pdf"></i> Download PDF Resume
    </button>
</div>

<div id="resume-display" class="card">
    <div id="resume-content">
        <p class="text-center text-muted">
            <i class="fa-solid fa-spinner fa-spin"></i> Loading resume...
        </p>
    </div>
</div>

{% include resume-manager.html %}