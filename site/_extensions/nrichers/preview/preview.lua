-- preview.lua

-- Track if CSS has already been added to prevent duplication
local css_added = false

-- Helper function to add a CSS file to the document header
function add_css(doc)
  if not css_added then
    local css_file = "/_extensions/nrichers/preview/preview.css"
    table.insert(doc.blocks, 1, pandoc.RawBlock("html", "<link rel=\"stylesheet\" href=\"" .. css_file .. "\">"))
    css_added = true  -- Set the flag so CSS is only added once
  end
end

-- Main function to apply course preview
function Div(el)
  if el.classes:includes("preview") then
    -- Get the `src` attribute, defaulting to "default-page.html" if missing
    local src = el.attributes.src or "default-page.html"
    
    -- Replace .qmd with .html in the source
    src = src:gsub("%.qmd$", ".html")

    -- Generate the HTML content for the course preview div
    local iframeHtml = string.format(
      '<div class="preview">\n' ..
      '  <iframe src="%s" width="400" height="225"></iframe>\n' ..
      '  <a href="%s" target="_blank"></a>\n' ..
      '</div>', src, src
    )

    -- Return the raw HTML to be inserted
    return pandoc.RawBlock("html", iframeHtml)
  end
end

-- Ensure CSS is added once per document
function Pandoc(doc)
  add_css(doc)
  return doc
end
