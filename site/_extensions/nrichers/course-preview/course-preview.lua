-- course-preview.lua

function Div(el)
  if el.classes:includes("course-preview") then
    -- Get the `src` attribute, defaulting to "default-page.html" if missing
    local src = el.attributes.src or "default-page.html"
    
    -- Replace .qmd with .html in the source
    src = src:gsub("%.qmd$", ".html")

    -- Generate the HTML content for the course preview div
    local iframeHtml = string.format(
      '<div class="course-preview">\n' ..
      '  <iframe src="%s" width="400" height="225"></iframe>\n' ..
      '  <a href="%s" target="_blank"></a>\n' ..
      '</div>', src, src
    )

    -- Return the raw HTML to be inserted
    return pandoc.RawBlock("html", iframeHtml)
  end
end
