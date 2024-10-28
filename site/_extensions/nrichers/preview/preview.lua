-- preview.lua

-- Track if CSS has already been added to prevent duplication
local css_added = false

-- Helper function to add a CSS file to the document header
function add_css(doc)
  if not css_added then
    local css_file = "/_extensions/nrichers/preview/preview.css"
    table.insert(doc.blocks, 1, pandoc.RawBlock("html", "<link rel=\"stylesheet\" href=\"" .. css_file .. "\">"))
    css_added = true
  end
end

-- Main function to apply preview
function Div(el)
  if el.classes:includes("preview") then
    -- Get the `source` attribute, defaulting to "index.qmd" if missing
    local source = el.attributes.source or "index.qmd"
    source = source:gsub("%.qmd$", ".html")

    -- Get the `target` attribute, defaulting to `source` if missing
    local target = el.attributes.target or el.attributes.source or "index.qmd"
    target = target:gsub("%.qmd$", ".html")

    -- Generate the HTML content for the preview div
    local iframeHtml = string.format(
      '<div class="preview">\n' ..
      '  <iframe src="%s" width="400" height="225"></iframe>\n' ..
      '  <a href="%s" target="_blank"></a>\n' ..
      '</div>', source, target
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
