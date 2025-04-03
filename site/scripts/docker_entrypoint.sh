#!/bin/sh
# Script to replace placeholders with actual URLs in HTML files and search.json

set -e

echo "==== Start ValidMind URL configuration ===="

# Define paths
CONFIG_FILE="/usr/share/nginx/html/config.json"
HTML_DIR="/usr/share/nginx/html"

# Define placeholder values, same as in modify_urls.sh
VALIDMIND_PLACEHOLDER="https://app.prod.validmind-configurable-url.ai"
JUPYTERHUB_PLACEHOLDER="https://jupyterhub.validmind-configurable-url.ai"

echo "Initializing ValidMind documentation site..."

# Initialize variables as empty
VALIDMIND_URL=""
JUPYTERHUB_URL=""

# First check environment variables
if [ -n "${VALIDMIND_URL:-}" ]; then
    VALIDMIND_URL="$VALIDMIND_URL"
    echo "Using VALIDMIND_URL from environment: $VALIDMIND_URL"
fi

if [ -n "${JUPYTERHUB_URL:-}" ]; then
    JUPYTERHUB_URL="$JUPYTERHUB_URL"
    echo "Using JUPYTERHUB_URL from environment: $JUPYTERHUB_URL"
fi

# If still empty, try config.json
if { [ -z "$VALIDMIND_URL" ] || [ -z "$JUPYTERHUB_URL" ]; } && [ -f "$CONFIG_FILE" ]; then
    echo "Looking for values in config file: $CONFIG_FILE"
    
    if command -v jq > /dev/null 2>&1; then
        # Use jq if available
        [ -z "$VALIDMIND_URL" ] && VALIDMIND_URL=$(jq -r '.VALIDMIND_URL // empty' "$CONFIG_FILE")
        [ -z "$JUPYTERHUB_URL" ] && JUPYTERHUB_URL=$(jq -r '.JUPYTERHUB_URL // empty' "$CONFIG_FILE")
    else
        # Simple fallback if jq isn't available
        [ -z "$VALIDMIND_URL" ] && VALIDMIND_URL=$(grep -o '"VALIDMIND_URL":"[^"]*"' "$CONFIG_FILE" 2>/dev/null | sed 's/"VALIDMIND_URL":"//;s/"//g')
        [ -z "$JUPYTERHUB_URL" ] && JUPYTERHUB_URL=$(grep -o '"JUPYTERHUB_URL":"[^"]*"' "$CONFIG_FILE" 2>/dev/null | sed 's/"JUPYTERHUB_URL":"//;s/"//g')
    fi
    
    [ -n "$VALIDMIND_URL" ] && echo "Using VALIDMIND_URL from config: $VALIDMIND_URL"
    [ -n "$JUPYTERHUB_URL" ] && echo "Using JUPYTERHUB_URL from config: $JUPYTERHUB_URL"
fi

# Finally, use hardcoded defaults as a last resort
if [ -z "$VALIDMIND_URL" ]; then
    VALIDMIND_URL="https://app.prod.validmind.ai"
    echo "Using default VALIDMIND_URL: $VALIDMIND_URL"
fi

if [ -z "$JUPYTERHUB_URL" ]; then
    JUPYTERHUB_URL="https://jupyterhub.validmind.ai"
    echo "Using default JUPYTERHUB_URL: $JUPYTERHUB_URL"
fi

# Final check to ensure we have non-empty values
if [ -z "$VALIDMIND_URL" ] || [ -z "$JUPYTERHUB_URL" ]; then
    echo "Error: One or both URLs are still empty. This will cause replacement issues."
    exit 1
fi

# Count total placeholder instances
VALIDMIND_COUNT=$(grep -r "$VALIDMIND_PLACEHOLDER" "$HTML_DIR" | wc -l)
JUPYTERHUB_COUNT=$(grep -r "$JUPYTERHUB_PLACEHOLDER" "$HTML_DIR" | wc -l)
echo "Found placeholders:"
echo "$VALIDMIND_COUNT instances of $VALIDMIND_PLACEHOLDER"
echo "$JUPYTERHUB_COUNT instances of $JUPYTERHUB_PLACEHOLDER"

# Replace placeholders in HTML files
echo "Replacing URL placeholders in HTML files..."
find "$HTML_DIR" -type f -name "*.html" -exec sed -i "s|$VALIDMIND_PLACEHOLDER|$VALIDMIND_URL|g" {} \;
find "$HTML_DIR" -type f -name "*.html" -exec sed -i "s|$JUPYTERHUB_PLACEHOLDER|$JUPYTERHUB_URL|g" {} \;

# Replace placeholders in search.json file
echo "Replacing URL placeholders in search.json..."
if [ -f "$HTML_DIR/search.json" ]; then
    sed -i "s|$VALIDMIND_PLACEHOLDER|$VALIDMIND_URL|g" "$HTML_DIR/search.json"
    sed -i "s|$JUPYTERHUB_PLACEHOLDER|$JUPYTERHUB_URL|g" "$HTML_DIR/search.json"
else
    echo "search.json file not found"
fi

# Verify replacement
VALIDMIND_AFTER=$(grep -r "$VALIDMIND_PLACEHOLDER" "$HTML_DIR" | wc -l)
JUPYTERHUB_AFTER=$(grep -r "$JUPYTERHUB_PLACEHOLDER" "$HTML_DIR" | wc -l)
echo "After replacement:"
echo "$VALIDMIND_AFTER instances of $VALIDMIND_PLACEHOLDER"
echo "$JUPYTERHUB_AFTER instances of $JUPYTERHUB_PLACEHOLDER"

if [ "$VALIDMIND_AFTER" -eq 0 ] && [ "$JUPYTERHUB_AFTER" -eq 0 ]; then
    echo "✓ URL replacement completed successfully"
else
    echo "⚠ Some placeholders might not have been replaced"
    echo "Files still containing placeholders:"
    grep -l "$VALIDMIND_PLACEHOLDER" "$HTML_DIR" | head -5
    grep -l "$JUPYTERHUB_PLACEHOLDER" "$HTML_DIR" | head -5
fi

echo "==== URL configuration complete ===="
