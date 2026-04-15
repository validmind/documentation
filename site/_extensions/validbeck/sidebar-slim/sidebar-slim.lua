-- Enables optional sidebar minimize/expand UI when `sidebar-slim: true`
-- is set in document or directory metadata.

local function sidebar_slim_enabled(meta)
  local v = meta.sidebar_slim or meta["sidebar-slim"]
  if v == nil then
    return false
  end
  if type(v) == "boolean" then
    return v
  end
  local s = pandoc.utils.stringify(v):lower()
  return s == "true" or s == "1" or s == "yes"
end

function Pandoc(doc)
  if not sidebar_slim_enabled(doc.meta) then
    return doc
  end
  if not quarto.doc.is_format("html:js") then
    return doc
  end

  quarto.doc.add_html_dependency({
    name = "validbeck-sidebar-slim",
    version = "1.0.0",
    stylesheets = { "sidebar-slim.css" },
    scripts = { "sidebar-slim.js" },
  })

  return doc
end
