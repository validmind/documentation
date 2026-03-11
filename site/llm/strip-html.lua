-- Copyright © 2023-2026 ValidMind Inc. All rights reserved.
-- Lua filter to strip HTML and unwrap divs for LLM output.
-- Used by Pandoc in clean.sh post-processing.

-- Strip raw HTML blocks
function RawBlock(el)
  if el.format == "html" then
    return {}
  end
end

-- Strip raw HTML inlines
function RawInline(el)
  if el.format == "html" then
    return {}
  end
end

-- Unwrap fenced divs (keep content)
function Div(el)
  return el.content
end
