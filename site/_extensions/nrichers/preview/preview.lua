-- preview.lua

-- Track if CSS has already been added to prevent duplication
local css_added = false
local skip_filter = false  -- Default: Do not skip

-- Helper function to add a CSS file to the document header
function add_css(doc)
  if not css_added then
    local css_file = "/_extensions/nrichers/preview/preview.css"
    table.insert(doc.blocks, 1, pandoc.RawBlock("html", "<link rel=\"stylesheet\" href=\"" .. css_file .. "\">"))
    css_added = true
  end
end

-- Function to check metadata for `skip_preview`
function Meta(meta)
  -- Set `skip_filter` to true if `skip_preview` is set in the metadata
  if meta.skip_preview and meta.skip_preview == true then
    skip_filter = true
  end
end

-- Main function to apply preview
function Div(el)
  -- If the filter is skipped, do nothing
  if skip_filter then
    return nil
  end

  if el.classes:includes("preview") then
    -- Get the `source`, `target`, `width`, `height`, and `offset` attributes, with defaults if not specified
    local source = el.attributes.source or "index.qmd"
    local target = el.attributes.target or source
    local width = el.attributes.width or "400"
    local height = el.attributes.height or "225"
    local offset = el.attributes.offset or "0"  -- Offset in pixels to crop from the top

    -- Convert .qmd to .html for non-external sources
    if not source:match("^https?://") then
      source = source:gsub("%.qmd$", ".html")
    end
    if not target:match("^https?://") then
      target = target:gsub("%.qmd$", ".html")
    end

    -- Generate HTML with clip-path to crop the top content by the specified offset
    local iframeHtml = string.format(
      '<div class="preview" style="width:%spx; height:%spx; overflow:hidden;">\n' ..
      '  <iframe src="%s" style="width:100%%; height:calc(100%% + %spx); position:relative; top:-%spx; border:none; border-radius:5px;"></iframe>\n' ..
      '  <a href="%s" target="_blank"></a>\n' ..
      '</div>', width, height, source, offset, offset, target
    )

    -- Return the raw HTML to be inserted
    return pandoc.RawBlock("html", iframeHtml)
  end
end

-- Ensure CSS is added once per document
function Pandoc(doc)
  -- If the filter is skipped, do nothing
  if skip_filter then
    return doc
  end

  add_css(doc)
  return doc
end
