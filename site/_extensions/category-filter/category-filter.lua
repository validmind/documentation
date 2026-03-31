-- Category Filter Lua Extension
-- Reads listing-filter from YAML frontmatter and injects config as a data attribute

local function meta_to_native(val)
  if val == nil then
    return nil
  end
  
  local mt = getmetatable(val)
  
  -- Check for pandoc List type (used for YAML arrays)
  if mt and mt.__name == "List" then
    local arr = {}
    for i, item in ipairs(val) do
      arr[i] = meta_to_native(item)
    end
    return arr
  end
  
  -- Check for pandoc Inlines (YAML string values become Inlines)
  if mt and (mt.__name == "Inlines" or mt.__name == "Blocks") then
    return pandoc.utils.stringify(val)
  end
  
  -- Plain Lua types
  local t = type(val)
  if t == "string" or t == "number" or t == "boolean" then
    return val
  elseif t == "table" then
    -- Check if it's an array-like table
    if #val > 0 and val[1] ~= nil then
      local arr = {}
      for i, item in ipairs(val) do
        arr[i] = meta_to_native(item)
      end
      return arr
    else
      -- It's a map/object
      local obj = {}
      for k, v in pairs(val) do
        obj[k] = meta_to_native(v)
      end
      return obj
    end
  end
  
  -- Fallback: try stringify
  return pandoc.utils.stringify(val)
end

function Meta(meta)
  if meta['listing-filter'] then
    local config = meta_to_native(meta['listing-filter'])
    local json = quarto.json.encode(config)
    local escaped = json:gsub("'", "&#39;")
    quarto.doc.include_text("after-body",
      '<div id="listing-filter-config" style="display:none" data-config=\'' .. escaped .. '\'></div>')
  end
end
