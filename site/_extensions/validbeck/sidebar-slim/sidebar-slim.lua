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

local function truthy_meta(meta, key_hyphen, key_underscore)
  local v = meta[key_underscore] or meta[key_hyphen]
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

  local narrow_default = truthy_meta(doc.meta, "sidebar-narrow", "sidebar_narrow")
  local cfg = { sidebarNarrow = narrow_default }
  quarto.doc.include_text(
    "in-header",
    '<script type="application/json" id="validbeck-sidebar-slim-config">'
      .. quarto.json.encode(cfg)
      .. "</script>"
  )

  quarto.doc.add_html_dependency({
    name = "validbeck-sidebar-slim",
    version = "1.0.3",
    stylesheets = { "sidebar-slim.css" },
    scripts = { "sidebar-slim.js" },
  })

  return doc
end
